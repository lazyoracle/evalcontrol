import evalcontrol

evaluation_board = evalcontrol.AD9959(rfclk=500e6, clkmtp=1)

ACR_1024 = '00 00 00 00 00 00 00 00 00 00 00 01 00 00 01 01 01 01 01 01 01 01 01 01'
ACR_512 = '00 00 00 00 00 00 00 00 00 00 00 01 00 00 01 00 00 00 00 00 00 00 00 00'


#evaluation_board.set_ACR(ACR, channel=[1])

while(True):
	evaluation_board.set_ACR(ACR_1024, channel=[1])
	evaluation_board.set_ACR(ACR_512, channel=[1])

#print(evaluation_board._read_from_register(0x06, 24))

