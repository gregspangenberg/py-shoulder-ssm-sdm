# py-shoulder-ssm-sdm

Python port of [Shoulder-SSM-SDM](https://github.com/pendarsm/Shoulder-SSM-SDM) written in MATLAB by [Pendar Soltanmohammadi](https://github.com/pendarsm).

This code contains Statistical Shape Models (SSMs) and Statistical Density Models (SDMs) of shoulder bones based upon 75 CT images. The statistical shape/density models descirbe an entire population and allow for practically infinite individual shape/density 3D models of the humerus or scapula to be created from the population. An array of principal component scores is used to describe how many standard deviations away you would like each prinipal component to be from the mean. A 3D model is then created in .vtk format based upon the array. This .vtk file can be viewed in [Paraview](https://www.paraview.org/) and converted to other 3D file formats for use within Finite Element Analysis.

To use this code, clone the repository and open the root folder so you can locally import sdm.py or ssm.py within a script. In example.py, an array of principal component scores is passed into sdm.humerus(), which writes the output to a .vtk file. The files within folders SDM and SSM use Git Large File Storage.


For information on how the models were developed please refer to Pendar's [paper](https://asmedigitalcollection.asme.org/biomechanical/article-abstract/142/12/121005/1084901).