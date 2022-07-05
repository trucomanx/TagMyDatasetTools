#!/usr/bin/python

import os
import sys
import shutil

import pandas as pd

def read_csv_file_and_move_by_type(csvpath,pathin,filenameout="filename"):
    '''
    Lee el archiv CSV en csvpath y lee los archivos relativos (agregando pathin) 
    y su categoria, y ordena los archivos en directorios con el nombre de la categoria 
    
    :param csvpath: El path completo del archivo CSV a leer.
    :type csvpath: str 
    :param pathin: Este directorio será agregado a cada file en el archiv CSV.
    :type pathin: str 
    :param filenameout: Prename de los archivos nuevos y ordenado en cada directorio
    :type filenameout: str 
    :return: True si todo fue bien o False si no.
    :rtype: bool
    '''
    if(os.path.exists(csvpath)==False):
        return False;
        
    df = pd.read_csv(csvpath, header=None)
    
    L=df.shape[0];
    
    if(L==0):
        return;
    
    ID=dict({});
    for n in range(L):
        ID[df[1][n]]=1;
        
    for n in range(L):
        fileimg=os.path.join(pathin,df[0][n]);
        if(os.path.exists(fileimg)):
            dirout=os.path.join(pathin,df[1][n]);
            try: 
                os.mkdir(dirout) 
            except: 
                pass
            
            shutil.move(fileimg,os.path.join(dirout,filenameout+str(ID[df[1][n]])+".png"));
            ID[df[1][n]]=ID[df[1][n]]+1;
    return True;


