from typing import Tuple

class Environment:
	def __init__(self,_allowed_action,_states):
		self.trf = {}
		self._initial_state=1
		self._allowed_action=_allowed_action
		self._states=_states
		self._current_state=self._initial_state
		print("Enter the transition")
		print("Format : current_state action next_state reward")
		for i in range((len(_allowed_action)*len(_states))):
			new=input().split(' ')
			new=[int(x) for x in new]
			s, a, n, r = new
			self.trf[s,a]=(n, r)

	def step(self,action:int)->Tuple[int,int]:
		perform = self.trf[(self._current_state,action)] #matching the dictonary to perform action
		if perform:
			n,r=perform
			self._current_state=n
			return (self._current_state,r)
		else:
			print("Error!!!")
			return 0

	def reset(self)->int:
		self._current_state=self._initial_state
		return self._current_state

st=input("Enter the states : ").split()
st=[int(x) for x in st]
ac=input("Enter the actions : ").split()
ac=[int(x) for x in ac]
env=Environment(st,ac)

state=env.reset()

act=input("Enter the actions to be performed : ").split()
act=[int(x) for x in act]
actions=act

print(f"Intial state is {state}")

for action in actions:
	next_state, reward=env.step(action)
	print(f"From state {state} to state {next_state} with action {action}, reward: {reward}")
	state=next_state
