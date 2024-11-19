# Installing python and its packages lib and pyqt modules

# installing python 3.11 packege 
Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.11.6/python-3.11.6-amd64.exe -OutFile python_installer.exe

# Processing python 3 package
Start-Process -FilePath .\python_installer.exe -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait

# Installing python 3.11  from store 


# Install pip (Python's package installer) if not already installed
python -m ensurepip --upgrade

# Upgrade pip to the latest version
python -m pip install --upgrade pip

# Install PyQt5 and related packages for GUI development
pip install pyqt5

#all package are started


python3 "D:\qtpython\app.py"