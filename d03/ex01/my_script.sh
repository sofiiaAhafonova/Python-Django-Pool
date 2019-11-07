#!/bin/bash

python3 -m venv local_lib; source local_lib/bin/activate   

pip --version

pip install --log install.log --upgrade --force-reinstall  git+https://github.com/jaraco/path.py.git

python my_program.py