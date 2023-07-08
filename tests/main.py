import time
import sys
sys.path.append('../dataspire_agent')
from dsr_agent.grpc_agent import GRPCAgent

def run():
	target = "localhost:9090"
	agent1 = GRPCAgent(target=target)
	agent2 = GRPCAgent(target=target, agent_type=1)
	data = "Data "
	# async with asyncio.TaskGroup() as tg:
	for x in range(1000):
		data = "Data " + str(x)
		time.sleep(0.01)
		agent1.sendString(data={'request' : data},id=str(1))
		# agent2.sendJson(data={'request' : data}, id=str(1))


run()