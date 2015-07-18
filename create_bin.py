import grass.script as grass
from grass.script import raster as grassR
import os
import string
import glob
import re
import fnmatch

#list_tot=grass.mlist_grouped ('rast', pattern='**') ['PERMANENT']
#ls_bu_vzio=[]
#ls_clip_map=[]
#for i in list_tot:
    #if "_clip2K" in i:
        #ls_clip_map.append(i)
    #else:
        #ls_bu_vzio.append(i)





#for i in ls_clip_map:
    #cont_id=0
    #for a in ls_bu_vzio:
        #if "id2__"+`cont_id` in i:
            #grass.run_command("g.region",rast=a)
            ##expressao2="Bin_id2_"+`cont_id`+"="+a+"+"+i
            #grass.run_command("r.series",input=a+","+i,out="Bin_id2_"+`cont_id`,method="sum",overwrite=True)
                      
        #cont_id=cont_id+1    
#
os.chdir(r"E:\data_2015\___john\Gabi_mapeamento_2015_05_d28\paisagens_antigas_DATA1\rasters_serapados_bufer_vazio_e_clip\Mapas_bin")
list_tot=grass.mlist_grouped ('rast', pattern='Bin_id2_*') ['PERMANENT']
for i in list_tot:
    grass.run_command("g.region",rast=i)
    grass.run_command("r.out.gdal",input=i,out=i+".tif",nodata=-9999)