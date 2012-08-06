from workers import solve_substitution

print 'Substituion cipher solver by Daniel Chatfield'
input = raw_input( 'Enter the ciphertext\n' )

"""
	Logic >
		Generate a key
"""

input = "Izdormth kozbvw uli Viwrmtglm Zoyrlm yvuliv qlrmrmt Dvhg Yilndrxs Zoyrlm rm  Sv hkvmg hrc hvzhlmh zg Gsv Szdgslimh yfg dzh mlg szmwvw srh Urihg Wrerhrlm wvyfg vrgsvi yb Qzxp Hnrgs li Erx Yfxprmtszn zmw dzh rmhgvzw zooldvw gl ovzev gsv Gsilhgovh uli Dzohzoo rm  Gsv Hzwwovih urmrhsvw gs rm gsv Gsriw Wrerhrlm Hlfgs rm  fmwvi gsv hgvdziwhsrk lu Qlsm Olev Mvd ylhh Yroo Nlliv xlfow lmob gzpv gsv xofy gl z gs kozxv urmrhs rm  dsrxs ovw gsvn gl yvxlnv ulfmwvi nvnyvih lu gsv Ulfigs Wrerhrlm Gsvb gsvm klhgvw z hrcgs kozxv urmrhs rm  hrc klrmgh zmw gdl kozxvh lfghrwv lu gsv kilnlgrlm kozxvh Dzohzoo gsvm glkkvw gsv wrerhrlm rm  yb z urev klrmg nzitrm gl drm z kozxv rm gsv Gsriw Wrerhrlm Dzohzoo gsvm urmrhsvw hvxlmw rm  hrc klrmgh yvsrmw xsznkrlmh Yfib gl drm z hvxlmw hfxxvhhrev kilnlgrlm Gsv Uvooldh Kzip xofy urmrhsvw gs rm gsv Hvxlmw Wrerhrlm rm  yvuliv hfuuvirmt ivovtzgrlm rm  wfv gl gsvri rmuvirli tlzo zeviztv gl gs kozxvw Xszioglm Zgsovgrx Rm srh hvevm bvzih zg gsv xofy Izdormth kozbvw z glgzo lu  ovztfv tznvh hxlirmt urev tlzoh Izdormth dzh hrtmvw yb Klig Ezov nzmztvi Uivwwrv Hgvvov uli z  uvv rm Qfmv  Sv nzwv  zkkvzizmxvh rm gsv  hvzhlm zmw kozbvw  tznvh rm gsv  xznkzrtm zh gsv Ezorzmgh hfuuvivw ivovtzgrlm lfg lu gsv Gsriw Wrerhrlm fmwvi Qzxprv Nfwrv Izdormth dzh trevm z uivv gizmhuvi gl Hlfgsvim Ovztfv hrwv Mfmvzglm Ylilfts rm Zkiro  Sv ozgvi gfimvw lfg uli slnvgldm xofy Xlovhsroo Gldm Sv ozgvi dlipvw uli Ofxzh Rmwfhgirvh"

solve_substitution.do_solve( input )