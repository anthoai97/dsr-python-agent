from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
from dsr_agent.agent_service_pb2 import SimplePackage, PackageMetadata, JsonMsgPack

class MessagePackage:
	def __init__(
		self,
		agent: str  = "DataSpire",
		agent_id: str = "dataspire-agent",
		message_id: str = "dataspire-agent-message-id",
		deadline: datetime = datetime.now()
	) -> None:
		self.agent_id = agent_id
		self.agent = agent
		self.message_id = message_id
		self.deadline = deadline
		self.data = []
		self.resend = 0

	def setData(self, data: any):
		self.data.append(data)

	def setMessageID(self, id: str = None):
		if id != None:
			self.message_id = id

	def toMessage(self):
		return {
			'agent': self.agent,
			'agent_id': self.agent_id,
			'data': self.data,
			'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
			'resend': self.resend,
		}
	
	def toGRPCSimplePackage(self) ->  SimplePackage:
		return SimplePackage(
				metadata=PackageMetadata(
				agent=self.agent,
				agent_id=self.agent_id,
				timestamp=Timestamp().FromDatetime(datetime.now()),
				message_id=self.message_id,
				resend=self.resend,
				type=0, 
			),
			data=self.data,
		)
	
	def toGRPCJsonPackage(self) ->  JsonMsgPack:
		return JsonMsgPack(
				metadata=PackageMetadata(
				agent=self.agent,
				agent_id=self.agent_id,
				timestamp=Timestamp().FromDatetime(datetime.now()),
				message_id=self.message_id,
				resend=self.resend,
				type=1, 
			),
			data=self.data,
		)

	def isReachDeadline(self) -> bool:
		now = datetime.now()
		if now < self.deadline:
			return False
		else:
			return True
		
	def setResend(self):
		self.resend += 1