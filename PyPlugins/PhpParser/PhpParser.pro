# --------- PyScriptingConsole profile -------------------
# Last changed by $Author: florian $
# $Id: PythonQt.pro 35381 2006-03-16 13:05:52Z florian $
# $Source$
# --------------------------------------------------

TARGET   = PhpParser
TEMPLATE = app

#DESTDIR = ../../lib

#CONFIG += console

include(../../Libs/LibPythonQt/build/PythonQt.prf)
include(../../Libs/LibPythonQt/build/PythonQt_QtAll.prf)

QT += widgets uitools network

SOURCES +=  \
            $$PWD/main.cpp

RESOURCES += $$PWD/res.qrc
