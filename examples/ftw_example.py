import evalcontrol

evaluation_board = evalcontrol.AD9959(rfclk=500e6, clkmtp=1)

#ftw_110 = '00 01 00 00 01 01 00 00 01 01 00 00 01 01 00 00 01 01 00 00 01 01 00 00 01 01 00 00 01 01 00 01'

#ftw_80 = '00 00 01 00 01 00 00 00 01 01 01 01 00 01 00 01 01 01 00 00 00 00 01 00 01 00 00 00 01 01 01 01'

ftw_20 = evaluation_board.compute_ftw(20e6)
ftw_40 = evaluation_board.compute_ftw(40e6)
ftw_80 = evaluation_board.compute_ftw(80e6)
ftw_160 = evaluation_board.compute_ftw(160e6)

while(True):
	evaluation_board.set_ftw(ftw_20, channel=[1])
	evaluation_board.set_ftw(ftw_40, channel=[1])
	evaluation_board.set_ftw(ftw_80, channel=[1])
	evaluation_board.set_ftw(ftw_160, channel=[1])




