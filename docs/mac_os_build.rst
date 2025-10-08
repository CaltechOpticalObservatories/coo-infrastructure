Build Setup for COO Software Employee – macOS Machine
=====================================================

System Requirements
-------------------

- **OS:** macOS Sonoma (14.x) or later  
- **Shell:** zsh (default)  
- **Python:** 3.12 (required minimum)  
- **Homebrew:** Installed and up-to-date  

Initial Setup
--------------

1. Replace ``employee`` with your actual macOS username.  
2. ``poder`` will be the facility/admin user.  
3. Replace ``mercury`` with your actual hostname.

User and Hostname Setup
=======================

Create Additional Users (Optional)
----------------------------------

If you need to create new users (requires admin privileges):

.. code-block:: bash

   # Create users
   sysadminctl -addUser employee
   sysadminctl -addUser poder

   # Add users to admin group
   dseditgroup -o edit -a employee -t user admin
   dseditgroup -o edit -a poder -t user admin

Set Hostname
------------

Change your Mac’s hostname to ``mercury``:

.. code-block:: bash

   scutil --set HostName mercury
   scutil --set LocalHostName mercury
   scutil --set ComputerName mercury
   dscacheutil -flushcache

Verify hostname:

.. code-block:: bash

   scutil --get HostName

Expected output (example):

.. code-block:: text

   mercury

Notes
-----

- On reboot, the hostname will persist.  
- You may need to re-open Terminal for changes to appear in your prompt.  

System Package Installation
---------------------------

Update Homebrew and install essential development tools:

.. code-block:: bash

   # Update and upgrade brew
   brew update && brew upgrade

   # Install Xcode Command Line Tools (if not installed)
   xcode-select --install

   # Install development dependencies
   brew install \
       openssl \
       zlib \
       bzip2 \
       readline \
       sqlite \
       wget \
       curl \
       llvm \
       xz \
       tk \
       libxml2 \
       libxmlsec1 \
       lzma \
       git \
       python@3.12 \
       boost \
       opencv \
       cfitsio \
       cmake \
       zmq \
       htop \
       vim \
       net-tools

.. note::

   ``build-essential`` and ``apt`` packages don’t exist on macOS.
   Equivalent functionality is provided by **Xcode Command Line Tools** and **Homebrew**.

KROOT Specific Packages (If Needed)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are optional packages that mimic Linux dependencies for KROOT environments:

.. code-block:: bash

   brew install \
       openconnect \
       subversion \
       cvs \
       tcl-tk \
       gfortran \
       boost \
       pandoc \
       groff \
       docutils \
       qt@5 \
       snmp \
       flex \
       bison

.. note::

   macOS combines many of these headers in
   ``/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/``.

Python 3.12 Installation
------------------------

Check your Python version:

.. code-block:: bash

   python3 --version
   # Expected: Python 3.12.x (must be < 3.13)

If Python is missing or outdated:

.. code-block:: bash

   brew install python@3.12
   brew link python@3.12 --force

Verify:

.. code-block:: bash

   which python3
   python3 --version

Python Package Installation
---------------------------

Install required Python packages using ``pip``:

.. code-block:: bash

   python3.12 -m pip install --upgrade pip
   python3.12 -m pip install numpy matplotlib pipython pyserial pandas PyQt5 cmake

Verify installation:

.. code-block:: bash

   python3.12 --version
   pip3.12 list

Optional: Virtual Environment
-----------------------------

Create and activate a virtual environment:

.. code-block:: bash

   cd ~
   python3.12 -m venv fei-venv
   source ~/local-venv/bin/activate
   pip install numpy matplotlib pipython

Deactivate later with:

.. code-block:: bash

   deactivate

Download Needed Drivers (and Software)
--------------------------------------

Download and install any required drivers or software for your hardware setup.
This may include:

- Camera drivers (e.g., AVT, Thorlabs, etc.)
- Motion controller software
- Other peripheral drivers

.. note::

   Many macOS drivers are distributed as ``.pkg`` installers.
   Follow vendor-specific instructions.

Download Tools Needed for Role-Specific Work
--------------------------------------------

Install the following utilities via Homebrew or direct download:

Other software (manual install):

- Slack  
- Zoom  
- VSCode or PyCharm  
- CameraD (if available for macOS)  
- SolidWorks (if needed, via Parallels/VM or networked Windows workstation)  
- Any other tools as required  

Done!
=====

✅ System is ready for COO software development on macOS.
