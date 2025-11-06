from __future__ import print_function
from __future__ import absolute_import

from setuptools import find_packages, setup

#####################
# required packages #
#####################
install_reqs = ['Jinja2>=3.1.0',
                'plotly>=5.18.0',
                'matplotlib>=3.7.0']

extras_require={
    'export': ['playwright>=1.40.0'],  # For PDF export
    'dev': ['pytest>=7.4.0'],
    'all': ['playwright>=1.40.0', 'pytest>=7.4.0']
}


#####################################
# Use ReadMe.md as long description #
#####################################
def readme():
    with open('README.md') as f:
        return f.read()

#################
# Setup package #
#################
setup(name='pyslides',
      version='2.0.0',
      description='Create beautiful, interactive HTML presentations with Python',
      long_description=readme(),
      long_description_content_type="text/markdown",
      author='Ahmed Tawfik',
      author_email='ahmed.tawfik@full-stack-science.com',
      packages=find_packages(),
      zip_safe=False,
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'Operating System :: Unix',
                   'Operating System :: POSIX',
                   'Operating System :: Microsoft :: Windows',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   'Programming Language :: Python :: Implementation :: CPython',
                   'Programming Language :: Python :: Implementation :: PyPy'],
      python_requires='>=3.6',
      install_requires=install_reqs,
      extras_require=extras_require,
      include_package_data=True,
      package_data={'': ['data/base.html']})
