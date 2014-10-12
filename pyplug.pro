#-------------------------------------------------
#
# Project created by QtCreator 2013-05-19T22:45:08
#
#-------------------------------------------------

QT += core gui uitools widgets

TARGET = PyPlug
TEMPLATE = app

INCLUDEPATH += LibPythonQt

DEPENDPATH += $$INCLUDEPATH

SOURCES += main.cpp

#include(LibPythonQt/build/common.prf)
include(LibPythonQt/build/PythonQt.prf)
#include(LibPythonQt/build/PythonQt_QtAll.prf)
include(PyPlugins/FtpClient/FtpClient.pri)
include(PyPlugins/PhpParser/PhpParser.pri)
