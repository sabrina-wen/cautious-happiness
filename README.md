# cautious-happiness
# Graphics Final Project
### Kristin Lin & Sabrina Wen, Pd. 10

Features Implemented:
 - Gouraud Shading
 - Ability to choose between either flat shading or gouraud shading using MDL commands
 
 How to Use:
 
In the MDL script, you can specify what kind of shading you want by using
`shading shade_type ` where shade_type indicates the type of shading you want to implement. There are two options:
1. ``` shading flat``` 
2. ``` shading gouraud```

NOTE: 
1. The shading MDL command MUST be called before you draw any shapes!
1. As you increase the step size for gouraud, the run time grows exponentially slower. For reference, a step size of 100 took 5 minutes to run. We recommend listening to a fun song as you wait to make things more enjoyable.
