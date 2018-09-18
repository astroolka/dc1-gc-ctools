import gammalib
import ctools
import cscripts

debug = True

select = cscripts.csmodelselect()
select['inobs']    = 'obs_selected.xml'
select['inmodel']  = 'catalog_gps_20180124.xml'
select['outmodel'] = 'cat_selected.xml'
select['roilimit'] = 5.0
select['tslimit']  = 25.0
select["debug"]    = debug
select.execute()

merge = cscripts.csmodelmerge()
merge["inmodels"]  = 'cat_selected.xml bkgcube.xml'
merge["outmodel"]  = 'models_cat.xml'
merge["debug"]     = debug
merge.execute()
