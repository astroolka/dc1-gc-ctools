import gammalib
import ctools
import cscripts

debug = True

detect = cscripts.cssrcdetect()
detect["inmap"]        = 'resmap_iem.fits'
detect["outmodel"]     = 'models_add1.xml'
detect["outds9file"]   = 'ds9_2.reg'
detect["srcmodel"]     = 'POINT'
detect["bkgmodel"]     = 'NONE'
detect["threshold"]    = 15.0
detect["debug"]        = debug
detect.execute()
