import evalcontrol

evaluation_board = evalcontrol.AD9959(rfclk=500e6, clkmtp=1)

'''
state = 1
try:
	while True:
		if state == 1:
			evaluation_board.set_frequency(110e6, channel = [1])
			state = 0
		else:
			evaluation_board.set_frequency(0.0, channel = [1])
			state = 1
except:
	pass

'''
evaluation_board.set_frequency(100e6, channel=[1])


# set the relative phase of channel 0 to 90 degree
#evaluation_board.set_phase(90, channel=0)

print(evaluation_board._read_from_register(0x04, 32))

