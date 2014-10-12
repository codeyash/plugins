# --------- PythonQt profile -------------------
# Last changed by $Author: florian $
# $Id: PythonQt.pro 35381 2006-03-16 13:05:52Z florian $
# $Source$
# --------------------------------------------------

TARGET   = PythonQt
TEMPLATE = lib


DESTDIR    = $$PWD/../lib

CONFIG += qt
CONFIG -= flat



contains(PYTHONQT_STATIC,1) {
    message(Building Static)
    CONFIG += staticlib
    DEFINES +=  PYTHONQT_STATIC_LIB
} else {
    message(Building DLL)
    CONFIG += dll
}
contains(QT_MAJOR_VERSION, 5) {
  QT += widgets
}

INCLUDEPATH += $$PWD

include ( ../build/common.prf )  
include ( ../build/python.prf )

include ( src.pri )  

include($${PYTHONQT_GENERATED_PATH}/com_trolltech_qt_core_builtin/com_trolltech_qt_core_builtin.pri)
include($${PYTHONQT_GENERATED_PATH}/com_trolltech_qt_gui_builtin/com_trolltech_qt_gui_builtin.pri)
