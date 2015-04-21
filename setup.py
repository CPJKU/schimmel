#!/usr/bin/env python
# encoding: utf-8
"""
@author: Sebastian Böck <sebastian.boeck@jku.at>

"""

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy as np

extensions = [Extension('schimmel',
                        ['hmm.pyx'],
                        include_dirs=[np.get_include()],
                        extra_compile_args=['-fopenmp'],
                        extra_link_args=['-fopenmp'])]

classifiers = ['Development Status :: 3 - Alpha',
               'Programming Language :: Python :: 2.7',
               'License :: OSI Approved :: BSD License']

setup(name='schimmel',
      version='0.1',
      description='Simple Cython Hidden Markov Model Extension Library',
      long_description=open('README.md').read(),
      author='Sebastian Böck, Department of Computational Perception, '
             'Johannes Kepler University, Linz, Austria',
      author_email='sebastian.boeck@jku.at',
      url='https://github.com/CPJKU/schimmel',
      license='BSD',
      ext_modules=extensions,
      cmdclass={'build_ext': build_ext},
      classifiers=classifiers)

