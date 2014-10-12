
TARGET   = PythonQt_QtAll
TEMPLATE = lib

DESTDIR    = $$PWD/../../lib

include ( ../../build/common.prf )  
include ( ../../build/PythonQt.prf )  

INCLUDEPATH += $$PWD

CONFIG += qt

#dll  staticlib
DEFINES +=  PYTHONQT_QTALL_EXPORTS

contains(PYTHONQT_STATIC,1) {
    message(Building Static)
    CONFIG += staticlib
    DEFINES +=  PYTHONQT_STATIC_LIB
} else {
    message(Building DLL)
    CONFIG += dll
}


HEADERS +=                \
  $$PWD/PythonQt_QtAll.h
  
SOURCES +=                \
  $$PWD/PythonQt_QtAll.cpp

QT +=multimedia uitools gui svg sql network xml xmlpatterns opengl widgets printsupport
#webkit  webkitwidgets
include ($$PYTHONQT_GENERATED_PATH/com_trolltech_qt_core/com_trolltech_qt_core.pri)
include ($$PYTHONQT_GENERATED_PATH/com_trolltech_qt_gui/com_trolltech_qt_gui.pri)
#include ($$PYTHONQT_GENERATED_PATH/com_trolltech_qt_svg/com_trolltech_qt_svg.pri)
include ($$PYTHONQT_GENERATED_PATH/com_trolltech_qt_sql/com_trolltech_qt_sql.pri)
include ($$PYTHONQT_GENERATED_PATH/com_trolltech_qt_network/com_trolltech_qt_network.pri)
include ($$PYTHONQT_GENERATED_PATH/com_trolltech_qt_opengl/com_trolltech_qt_opengl.pri)
#include ($$PYTHONQT_GENERATED_PATH/com_trolltech_qt_webkit/com_trolltech_qt_webkit.pri)
include ($$PYTHONQT_GENERATED_PATH/com_trolltech_qt_xml/com_trolltech_qt_xml.pri)
include ($$PYTHONQT_GENERATED_PATH/com_trolltech_qt_uitools/com_trolltech_qt_uitools.pri)
