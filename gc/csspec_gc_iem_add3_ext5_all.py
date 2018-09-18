import gammalib
import ctools
import cscripts

debug = True

butterfly = ctools.ctbutterfly()
butterfly['inobs']    = 'cntcube.fits'
butterfly['inmodel']  = 'stacked_results_iem_add3_ext5.xml'
butterfly['srcname']  = 'Src001'
butterfly['expcube']  = 'expcube.fits'
butterfly['psfcube']  = 'psfcube.fits'
butterfly['bkgcube']  = 'bkgcube.fits'
butterfly['outfile']  = 'butterfly_iem_add3_ext5.txt'
butterfly['emin']     = 0.1
butterfly['emax']     = 100.0
butterfly['debug']    = debug
butterfly.execute()

spec = cscripts.csspec()
spec['inobs']      = 'cntcube.fits'
spec['inmodel']    = 'stacked_results_iem_add3_ext5.xml'
spec['srcname']    = 'Src001'
spec['expcube']    = 'expcube.fits'
spec['psfcube']    = 'psfcube.fits'
spec['bkgcube']    = 'bkgcube.fits'
spec['outfile']    = 'spectrum_gc_iem_add3_ext5.fits'
spec['method']     = 'AUTO'
spec['ebinalg']    = 'LOG'
spec['emin']       = 0.1
spec['emax']       = 100.0
spec['enumbins']   = 30
spec['debug']      = debug
spec.execute()
