#!/usr/bin/env python

# To install the package to a directory other than site-packages, use:
#
#     python setup.py install --install-platlib <path>

def configuration(parent_package='',top_path=None):

	# Create a package configuration instance named "example".
	from numpy.distutils.misc_util import Configuration
	config = Configuration('drxn', parent_package, top_path)

	config.add_extension('fisher_coinc', ['fisher_coinc.pyf', 'fisher_coinc.f'])

	return config

# The following "boilerplate" actually executes the setup command,
# using as its input a Python dictionary created by the configuration
# object created by the function above.
if __name__ == "__main__":
	from numpy.distutils.core import setup
	setup(version='0.1',
          description='drxn - Directional inference',
          author='Tom Loredo',
          author_email = 'loredo@astro.cornell.edu',
          license = 'SciPy License (BSD Style)',
          #py_modules = ['adapt'],
          **configuration(top_path='').todict())
