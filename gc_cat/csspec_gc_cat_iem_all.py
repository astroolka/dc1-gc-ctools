import gammalib
import ctools
import cscripts

debug = True

butterfly = ctools.ctbutterfly()
butterfly['inobs']    = 'cntcube.fits'
butterfly['inmodel']  = 'results_cat_iem.xml'
butterfly['srcname']  = 'CTA J1745-2900'
butterfly['expcube']  = 'expcube.fits'
butterfly['psfcube']  = 'psfcube.fits'
butterfly['bkgcube']  = 'bkgcube.fits'
butterfly['outfile']  = 'butterfly_cat_iem.txt'
butterfly['emin']     = 0.1
butterfly['emax']     = 100.0
butterfly['debug']    = debug
butterfly.execute()

spec = cscripts.csspec()
spec['inobs']      = 'cntcube.fits'
spec['inmodel']    = 'results_cat_iem.xml'
spec['srcname']    = 'CTA J1745-2900'
spec['expcube']    = 'expcube.fits'
spec['psfcube']    = 'psfcube.fits'
spec['bkgcube']    = 'bkgcube.fits'
spec['outfile']    = 'spectrum_gc_cat_iem_all.fits'
spec['method']     = 'AUTO'
spec['ebinalg']    = 'LOG'
spec['emin']       = 0.1
spec['emax']       = 100.0
spec['enumbins']   = 30
spec['debug']      = debug
spec.execute()
