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

from CustomLib.Classes import BoxUpClass as BUC
# Import the custom class for sorting the spectrum

if __name__ == '__main__':
    """instantiate objects and process""" 
    num_res = 500
    BUC_Obj = BUC()
    BUC_Obj.Import_Data()
    BUC_Obj.Reshape_Data()
    BUC_Obj.Plot_Data()
    BUC_Obj.Create_Bottom_Plane()
    BUC_Obj.Write_New_Files()
    BUC_Obj.catonate_XYZ_Cols()
    BUC_Obj.compute_Side_Panel_Coords()
    BUC_Obj.Write_Columns_2_Text()
