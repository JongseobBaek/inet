.. _usr:cha:usage:

Using the INET Framework
========================

.. _usr:sec:usage:installation:

Installation
------------

There are several ways to install the INET Framework:

-  Let the OMNeT++ IDE download and install it for you. This is the
   easiest way. Just accept the offer to install INET in the dialog that
   comes up when you first start the IDE, or choose *Help > Install
   Simulation Models* any time later.

-  From INET Framework web site, *http://inet.omnetpp.org*. The IDE
   always installs the last stable version compatible with your version
   of OMNeT++. If you need some other version, they are available for
   download from the web site. Installation instructions are also
   provided there.

-  From GitHub. If you have experience with *git*, clone the INET
   Framework project (``inet-framework/inet``), check out the
   revision of your choice, and follow the INSTALL file in the project
   root.

.. _usr:sec:usage:installing-inet-extensions:

Installing INET Extensions
--------------------------

If you plan to make use of INET extensions (e.g. Veins or SimuLTE),
follow the installation instructions provided with them.

In the absence of specific instructions, the following procedure usually
works:

-  First, check if the project root contains a file named
   ``.project``.

-  If it does, then the project can be imported into the IDE (use *File
   > Import > General > Existing Project* into workspace). make sure
   that the project is recognized as an OMNeT++ project (the *Project
   Properties* dialog contains a page titled *OMNeT++*), and it lists
   the INET project as dependency (check the *Project References* page
   in the *Project Properties* dialog).

-  If there is no ``.project`` file, you can create an empty OMNeT++
   project using the *New OMNeT++ Project* wizard in *File > New*, add
   the INET project as dependency using the *Project References* page in
   the *Project Properties* dialog, and copy the source files into the
   project.

.. _usr:sec:usage:getting-familiar-with-inet:

Getting Familiar with INET
--------------------------

The INET Framework builds upon OMNeT++, and uses the same concept:
modules that communicate by message passing. Hosts, routers, switches
and other network devices are represented by OMNeT++ compound modules.
These compound modules are assembled from simple modules that represent
protocols, applications, and other functional units. A network is again
an OMNeT++ compound module that contains host, router and other modules.

Modules are organized into a directory structure that roughly follows
OSI layers:

-  ``src/inet/applications/`` – traffic generators and application
   models

-  ``src/inet/transportlayer/`` – transport layer protocols

-  ``src/inet/networklayer/`` – network layer protocols and
   accessories

-  ``src/inet/linklayer/`` – link layer protocols and accessories

-  ``src/inet/physicallayer/`` – physical layer models

-  ``src/inet/routing/`` – routing protocols (internet and ad hoc)

-  ``src/inet/mobility/`` – mobility models

-  ``src/inet/power/`` – energy consumption modeling

-  ``src/inet/environment/`` – model of the physical environment

-  ``src/inet/node/`` – preassembled network node models

-  ``src/inet/visualizer/`` – visualization components (2D and 3D)

-  ``src/inet/common/`` – miscellaneous utility components

The OMNeT++ NED language uses hierarchical packages names. Packages
correspond to directories under ``src/``, so e.g. the
``src/inet/transportlayer/tcp`` directory corresponds to the
``inet.transportlayer.tcp`` NED package.

For modularity, the INET Framework has about 80 *project features*
(parts of the codebase that can be disabled as a unit) defined. Not all
project features are enabled in the default setup after installation.
You can review the list of available project features in the *Project \|
Project Features...* dialog in the IDE. If you want to know more about
project features, refer to the *OMNeT++ User Guide*.
