import gammalib
import ctools
import cscripts

debug = True

like = ctools.ctlike()
like['inobs']    = 'cntcube.fits'
like['expcube']  = 'expcube.fits'
like['psfcube']  = 'psfcube.fits'
like['bkgcube']  = 'bkgcube.fits'
like['inmodel']  = 'stacked_models_iem_add1.xml'
like['outmodel'] = 'stacked_results_iem_add1.xml'
like["debug"]    = debug
like.execute()

resmap = cscripts.csresmap()
resmap['inobs']      = 'cntcube.fits'
resmap['expcube']    = 'expcube.fits'
resmap['psfcube']    = 'psfcube.fits'
resmap['bkgcube']    = 'bkgcube.fits'
resmap['inmodel']    = 'stacked_results_iem_add1.xml'
resmap['modcube']    = 'NONE'
resmap['outmap']     = 'resmap_iem_add1.fits'
resmap['algorithm']  = 'SIGNIFICANCE'
resmap["debug"]      = debug
resmap.execute()
