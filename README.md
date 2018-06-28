## CPPN-Art-Sandbox
### Compositional pattern-producing networks based abstract art generator
Based on "Compositional Pattern Producing Networks: A Novel Abstraction of Development", Kenneth O.Stanley


### Example image

<img src="https://github.com/audeberc/CPPN-Art-Sandbox/blob/master/illustrations/ex1.jpg" width="400" height="400" />
<img src="https://github.com/audeberc/CPPN-Art-Sandbox/blob/master/illustrations/ex2.jpg" width="400" height="400" />
<img src="https://github.com/audeberc/CPPN-Art-Sandbox/blob/master/illustrations/ex3.jpg" width="400" height="400" />

### Example animation

[Animated example!](https://gfycat.com/PettyImportantBlueshark)


## requirements
-python3
-tensorflow
-keras
-opencv 
-numpy
-pyQt5

## Manual
Launch the GUI using:
```
python3 main.py
```
<img src="https://github.com/audeberc/CPPN-Art-Sandbox/blob/master/illustrations/gui.png"/>

##### Image settings
Click image settings to set the preview window resolution & final render resolution

##### Random SEED
Click RND to generate a new random seed, you can enter your own seed in the rightmost window

##### Coordinates settings

CCPN works by using a neural network to define a function F(X,Y,Z,A) = Pixel Value 
with 
* X function mapped to the x-coordinate in the image
* Y function mapped to the y-coordinate in the image
* Z a distance function of the x/y coordinates (by default the distance from the center sqrt(x^2+y^2)
* A an extra parameter to animate through the latent space 

You can use the 3 first windows to define three functions depending respectively of 
* x
* y
* x, y
Entering "x ** 2" and "y ** 2" will for example yield a symmetrical image through F(x** 2, y** 2, Z, A)

You can enter a fixed value of A or generate a sequence of images exploring different values of A by clicking the ANIM button.

##### Variance
Sets the variance of the neural network initialisation, higher values will usually generate more complex and unlinear results 

##### Network architecture definition
A list describing the neural network achitecture. You can add layers by clicking the "Add Layer button" and remove the last layer by double clicking it. You can also modify the activation function and number of units in each dense layer.


##### Render & preview
The preview button renders the image at a low resolution (64x64 by default), allowing a quick settings of the coordinates and achitecture. The full resolution image can then be rendered and exported using the corresponding buttons.

related gits:
https://github.com/hardmaru/cppn-tensorflow

http://blog.otoro.net/2016/03/25/generating-abstract-patterns-with-tensorflow/
