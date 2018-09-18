import gammalib
import ctools
import cscripts

debug = True

binning = ctools.ctbin()
binning['inobs']    = 'obs_selected.xml'
binning['xref']     = 0.0
binning['yref']     = 0.0
binning['coordsys'] = 'GAL'
binning['proj']     = 'CAR'
binning['binsz']    = 0.02
binning['nxpix']    = 500
binning['nypix']    = 500
binning['ebinalg']  = 'LOG'
binning['emin']     = 0.1
binning['emax']     = 100.0
binning['enumbins'] = 30
binning['outcube']  = 'cntcube.fits'
binning["debug"]    = debug
binning.execute()

expcube = ctools.ctexpcube()
expcube['inobs']   = 'obs_selected.xml'
expcube['incube']  = 'cntcube.fits'
expcube['outcube'] = 'expcube.fits'
expcube["debug"]   = debug
expcube.execute()

psfcube = ctools.ctpsfcube()
psfcube['inobs']    = 'obs_selected.xml'
psfcube['incube']   = 'NONE'
psfcube['ebinalg']  = 'LOG'
psfcube['emin']     = 0.1
psfcube['emax']     = 100.0
psfcube['enumbins'] = 30
psfcube['nxpix']    = 14
psfcube['nypix']    = 14
psfcube['binsz']    = 1.0
psfcube['coordsys'] = 'GAL'
psfcube['proj']     = 'CAR'
psfcube['xref']     = 0.0
psfcube['yref']     = 0.0
psfcube['outcube']  = 'psfcube.fits'
psfcube["debug"]    = debug
psfcube.execute()

bkgcube = ctools.ctbkgcube()
bkgcube['inobs']    = 'obs_selected.xml'
bkgcube['inmodel']  = '$CTOOLS/share/models/bkg_irf.xml'
bkgcube['incube']   = 'cntcube.fits'
bkgcube['outcube']  = 'bkgcube.fits'
bkgcube['outmodel'] = 'bkgcube.xml'
bkgcube["debug"]    = debug
bkgcube.execute()
