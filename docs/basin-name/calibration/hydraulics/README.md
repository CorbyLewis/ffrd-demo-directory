# Hydraulics
## Description:
This folder includes subfolders, each corresponding to an individual model-unit containing the HEC-RAS model used for the conformance phase of modeling.

Models should include all relevant files required to simulate the model on desktop. This includes all model files associated with historic events used for calibration. Any referenced DSS files (such as observed data used as boundary conditions) should be included. Observed data linked as reference, such as rating-curves, flow and stage hydrographs, should also be included in the model. Associated land-use/cover files should also be included.

Note that terrain files are not to be stored in this directory, they are located in:
> ffrd-basin > terrain-modeling


### model-unit folder
Includes current model results for the *calibration* phase.

### archive folder
The *"archive"* folder is used to house draft and outdated model versions as updates are made. Archived models should be date stamped. Examples of an archived model unit directory name:
> model-unit_YYYYMMDD
> 
> kickapoo_20250314