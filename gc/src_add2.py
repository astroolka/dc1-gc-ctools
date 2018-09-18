import gammalib
import ctools
import cscripts

debug = True

detect = cscripts.cssrcdetect()
detect["inmap"]        = 'resmap_iem_add1_ext2.fits'
detect["outmodel"]     = 'models_add2.xml'
detect["outds9file"]   = 'ds9_3.reg'
detect["srcmodel"]     = 'POINT'
detect["bkgmodel"]     = 'NONE'
detect["threshold"]    = 7.0
detect["debug"]        = debug
detect.execute()
