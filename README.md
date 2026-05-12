# Master thesis GEO5960 - 2025/2026
**Author: Kjersti Stangeland**
Contact: kjesta@uio.no

Here lies the scripts for processing lab data, both acoustic probe data and PIV data, for my thesis.
Both processing scripts and analyis is provided.

*Overview*

* `words_written.ipynb`: Manual tracking of my word count in Overleaf, for fun.
* `extending_weber2025.pdf`: Hand written notes extending the theory of Weber (2025) by including inertia in his Hele-Shaw formulation.
* `/Reanalysis_of_Maxime/`: Initial scripts for analyzing the labdata of Maxime Leclerc. His data served as a starting point for finding the relevant wave parameters to run in my experimental campaign. Here, I tried to replicate his results and make my own versions of his scripts. None of the scripts in this folder contirbutes directly to my own thesis.
* `/Lab/processing_funcs.py`: Functions for pre-processing acoustic probe data.
* `/Lab/post_processing.ipynb`: Examples on pre-processing. 
* `/Lab/funcs.py`: Functions for estimating wavenumber and cutting off data which contain wave ramp-up and reflections.
* `/Lab/BL_thickness.ipynb`: Reporting the Stokes boundary layer thickness of the waves ran.
* `/Lab/analysis_funcs.py`: Functions for finding the individual peaks of waves, mean amplitude, observed damping coefficient, and theoretical quantities from Weber (2025).
* `/Lab/Results/`: Notebooks where all probe experiments are processed.
* `/Lab/Probe_analysis/`: Analysis of the processed probe data.
* `/Lab/PIV/plate_top_rectangular_IR/`: Notebooks where PIV analysis is done.
* `/Lab/PIV/flow_field_comparison.ipynb`: Plotting velocity fields for comparison.
* `/Lab/PIV/vertical_velocity.ipynb`: Analysis of the vertical velocity obtained from PIV to the theoretical values.

Weber, J. E. H. (2025). Surface wave damping by a Robin boundary condition at a permeable seabed. European Journal of Mechanics - B/Fluids, 109, 243–252. https://doi.org/10.1016/j.euromechflu.2024.10.010
