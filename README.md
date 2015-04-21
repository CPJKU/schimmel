schimmel
========

**S**imple **C**ython **Hi**dden **M**arkov **M**odel **e**xtension **l**ibrary

This repo contains a single Cython HMM implementation, which is optimised for
speed and parallel execution of the Viterbi algorithm.

Installation:
-------------

To enable multi-threading support, you need a compiler which supports the
`OpenMP` specifications. More recent versions of `gcc` do so. On systems with
other default compilers, set your `$CC` variable accordingly, e.g.
`export CC=gcc`.

To use this package without installing it, you need to build the extension:

```
$ python setup.py build_ext --inplace
```

To build and install it, do:

```
$ python setup.py build
$ python setup.py install
```

You need higher privileges (use `su` or `sudo`) to install the files to a
common place like `/usr/local` or similar. Alternatively you can install the
package locally by setting the appropriate switch:

```
$ python setup.py install --user
```

Requirements:
-------------
* Python 2.7
* Cython
* Numpy
* Scipy

ToDo:
-----
- [ ] add examples
- [ ] add forward, backward and Baum–Welch algorithms
