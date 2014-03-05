extremalyst
===========

Find local extrema of surfaces in 3-space using gradient ascent/descent.

Clone the git repo, run with `python main.py`. For help with this, see below.

### Basic Usage:
* Enter a gradient vector in the form \<Fx, Fy\> when prompted. Next, enter a theta-pair in the form (theta1, theta2)
  * For those unfamiliar with terminology, the theta-pair is just an initial starting point in the xy domain plane.
* The CAS supports implied multiplication of coefficients (i.e. '2x', 'xy', '2[1+x]', '[1+x]2' etc.)
* Important: Do not use parentheses within the actual equations. Rather, use brackets instead.
* Type 'quit' when prompted for gradient vector to cancel and exit the program

### Current Status:
* Mostly working basic CAS (computer algebra system)
* Parses gradient vector passed in component notation <Fx, Fy>, theta-pair in coordinate notation (theta1, theta2)
* Converts into RPN, substitutes theta-pair and evaluates the RPN equation
* TODO: Implement gradient descent!

### Installation Guide:
###### Mac OS X:
1. Download and uncompress zip to desktop folder. Open Terminal.
2. Enter `cd ~/Desktop`, followed by `ls`. If you see `main.py` then skip step 3.
3. If not, `cd extremalyst-master`.
4. Finally, `'python main.py`

###### Windows:
1. Download and install [Python 2.7.6](http://python.org/download/releases/2.7.6/)
2. Download zip and unzip to some folder. Navigate to that folder.
3. Open `main.py`. This should open with Python.

###### Linux:
You know what you're doing. If not, RTFM.

### Planned Features:
* Calculate all absolute extrema over a rectangular bounded region
