import gammalib
import ctools
import cscripts

debug = True

detect = cscripts.cssrcdetect()
detect["inmap"]        = 'resmap_iem_add2_ext4.fits'
detect["outmodel"]     = 'models_add3.xml'
detect["outds9file"]   = 'ds9_4.reg'
detect["srcmodel"]     = 'POINT'
detect["bkgmodel"]     = 'NONE'
detect["threshold"]    = 5.0
detect["debug"]        = debug
detect.execute()
