Project specifications
======================================================================

Framework and general objective
_______________________________

The project aims to develop a graphical interface in PyQt that will allow to query the MusicBrainz API in order to list and save in a text file all the tracks of a searched album.\

The main steps of the project are to:

* understanding how the MusicBrainz API works;
* designing, drawing and developing the graphical interface;
* using the MVC_help Model View Controller (MVC) model to structure the application code

Development environment and GIT repository
___________________________________________


The project must :

* use the Git version management tool and a Python development IDE ;

* be structured according to the tree structure shown below
* be able to run on the Linux system of the deb11-lxqt Virtual Machine in the datacenter during the final demonstration;
* be documented :

    * project description in restructuredText format,
    * relevant comments in the code (if useful for understanding),
    * comments on the developed functions

* have a test directory where all developed Python functions will have a unit test code

The project is attached to a GIT repository that you will have created on GitHub and to the delivery of your computer codes. The repository must absolutely be handed over at the final delivery of the project. The versioning being traced and dated, it will be used for the evaluation of the work of the group and of each student.

Scripting/programming languages
_______________________________

The project must use :

    Python programming language (version > 3.9) for source codes and PyQt for GUI projects
    PHP/MySQL for web application projects
    and/or the bash scripting language for scripts allowing the automation of certain processes and the publication of results (seen in R108-Basic operating systems)

Project tree
_____________

Your project must :

    * be executed by means of a script project_name.py. This script will follow the classic program structure seen in R1.07-Programming basics and described in the Python form. It will take any parameters in arguments specified below.

    * respect the following tree structure (PROJECTGitHUB designates the directory to which your project is attached and constitutes the base of the local Git repository) :
.. figure:: _static/arborescence.png
        :align: center

        tree structure of our project

Documentation
______________
* The general project documentation should be written in restructuredText format. You can do this using the Sphinx software;

* You should add doctrinal comments at the start of the function in order to:

    #. Specify what the function does,
    #. To indicate its author, its dates of creation and last modification,
    #. Describe its parameters and, where applicable, their types,
    #. describe the limits for using parameters for proper operation of the function and exceptions that are likely to be raised,
    #. what it returns
    #. give an example of use

Unit tests
___________
Drawing inspiration from the lab on functions in the resource R1.07-Fundamentals of programming, you will have to write test code for each function developed in the project. This will be placed in a Python program in the tests directory.