import grass.script as grass
from grass.script import raster as grassR
import os
import string
import glob
import re
import fnmatch
lista_arquivos=[]
LISTA=[]
LISTA2=[]  
list_patter=[]


folder_files="E:\\data_2015\\___john\\Gabi_mapeamento_2015_05_d28\\paisagens_antigas_DATA1\\rasters_serapados_bufer_vazio_e_clip"
for file in os.listdir(folder_files):
        if fnmatch.fnmatch(file, '*.tif'):
                lista_arquivos.append(file)
                

                 
os.chdir(folder_files)
for i in lista_arquivos:
        out=i.replace('.tif','')
        list_patter.append(out)
        grass.run_command('r.in.gdal',input=i,out=out,overwrite=True,flags="o")
    
    
    
        


