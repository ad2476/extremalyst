Extremalyst (Extrema Analyst)
===========

Find local extrema of surfaces in 3-space using gradient ascent/descent.

Note: If you encounter a bug or any unexpected behaviour, please raise an issue so that it may be addressed.

### Installation Guide:
Clone the git repo, run with `python main.py`.
###### Mac OS X:
1. Download and uncompress zip to desktop folder. Open Terminal.
2. Enter `cd ~/Desktop`, followed by `ls`. If you see `main.py` then skip step 3.
3. If not, `cd extremalyst-master`.
4. Finally, `'python main.py`.

###### Windows:
1. Download and install [Python 2.7.6](http://python.org/download/releases/2.7.6/).
2. Download zip and unzip to some folder. Navigate to that folder.
3. Open `main.py`. This should open with Python.

###### Linux:
Assuming git is installed: `git clone https://github.com/ad2476/extremalyst.git` `cd extremalyst` `python main.py`

### Basic Usage:
* (Optional) Enter the equation of the surface `F(x,y)` which you wish to analyse.
  * To skip this step, enter `pass` instead. Any evaluations of F(x,y) will not be correct, however.
* Enter a gradient vector in the form `<Fx, Fy>` when prompted. Next, enter a theta-pair in the form `(theta1, theta2)`.
  * For those unfamiliar with terminology, the theta-pair is just an initial starting point in the xy domain plane.
* The CAS supports implied multiplication of coefficients (i.e. '2x', 'xy', '2[1+x]', '[1+x]2' etc.).
* Important: Do not use parentheses within the actual equations. Rather, use brackets instead.
* Type `quit` when prompted for `F(x,y)` to cancel and exit the program.

![alt text](https://raw.github.com/ad2476/extremalyst/master/img/ex1.png "Example 1")

### Features:
* Mostly working basic CAS (computer algebra system).
* Parses gradient vector passed in component notation `<Fx, Fy>`, theta-pair in coordinate notation `(theta1, theta2)`.
* Converts into RPN and can evaluate the resultant RPN expression.
* Uses gradient descent to calculate a local minimum, and gradient ascent to calculate a maximum. Evaluates `F(x,y`) for the solved `theta`.

### Status:
Does not support mathematical functions or constants (e.g. `ln(x)`, `sin(x)`, `e`, `pi`, etc). 

###### Tests of algorithm convergence
* Gradient descent converges on the correct minimum for upward-facing surfaces (`alpha=0.01`, 10000 iterations).
  * Tested: Circular/elliptical paraboloids in the form: `F(x,y)=a(x-h)^2 + b(y-k)^2 + c`.
  * NOTE: It appears gradient descent/ascent will not converge on saddle points. `theta1` will converge in one direction, while `theta2` will converge in the other. (Direction meaning ascent or descent).
* Gradient ascent converges on the correct minimum for downward-facing surfaces (`alpha=0.01`, 10000 iterations).

### Planned Features:
* Calculate all absolute extrema over a rectangular bounded region.
* Add support for `e` and `pi`.
* Add support for `sqrt(x)`, `ln(x)`, `sin(x)`, `cos(x)`, `tan(x)`.
