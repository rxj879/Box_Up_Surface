# -*- coding: utf-8 -*-
"""
   Copyright 2020 DR ROBIN RAFFE PRYCE JONES
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
from tkinter import filedialog as fd
from tkinter import Tk

import math
# Import ask save / open file and directory dialogue box library

import numpy as np

import matplotlib.pyplot as plt

# import xlsxwriter module
import xlsxwriter


def Write_Data_2_Text(All_Data, Textpath):

    np.savetxt(Textpath, All_Data, delimiter='\t')

def Get_File (Idir = None):
    "This uses tkinter to ask for the directory where the data is in text files"
    root = Tk();
    root.file = fd.askopenfilename(initialdir = Idir, title = "Select file");
    root.withdraw();
    return root.file;

# I'm fairly sure there's a more efficient way of doing this...
def get_z(mat, x, y):
    ind = (mat[:,(0,1)] == (x,y)).all(axis=1)
    row = mat[ind,:]
    return row[0,2]


def Reshape_3D(mat):
    x = np.unique(mat[:,0])
    y = np.unique(mat[:,1])
    X,Y = np.meshgrid(x, y)



    z = np.array([get_z(mat,x,y) for (x,y) in zip(np.ravel(X), np.ravel(Y))])
    Z = z.reshape(X.shape)
    return X,Y,Z

def Plot(X,Y,Z):
    plt.pcolormesh(X,Y,Z)
    plt.xlim(min(X[0,:]), max(X[0,:]))
    plt.ylim(min(Y[:,0]), max(Y[:,0]))
    plt.show()
    
def XLSX_Write_Data(Path, X,Y,Z):
    
    workbook = xlsxwriter.Workbook(Path)
    worksheet = workbook.add_worksheet()
 
    worksheet.write('A1', 0)
    worksheet.write('B1', len(X[0,:]))
    worksheet.write('C1', len(Y[:,0]))
    #######
    row = 1
    column = 1
    for X_item in X[0,:]:
        worksheet.write(row, column,  X_item)
        column += 1
    #######
    row = 2
    column = 0
    for Y_item in Y[:,0]:
        worksheet.write(row, column,  Y_item)
        row += 1
    #######
    row = 2
    column = 1
    z_row = 0
    for Z_item in Z[:,0]:
        for Z_item in Z[z_row,:]:
            worksheet.write(row, column,  Z_item)
            column += 1
        column = 1
        z_row += 1
        row += 1
    
    workbook.close()

# def Join_Lines(TopZ,BottomZ,grandularity):
#     Z_down = []
#     for X_top in TopZ[0,:]:
        

def Round_to_Sig_Fig(number, SigFigs):

    rounded_number = round(number, SigFigs - int(math.floor(math.log10(abs(number)))) - 1)
    return rounded_number;