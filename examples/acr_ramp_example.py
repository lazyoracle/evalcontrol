import evalcontrol

evaluation_board = evalcontrol.AD9959(rfclk=500e6, clkmtp=1)

ACR_0 = '00 00 00 00 00 00 00 00 00 00 00 01 00 00 01 01 01 01 01 01 01 01 01 01'
ACR_1 = '00 00 00 00 00 00 00 00 00 00 00 01 00 00 01 01 01 01 01 01 01 01 01 00'
ACR_2 = '00 00 00 00 00 00 00 00 00 00 00 01 00 00 01 01 01 01 01 01 01 01 00 00'
ACR_3 = '00 00 00 00 00 00 00 00 00 00 00 01 00 00 01 01 01 01 01 01 01 00 00 00'
ACR_4 = '00 00 00 00 00 00 00 00 00 00 00 01 00 00 01 01 01 01 01 01 00 00 00 00'
ACR_41= '00 00 00 00 00 00 00 00 00 00 00 01 00 00 01 01 01 01 01 00 01 01 00 00'
ACR_5 = '00 00 00 00 00 00 00 00 00 00 00 01 00 00 01 01 01 01 01 00 00 00 00 00'
ACR_51= '00 00 00 00 00 00 00 00 00 00 00 01 00 00 01 01 01 01 00 01 01 00 00 00'
ACR_6 = '00 00 00 00 00 00 00 00 00 00 00 01 00 00 01 01 01 01 00 00 00 00 00 00'
ACR_61= '00 00 00 00 00 00 00 00 00 00 00 01 00 00 01 01 01 00 01 01 00 00 00 00'
ACR_7 = '00 00 00 00 00 00 00 00 00 00 00 01 00 00 01 01 01 00 00 00 00 00 00 00'
ACR_71= '00 00 00 00 00 00 00 00 00 00 00 01 00 00 01 01 00 01 01 00 00 00 00 00'
ACR_8 = '00 00 00 00 00 00 00 00 00 00 00 01 00 00 01 01 00 00 00 00 00 00 00 00'
ACR_81= '00 00 00 00 00 00 00 00 00 00 00 01 00 00 01 00 01 01 01 00 00 00 00 00'
ACR_82= '00 00 00 00 00 00 00 00 00 00 00 01 00 00 01 00 01 01 00 00 00 00 00 00'
ACR_9 = '00 00 00 00 00 00 00 00 00 00 00 01 00 00 01 00 00 00 00 00 00 00 00 00'
ACR_91= '00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 01 01 01 01 00 00 00 00 00'
ACR_92= '00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 01 01 01 00 00 00 00 00 00'
ACR_93= '00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 01 01 00 00 00 00 00 00 00'
ACR_94= '00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 01 00 00 00 00 00 00 00 00'
ACR_10 = '00 00 00 00 00 00 00 00 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00'



'''
ACR_1023 = '00 00 00 00 00 00 00 00 00 00 00 01 00 00 01 01 01 01 01 01 01 01 01 01'
ACR_1022 = '00 00 00 00 00 00 00 00 00 00 00 01 00 00 01 01 01 01 01 01 01 01 01 00'
ACR_1021 = '00 00 00 00 00 00 00 00 00 00 00 01 00 00 01 01 01 01 01 01 01 01 00 01'
ACR_1020 = '00 00 00 00 00 00 00 00 00 00 00 01 00 00 01 01 01 01 01 01 01 01 00 00'
ACR_1019 = '00 00 00 00 00 00 00 00 00 00 00 01 00 00 01 01 01 01 01 01 01 00 01 01'
ACR_1018 = '00 00 00 00 00 00 00 00 00 00 00 01 00 00 01 01 01 01 01 01 01 00 01 00'
ACR_1017 = '00 00 00 00 00 00 00 00 00 00 00 01 00 00 01 01 01 01 01 01 01 00 00 01'
ACR_1016 = '00 00 00 00 00 00 00 00 00 00 00 01 00 00 01 01 01 01 01 01 01 00 00 00'
ACR_512 = '00 00 00 00 00 00 00 00 00 00 00 01 00 00 01 00 00 00 00 00 00 00 00 00'
'''


#evaluation_board.set_ACR(ACR, channel=[1])

while(True):
	evaluation_board.set_ACR(ACR_0, channel=[1])
	evaluation_board.set_ACR(ACR_1, channel=[1])
	evaluation_board.set_ACR(ACR_2, channel=[1])
	evaluation_board.set_ACR(ACR_3, channel=[1])
	evaluation_board.set_ACR(ACR_4, channel=[1])
	evaluation_board.set_ACR(ACR_41, channel=[1])
	evaluation_board.set_ACR(ACR_5, channel=[1])
	evaluation_board.set_ACR(ACR_51, channel=[1])
	evaluation_board.set_ACR(ACR_6, channel=[1])
	evaluation_board.set_ACR(ACR_61, channel=[1])
	evaluation_board.set_ACR(ACR_7, channel=[1])
	evaluation_board.set_ACR(ACR_71, channel=[1])
	evaluation_board.set_ACR(ACR_8, channel=[1])
	evaluation_board.set_ACR(ACR_81, channel=[1])
	evaluation_board.set_ACR(ACR_82, channel=[1])
	evaluation_board.set_ACR(ACR_9, channel=[1])
	evaluation_board.set_ACR(ACR_91, channel=[1])
	evaluation_board.set_ACR(ACR_92, channel=[1])
	evaluation_board.set_ACR(ACR_93, channel=[1])
	evaluation_board.set_ACR(ACR_94, channel=[1])
	evaluation_board.set_ACR(ACR_10, channel=[1])


#print(evaluation_board._read_from_register(0x06, 24))

