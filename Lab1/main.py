from typing import Tuple

class Environment:
	def __init__(self):
		self._initial_state=1
		self._allowed_action=[0,1]
		self._states=[1,2,3]
		self._current_state=self._initial_state

	def step(self,action:int)->Tuple[int,int]:
		if action not in self._allowed_action:
			raise ValueError("Action is not allowed")

		reward=0
		if action==0 and self._current_state==1:
			self._current_state=2
			reward=1
			return (self._current_state,reward)
		elif action==1 and self._current_state==1:
			self._current_state=3
			reward=10
			return (self._current_state,reward)
		elif action==0 and self._current_state==2:
			self._current_state=1
			reward=0
			return (self._current_state,reward)
		elif action==1 and self._current_state==2:
			self._current_state=3
			reward=1
			return (self._current_state,reward)
		elif action==0 and self._current_state==3:
			self._current_state=2
			reward=0
			return (self._current_state,reward)
		elif action==1 and self._current_state==3:
			self._current_state=3
			reward=10
			return (self._current_state,reward)

	def reset(self)->int:
		self._current_state=self._initial_state
		return self._current_state

env=Environment()
state=env.reset()

actions=[0,0,1,1,0,1]

print(f"Intial state is {state}")

for action in actions:
	next_state, reward=env.step(action)
	print(f"From state {state} to state {next_state} with action {action}, reward: {reward}")
	state=next_state
