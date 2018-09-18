import gammalib
import ctools
import cscripts

debug = True

edispcube = ctools.ctedispcube()
edispcube['inobs']    = 'obs_selected.xml'
edispcube['incube']   = 'NONE'
edispcube['ebinalg']  = 'LOG'
edispcube['emin']     = 0.1
edispcube['emax']     = 100.0
edispcube['enumbins'] = 30
edispcube['nxpix']    = 14
edispcube['nypix']    = 14
edispcube['binsz']    = 1.0
edispcube['coordsys'] = 'GAL'
edispcube['proj']     = 'CAR'
edispcube['xref']     = 0.0
edispcube['yref']     = 0.0
edispcube['outcube']  = 'edispcube_1.4.3.fits'
edispcube["debug"]    = debug
edispcube.execute()
