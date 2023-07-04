import threading
import time
import grpc
from datetime import datetime, timedelta
from google.protobuf.struct_pb2 import Struct

from dsr_agent import agent_service_pb2_grpc
from dsr_agent.message_package import MessagePackage
from dsr_agent.http_agent import AppType
from dsr_agent.logger import logger

class GRPCAgent:
	def __init__(
		self: AppType,
		*,
		agent_id: str = "dataspire-agent",
		agent_name: str = "DataSpire Agent",
		agent_type: int = 0, # 0 is string / 1 is json
		target: str = "localhost:8080",
		timeout: int = 10, # Secconds
		interval: int = 0, # Secconds
	) -> None:
		self.agent_id = agent_id
		self.agent_name = agent_name
		self.target = target
		self.timeout = timeout
		self.interval = interval
		self.agent_type = agent_type
		self.channel = grpc.insecure_channel(self.target)
		self.msgPack: MessagePackage = self._createMessagePackage()

	def _handleError(self, rpc_error: grpc.RpcError):
		logger.error(f"Call failed with code: {rpc_error.code()}")
		logger.error(f"Call failed with code: {rpc_error.debug_error_string()}")

	def _createMessagePackage(self) -> MessagePackage:
		now = datetime.now()
		return MessagePackage(
			agent_id = self.agent_id,
			agent = self.agent_name,
			deadline = now + timedelta(seconds= self.interval),
		)
	
	def sendString(self, data:any, id:str = None) -> None:
		self.msgPack.setData(data=str(data))
		self.msgPack.message_id = id
		self._send()
	
	def sendJson(self, data: any, id: str = None) -> None:
		s = Struct()
		s.update(data)
		self.msgPack.setData(data=s)
		self.msgPack.message_id = id
		self._send()
		
	def _send(self) -> None:
		if(self.msgPack.isReachDeadline() == False):
			return;
		# Async call
		thread = threading.Thread(target=self._executeRemote, args=(self.msgPack,), daemon=True)
		thread.start()
		self.msgPack = self._createMessagePackage()
	
	def _executeRemote(self, msgPack: MessagePackage) -> None:
		try:
			logger.info("Start execute send message")
			stub = agent_service_pb2_grpc.AgentServiceStub(self.channel)
			match self.agent_type:
				case 0:
					_ = stub.SendSimpleMsgPack(msgPack.toGRPCSimplePackage(), timeout= self.timeout)
				case 1:
					_ = stub.SendJsonMsgPack(msgPack.toGRPCJsonPackage(), timeout= self.timeout)
					
			logger.info("Send message successful")
		except grpc.RpcError as rpc_error:
			msgPack.setResend()
			self._handleError(rpc_error=rpc_error)