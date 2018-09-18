import gammalib
import ctools
import cscripts

debug = True

like = ctools.ctlike()
like['inobs']     = 'cntcube.fits'
like['expcube']   = 'expcube.fits'
like['psfcube']   = 'psfcube.fits'
like['bkgcube']   = 'bkgcube.fits'
like['edisp']     = False
like['inmodel']   = 'stacked_results_iem_add3_ext5_fixed.xml'
like['outmodel']  = 'stacked_results_iem_add3_ext5_noedisp.xml'
like["debug"]     = debug
like.execute()

