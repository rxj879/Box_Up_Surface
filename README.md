# Box_Up_Surface
Manipulates XYZ surface data and exports an Excel file in the format for importing to Lumerical and, also, creates a box enclosure under surface XYZ data (e.g. AFM data) to Mesh an enclosed solid to modify features in CAD so that one can export a part in STL format for Lumerical

This script allows one to import XYZ column data from a scanning probe miscroscope (e.g. AFM)
in a text file and process it to the layout required for type 1 data Lumerical surface import tool data: 
https://support.lumerical.com/hc/en-us/articles/360034901973-Surface-import-Simulation-object

Note that the data is scaled to units of nm

If you need to make modifications to the surface features, the program, in addition, creates a 
closed box of cloud data points in XYZ colum data which is written
to a new text file such that one can make an enclosed solid from meshing the XYZ data:

First, I used MeshLab to create a Mesh from the boxed up XYZ surface data as per this video guide:

https://www.youtube.com/watch?v=uJRYEbO1YmA

I exported the Mesh as an "Alias Wavefront Object" .Obj file format

Then I imported the .Obj mesh into Fusion 360 and followed this guide to make it solid:

https://www.youtube.com/watch?v=tVGtG-UjlYg

---------------------
