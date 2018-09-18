import gammalib
import ctools
import cscripts

debug = True

like = ctools.ctlike()
like['inobs']    = 'cntcube.fits'
like['expcube']  = 'expcube.fits'
like['psfcube']  = 'psfcube.fits'
like['bkgcube']  = 'bkgcube.fits'
like['inmodel']  = 'stacked_models.xml'
like['outmodel'] = 'stacked_results.xml'
like["debug"]    = debug
like.execute()

resmap = cscripts.csresmap()
resmap['inobs']      = 'cntcube.fits'
resmap['expcube']    = 'expcube.fits'
resmap['psfcube']    = 'psfcube.fits'
resmap['bkgcube']    = 'bkgcube.fits'
resmap['inmodel']    = 'stacked_results.xml'
resmap['modcube']    = 'NONE'
resmap['outmap']     = 'resmap.fits'
resmap['algorithm']  = 'SIGNIFICANCE'
resmap["debug"]      = debug
resmap.execute()
