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
 
import numpy as np
# Import the mathematical libraries

from CustomLib.Funcs import (Get_File, Reshape_3D,
                             Plot, XLSX_Write_Data,
                             Round_to_Sig_Fig,
                             Write_Data_2_Text)
#Import custom functions required


class BoxUpClass:
    """Class for multiple spectra to sort lumerical data"""
    
    def __init__(self):
        """Initialise require attributes"""
        self.Data = []
        self.FileName = []
        self.File = Get_File();


    def Import_Data(self):
        """Point Cloud Data"""

        Data=np.genfromtxt(self.File, delimiter = '\t'); 
        self.Data = Data*1E9


    def Reshape_Data(self):
        
        self.XX, self.YY, self.ZZ = Reshape_3D(self.Data)

    def Plot_Data(self):
        
        Plot(self.XX, self.YY, self.ZZ)

    def Create_Bottom_Plane(self):
        
        self.m_X = len(self.XX[0,:])
        
        self.n_Y = len(self.YY[:,0])
        
        self.Floor_Level = Round_to_Sig_Fig(np.min(self.ZZ), 1)
        self.Floor_Level -= abs(2.0*self.Floor_Level) 
        
        Z_Floor = np.full((self.n_Y, self.m_X), self.Floor_Level)
        
        
        
        self.Floor_Data = np.stack([self.XX.ravel(), self.YY.ravel(), Z_Floor.ravel()], axis=1)
        
    def compute_Side_Panel_Coords(self):
        X_spacing = abs(self.XX[0,0]-self.XX[0,-1])/(len(self.XX[0,:]-1))
        
        i=0

        for j in range(len(self.XX[0,:])):
            self.Compute_Lines(X_spacing, i, j)

        for i in range(1,len(self.YY[:,0])):
            self.Compute_Lines(X_spacing, i, j)

        for j in range(j-1,-1,-1):
            self.Compute_Lines(X_spacing, i, j)

        for i in range(i-1,0,-1):
            self.Compute_Lines(X_spacing, i, j)


        
        
    def Compute_Lines(self, X_spacing, i, j):
        Z_num = int(round(abs(self.ZZ[i,j]-self.Floor_Level)/X_spacing))
        
        Z_line = np.linspace(self.Floor_Level, self.ZZ[i,j], Z_num)
        X_line = np.full(len(Z_line), self.XX[i,j])
        Y_line = np.full(len(Z_line), self.YY[i,j])
        Matrix_T = np.array([X_line, Y_line, Z_line])
        Matrix=Matrix_T.T
        Matrix = np.delete(Matrix, 0, 0)
        Matrix = np.delete(Matrix, -1, 0)
        self.All_Data = np.concatenate((self.All_Data, Matrix), axis=0)


        

        
    def catonate_XYZ_Cols(self):
        
        self.All_Data = np.concatenate((self.Data, self.Floor_Data), axis=0)
        
        
    def Write_Columns_2_Text(self):
        
        Textpath = self.File
        Textpath = Textpath.replace('.txt', '_new_Text_File.txt')
        
        Write_Data_2_Text(self.All_Data, Textpath)

        
    def Write_New_Files(self):
        """Write the data to excel files in the format to save as txt and import to Lumerical"""
        Excelpath = self.File
        Excelpath = Excelpath.replace('.txt', '_EXCEL.xlsx')

        
        XLSX_Write_Data(Excelpath, self.XX,self.YY,self.ZZ)
