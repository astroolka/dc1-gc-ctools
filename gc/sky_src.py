import gammalib
import ctools
import cscripts

debug = True

skymap = ctools.ctskymap()
skymap['inobs']        = 'obs_selected.xml'
skymap['outmap']       = 'skymap_bkgsubtract.fits'
skymap['emin']         = 0.1
skymap['emax']         = 100.0
skymap['nxpix']        = 600
skymap['nypix']        = 600
skymap['binsz']        = 0.02
skymap['coordsys']     = 'GAL'
skymap['proj']         = 'CAR'
skymap['xref']         = 0.0
skymap['yref']         = 0.0
skymap['bkgsubtract']  = 'IRF'
skymap["debug"]        = debug
skymap.execute()

detect = cscripts.cssrcdetect()
detect["inmap"]        = 'skymap_bkgsubtract.fits'
detect["outmodel"]     = 'stacked_models.xml'
detect["outds9file"]   = 'ds9_1.reg'
detect["srcmodel"]     = 'POINT'
detect["bkgmodel"]     = 'CUBE'
detect["threshold"]    = 15.0
detect["debug"]        = debug
detect.execute()
