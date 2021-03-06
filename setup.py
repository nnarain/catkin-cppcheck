from __future__ import print_function

import os
import shlex
import subprocess
from setuptools import setup

root = os.path.dirname(os.path.realpath(__file__))

# Long description from README
readme = os.path.join(root, 'README.rst')

# Read latest git tag
try:
    latest_tag = subprocess.check_output(shlex.split('git describe --tags --abbrev=0'), cwd=root)
except Exception as e:
    print('Error getting latest git tag. {}'.format(str(e)))
    exit(1)

setup(
    name='catkin-cppcheck',
    version=latest_tag,
    author='Natesh Narain',
    author_email='nnaraindev@gmail.com',
    description='Run cppcheck on catkin packages',
    long_description=open(readme).read(),
    license='MIT',
    keywords='catkin ros cppcheck c++',

    package_dir={'': 'src'},
    packages=['catkin_cppcheck'],

    install_requires=['catkin-pkg'],

    entry_points= {
        'catkin_tools.commands.catkin.verbs': [
            'cppcheck = catkin_cppcheck.main:description'
        ]
    }
)
