import gammalib
import ctools
import cscripts

debug = True

like = ctools.ctlike()
like['inobs']    = 'cntcube.fits'
like['expcube']  = 'expcube.fits'
like['psfcube']  = 'psfcube.fits'
like['bkgcube']  = 'bkgcube.fits'
like['inmodel']  = 'models_cat_iem+fb+ts.xml'
like['outmodel'] = 'results_cat_iem+fb+ts.xml'
like["debug"]    = debug
like.execute()

resmap = cscripts.csresmap()
resmap['inobs']      = 'cntcube.fits'
resmap['expcube']    = 'expcube.fits'
resmap['psfcube']    = 'psfcube.fits'
resmap['bkgcube']    = 'bkgcube.fits'
resmap['inmodel']    = 'results_cat_iem+fb+ts.xml'
resmap['modcube']    = 'NONE'
resmap['outmap']     = 'resmap_cat_iem+fb+ts.fits'
resmap['algorithm']  = 'SIGNIFICANCE'
resmap["debug"]      = debug
resmap.execute()
