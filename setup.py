try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='impactEffects',
      use_scm_version=True,
      setup_requires=['setuptools_scm'],
      description="Environment for MPM assessment 3.",
      long_description="Environment for MPM assessement 3.",
      url="https://github.com/acse-dx121/impact-effects.git",
      author="Imperial College London",
      author_email='rhodri.nelson@imperial.ac.uk',
      packages=['impactEffects'])

with open("README.md", "r") as fh:
  long_description = fh.read()

# import setuptools

# setuptools.setup(
#   name="impactffects",
#   version="0.0.1",
#   author="Daniel Xing",
#   author_email="dx121@ic.ac.uk",
#   description="A small example package",
#   long_description=long_description,
#   long_description_content_type="text/markdown",
#   url="https://github.com/acse-dx121/impact-effects.git",
#   classifiers=[
#   "Programming Language :: Python :: 3",
#   "License :: OSI Approved :: MIT License",
#   "Operating System :: OS Independent",
#   ],
#   packages=['src'],
# )


