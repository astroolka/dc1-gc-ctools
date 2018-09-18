import gammalib
import ctools
import cscripts

debug = True

obsselect = cscripts.csobsselect()
obsselect['inobs']     = '$CTADATA/obs/obs_gps_baseline.xml'
obsselect['pntselect'] = 'CIRCLE'
obsselect['coordsys']  = 'GAL'
obsselect['glon']      = 0.0
obsselect['glat']      = 0.0
obsselect['rad']       = 5.0
obsselect['tmin']      = 'NONE'
obsselect['tmax']      = 'NONE'
obsselect['outobs']    = 'obs_gps.xml'
obsselect["debug"]     = debug
obsselect.execute()

obsselect = cscripts.csobsselect()
obsselect['inobs']     = '$CTADATA/obs/obs_gc_baseline.xml'
obsselect['pntselect'] = 'CIRCLE'
obsselect['coordsys']  = 'GAL'
obsselect['glon']      = 0.0
obsselect['glat']      = 0.0
obsselect['rad']       = 5.0
obsselect['tmin']      = 'NONE'
obsselect['tmax']      = 'NONE'
obsselect['outobs']    = 'obs_gc.xml'
obsselect["debug"]     = debug
obsselect.execute()

select = ctools.ctselect()
select['inobs']   = 'obs_gps.xml'
select['ra']      = 'NONE'
select['dec']     = 'NONE'
select['rad']     = 'NONE'
select['tmin']    = 'NONE'
select['tmax']    = 'NONE'
select['emin']    = 0.1
select['emax']    = 100.0
select['outobs']  = 'obs_selected_gps.xml'
select["debug"]   = debug
select.execute()

select = ctools.ctselect()
select['inobs']   = 'obs_gc.xml'
select['ra']      = 'NONE'
select['dec']     = 'NONE'
select['rad']     = 'NONE'
select['tmin']    = 'NONE'
select['tmax']    = 'NONE'
select['emin']    = 0.1
select['emax']    = 100.0
select['outobs']  = 'obs_selected_gc.xml'
select["debug"]   = debug
select.execute()
