include(../../LibPythonQt/build/PythonQt.prf)
include(../../Libs/LibPythonQt/build/PythonQt_QtAll.prf)

QT += widgets uitools network

SOURCES += \
  $$PWD/main.cpp

RESOURCES += $$PWD/res.qrc
