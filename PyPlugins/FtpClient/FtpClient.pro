# --------- PyScriptingConsole profile -------------------
# Last changed by $Author: florian $
# $Id: PythonQt.pro 35381 2006-03-16 13:05:52Z florian $
# $Source$
# --------------------------------------------------

TARGET   = PyGettingStarted
TEMPLATE = plugin

#DESTDIR = ../../lib

CONFIG += console

include(../../LibPythonQt/build/PythonQt.prf)
include(../../LibPythonQt/build/PythonQt_QtAll.prf)

QT += widgets uitools network

SOURCES += \
  $$PWD/main.cpp

RESOURCES += $$PWD/res.qrc
