Overview
========
It displays the usage of about how to create a wheel file ie *.whl for distribution of python modules.

Make sure you have the latest versions of setuptools and wheel installed:
=====
	pip install --user --upgrade setuptools wheel

Now run this command from the same directory where setup.py is located:
=====
	setup.py sdist bdist_wheel
	
How to install from locally after generating
=========
	pip install some-package.whl