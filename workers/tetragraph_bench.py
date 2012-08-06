from lib import *
import time
import solve_substitution

start_time = time.time()
key = [i for i in 'zyxwvutsrqponmlkjihgfedcba'.upper()]
input = "Izdormth kozbvw uli Viwrmtglm Zoyrlm yvuliv qlrmrmt Dvhg Yilndrxs Zoyrlm rm  Sv hkvmg hrc hvzhlmh zg Gsv Szdgslimh yfg dzh mlg szmwvw srh Urihg Wrerhrlm wvyfg vrgsvi yb Qzxp Hnrgs li Erx Yfxprmtszn zmw dzh rmhgvzw zooldvw gl ovzev gsv Gsilhgovh uli Dzohzoo rm  Gsv Hzwwovih urmrhsvw gs rm gsv Gsriw Wrerhrlm Hlfgs rm  fmwvi gsv hgvdziwhsrk lu Qlsm Olev Mvd ylhh Yroo Nlliv xlfow lmob gzpv gsv xofy gl z gs kozxv urmrhs rm  dsrxs ovw gsvn gl yvxlnv ulfmwvi nvnyvih lu gsv Ulfigs Wrerhrlm Gsvb gsvm klhgvw z hrcgs kozxv urmrhs rm  hrc klrmgh zmw gdl kozxvh lfghrwv lu gsv kilnlgrlm kozxvh Dzohzoo gsvm glkkvw gsv wrerhrlm rm  yb z urev klrmg nzitrm gl drm z kozxv rm gsv Gsriw Wrerhrlm Dzohzoo gsvm urmrhsvw hvxlmw rm  hrc klrmgh yvsrmw xsznkrlmh Yfib gl drm z hvxlmw hfxxvhhrev kilnlgrlm Gsv Uvooldh Kzip xofy urmrhsvw gs rm gsv Hvxlmw Wrerhrlm rm  yvuliv hfuuvirmt ivovtzgrlm rm  wfv gl gsvri rmuvirli tlzo zeviztv gl gs kozxvw Xszioglm Zgsovgrx Rm srh hvevm bvzih zg gsv xofy Izdormth kozbvw z glgzo lu  ovztfv tznvh hxlirmt urev tlzoh Izdormth dzh hrtmvw yb Klig Ezov nzmztvi Uivwwrv Hgvvov uli z  uvv rm Qfmv  Sv nzwv  zkkvzizmxvh rm gsv  hvzhlm zmw kozbvw  tznvh rm gsv  xznkzrtm zh gsv Ezorzmgh hfuuvivw ivovtzgrlm lfg lu gsv Gsriw Wrerhrlm fmwvi Qzxprv Nfwrv Izdormth dzh trevm z uivv gizmhuvi gl Hlfgsvim Ovztfv hrwv Mfmvzglm Ylilfts rm Zkiro  Sv ozgvi gfimvw lfg uli slnvgldm xofy Xlovhsroo Gldm Sv ozgvi dlipvw uli Ofxzh Rmwfhgirvh"

proximity_to_english = 100;

for i in range(26):
	for j in range(i+1, 26):
		key_to_try = key[:]
		tmp = key_to_try[j]
		key_to_try[j] = key_to_try[i]
		key_to_try[i] = tmp

		plaintext = solve_substitution.decrypt_message( key_to_try, input )
		tetragraph = funcs.tetragraph_freq( plaintext )
		new_proximity_to_english = funcs.tetragraph_compare( tetragraph )

		if new_proximity_to_english < proximity_to_english:
			# this key is better
			key = key_to_try
			proximity_to_english = new_proximity_to_english


print time.time() - start_time, "seconds"