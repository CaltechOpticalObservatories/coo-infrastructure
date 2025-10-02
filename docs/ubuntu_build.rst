Build Setup for COO Software Employee - Linux-Machine 
=====================================================

System Requirements
-------------------

- OS: Ubuntu 24.04 LTS(Latest Version)
- Linux: Current Kernel version Linux 6.8.0 (-59 Ubuntu)
- Python: 3.12 (required-minimum)

Initial Setup
-----------------
1. replace ''employee'' with your actual username
2. poder will be the facility/admin user
3. replace ''mercury'' with your actual hostname

User and Hostname Setup
=======================

Create a development user ``employee`` and facility user ``poder``:

.. code-block:: bash

   # Create users
   sudo adduser employee
   sudo adduser poder

   # Add users to sudo group
   sudo usermod -aG sudo employee
   sudo usermod -aG sudo poder

   # Add serial access group
   sudo usermod -aG dialout employee
   sudo usermod -aG dialout poder

   # Set new hostname
   sudo hostnamectl set-hostname ''mercury''
   sudo vim /etc/hosts

In ``/etc/hosts`` (opened with ``vim``), change the line:

.. code-block:: text

   127.0.1.1   old-hostname

to:

.. code-block:: text

   127.0.1.1   ''mercury'''

Save and exit with ``:wq``.

Verify hostname:

.. code-block:: bash

   hostnamectl

Expected output (example):

.. code-block:: text

   Static hostname: ''mercury''

Notes
-----

- On reboot, the hostname will be set properly.  
- Changes with ``usermod`` require logout/login to take effect.  


System Package Installation
---------------------------

Update package list and install the essential build tools:

.. code-block:: bash

   sudo apt update
   sudo apt install -y \
       software-properties-common \
       build-essential \
       libffi-dev \
       libssl-dev \
       zlib1g-dev \
       libbz2-dev \
       libreadline-dev \
       libsqlite3-dev \
       wget \
       curl \
       llvm \
       libncursesw5-dev \
       xz-utils \
       tk-dev \
       libxml2-dev \
       libxmlsec1-dev \
       liblzma-dev \
       git \
       python3-pip \
       libboost-all-dev \
       libopencv-dev \
       libccfits-dev \
       libcfitsio-dev \
       cmake \
       libzmq3-dev \
       net-tools \
       htop
       vim \


KROOT Specific Packages(If Needed)
~~~~~~~~~~~~~~~~~~~~~~~

These packages are needed for KROOT environments:

.. code-block:: bash

   sudo apt install -y \
       openconnect \
       subversion cvs at \
       python-dev-is-python3 \
       libxt-dev libxml2-dev libncurses-dev \
       tcl tcl-dev tcl-thread tcllib tk tk-dev expect \
       tclx tcl-fitstcl libpq-dev \
       g++ gfortran \
       libboost-dev libboost-system-dev libboost-filesystem-dev \
       python3-tk python3-pil.imagetk \
       libpam-dev \
       pandoc groff rst2pdf \
       python3-dev python3-docutils \
       python3.12-venv \
       python3-ephem \
       pyqt5-dev-tools \
       make m4 autoconf \
       xorg-dev xaw3dg-dev \
       libmotif-dev \
       lib32c-dev \
       libcfitsio-dev \
       snmp \
       flex flex-doc bison bison-doc


Python 3.12 Installation
------------------------

Ubuntu 24.04 ships with Python 3.12.3. Double check version is at least 3.12.3 and not newer than 3.13.

Check version:

.. code-block:: bash

   python3 --version
   # Expected: Python 3.12.3 => must be < Python 3.13

If you need to install Python, build from source:

.. code-block:: bash

   cd /usr/src
   sudo wget https://www.python.org/ftp/python/3.12.3/Python-3.12.3.tgz
   sudo tar xzf Python-3.12.3.tgz
   cd Python-3.12.3
   sudo ./configure --enable-optimizations
   sudo make -j $(nproc)
   sudo make altinstall  # Installs as python3.12


Python Package Installation
---------------------------

Install required Python packages using pip:

.. code-block:: bash

   python3.12 -m pip install --upgrade pip
   python3.12 -m pip install numpy matplotlib pipython serial panda QT5.2 cmake

Verify installation:

.. code-block:: bash

   python3.12 --version
   pip3.12 list


Optional: Virtual Environment
-----------------------------

Create and activate a virtual environment:

.. code-block:: bash

   # Inside /home/employee
   python3.12 -m venv fei-venv
   source ~/fei-venv/bin/activate
   pip install numpy matplotlib pipython


Download Needed Drivers (and Software)
--------------------------------------

Download and install any required drivers or software for your hardware setup. This may include:
- Camera drivers
- Motion controller software
- Other peripheral drivers

Download Tools needed for title specific work
---------------------------------------------
- Git
- Slack
- Zoom
- SVN
- CVS
- At
- OpenConnect
- Other tools as needed
- IDEs (VSCode, PyCharm, etc.)
- CameraD
- SolidWorks (if needed, via Wine or VM)
- Other software as needed

Done!
=====
