# The PEP 484 type hints stub file for the QtQuick3D module.
#
# Generated by SIP 6.5.0
#
# Copyright (c) 2021 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt6.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import enum
import typing

import PyQt6.sip

from PyQt6 import QtQml
from PyQt6 import QtGui
from PyQt6 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]


class QQuick3D(PyQt6.sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QQuick3D') -> None: ...

    @staticmethod
    def idealSurfaceFormat(samples: int = ...) -> QtGui.QSurfaceFormat: ...


class QQuick3DObject(QtCore.QObject, QtQml.QQmlParserStatus):

    def __init__(self, parent: typing.Optional['QQuick3DObject'] = ...) -> None: ...

    def componentComplete(self) -> None: ...
    def classBegin(self) -> None: ...
    def stateChanged(self) -> None: ...
    def setParentItem(self, parentItem: 'QQuick3DObject') -> None: ...
    def parentItem(self) -> 'QQuick3DObject': ...
    def setState(self, state: str) -> None: ...
    def state(self) -> str: ...


class QQuick3DGeometry(QQuick3DObject):

    class PrimitiveType(enum.Enum):
        Points = ... # type: QQuick3DGeometry.PrimitiveType
        LineStrip = ... # type: QQuick3DGeometry.PrimitiveType
        Lines = ... # type: QQuick3DGeometry.PrimitiveType
        TriangleStrip = ... # type: QQuick3DGeometry.PrimitiveType
        TriangleFan = ... # type: QQuick3DGeometry.PrimitiveType
        Triangles = ... # type: QQuick3DGeometry.PrimitiveType

    class Attribute(PyQt6.sip.simplewrapper):

        class ComponentType(enum.Enum):
            U16Type = ... # type: QQuick3DGeometry.Attribute.ComponentType
            U32Type = ... # type: QQuick3DGeometry.Attribute.ComponentType
            F32Type = ... # type: QQuick3DGeometry.Attribute.ComponentType
            I32Type = ... # type: QQuick3DGeometry.Attribute.ComponentType

        class Semantic(enum.Enum):
            IndexSemantic = ... # type: QQuick3DGeometry.Attribute.Semantic
            PositionSemantic = ... # type: QQuick3DGeometry.Attribute.Semantic
            NormalSemantic = ... # type: QQuick3DGeometry.Attribute.Semantic
            TexCoordSemantic = ... # type: QQuick3DGeometry.Attribute.Semantic
            TangentSemantic = ... # type: QQuick3DGeometry.Attribute.Semantic
            BinormalSemantic = ... # type: QQuick3DGeometry.Attribute.Semantic
            JointSemantic = ... # type: QQuick3DGeometry.Attribute.Semantic
            WeightSemantic = ... # type: QQuick3DGeometry.Attribute.Semantic
            ColorSemantic = ... # type: QQuick3DGeometry.Attribute.Semantic
            TargetPositionSemantic = ... # type: QQuick3DGeometry.Attribute.Semantic
            TargetNormalSemantic = ... # type: QQuick3DGeometry.Attribute.Semantic
            TargetTangentSemantic = ... # type: QQuick3DGeometry.Attribute.Semantic
            TargetBinormalSemantic = ... # type: QQuick3DGeometry.Attribute.Semantic
            TexCoord1Semantic = ... # type: QQuick3DGeometry.Attribute.Semantic
            TexCoord0Semantic = ... # type: QQuick3DGeometry.Attribute.Semantic

        componentType = ... # type: 'QQuick3DGeometry.Attribute.ComponentType'
        offset = ... # type: int
        semantic = ... # type: 'QQuick3DGeometry.Attribute.Semantic'

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, a0: 'QQuick3DGeometry.Attribute') -> None: ...

    def __init__(self, parent: typing.Optional[QQuick3DObject] = ...) -> None: ...

    def indexData(self) -> QtCore.QByteArray: ...
    def vertexData(self) -> QtCore.QByteArray: ...
    def clear(self) -> None: ...
    @typing.overload
    def addAttribute(self, semantic: 'QQuick3DGeometry.Attribute.Semantic', offset: int, componentType: 'QQuick3DGeometry.Attribute.ComponentType') -> None: ...
    @typing.overload
    def addAttribute(self, att: 'QQuick3DGeometry.Attribute') -> None: ...
    def setPrimitiveType(self, type: 'QQuick3DGeometry.PrimitiveType') -> None: ...
    def setBounds(self, min: QtGui.QVector3D, max: QtGui.QVector3D) -> None: ...
    def setStride(self, stride: int) -> None: ...
    @typing.overload
    def setIndexData(self, data: QtCore.QByteArray) -> None: ...
    @typing.overload
    def setIndexData(self, offset: int, data: QtCore.QByteArray) -> None: ...
    @typing.overload
    def setVertexData(self, data: QtCore.QByteArray) -> None: ...
    @typing.overload
    def setVertexData(self, offset: int, data: QtCore.QByteArray) -> None: ...
    def stride(self) -> int: ...
    def boundsMax(self) -> QtGui.QVector3D: ...
    def boundsMin(self) -> QtGui.QVector3D: ...
    def primitiveType(self) -> 'QQuick3DGeometry.PrimitiveType': ...
    def attribute(self, index: int) -> 'QQuick3DGeometry.Attribute': ...
    def attributeCount(self) -> int: ...


class QQuick3DTextureData(QQuick3DObject):

    class Format(enum.Enum):
        None_ = ... # type: QQuick3DTextureData.Format
        RGBA8 = ... # type: QQuick3DTextureData.Format
        RGBA16F = ... # type: QQuick3DTextureData.Format
        RGBA32F = ... # type: QQuick3DTextureData.Format
        RGBE8 = ... # type: QQuick3DTextureData.Format
        R8 = ... # type: QQuick3DTextureData.Format
        R16 = ... # type: QQuick3DTextureData.Format
        R16F = ... # type: QQuick3DTextureData.Format
        R32F = ... # type: QQuick3DTextureData.Format
        BC1 = ... # type: QQuick3DTextureData.Format
        BC2 = ... # type: QQuick3DTextureData.Format
        BC3 = ... # type: QQuick3DTextureData.Format
        BC4 = ... # type: QQuick3DTextureData.Format
        BC5 = ... # type: QQuick3DTextureData.Format
        BC6H = ... # type: QQuick3DTextureData.Format
        BC7 = ... # type: QQuick3DTextureData.Format
        DXT1_RGBA = ... # type: QQuick3DTextureData.Format
        DXT1_RGB = ... # type: QQuick3DTextureData.Format
        DXT3_RGBA = ... # type: QQuick3DTextureData.Format
        DXT5_RGBA = ... # type: QQuick3DTextureData.Format
        ETC2_RGB8 = ... # type: QQuick3DTextureData.Format
        ETC2_RGB8A1 = ... # type: QQuick3DTextureData.Format
        ETC2_RGBA8 = ... # type: QQuick3DTextureData.Format
        ASTC_4x4 = ... # type: QQuick3DTextureData.Format
        ASTC_5x4 = ... # type: QQuick3DTextureData.Format
        ASTC_5x5 = ... # type: QQuick3DTextureData.Format
        ASTC_6x5 = ... # type: QQuick3DTextureData.Format
        ASTC_6x6 = ... # type: QQuick3DTextureData.Format
        ASTC_8x5 = ... # type: QQuick3DTextureData.Format
        ASTC_8x6 = ... # type: QQuick3DTextureData.Format
        ASTC_8x8 = ... # type: QQuick3DTextureData.Format
        ASTC_10x5 = ... # type: QQuick3DTextureData.Format
        ASTC_10x6 = ... # type: QQuick3DTextureData.Format
        ASTC_10x8 = ... # type: QQuick3DTextureData.Format
        ASTC_10x10 = ... # type: QQuick3DTextureData.Format
        ASTC_12x10 = ... # type: QQuick3DTextureData.Format
        ASTC_12x12 = ... # type: QQuick3DTextureData.Format

    def __init__(self, parent: typing.Optional[QQuick3DObject] = ...) -> None: ...

    def setHasTransparency(self, hasTransparency: bool) -> None: ...
    def hasTransparency(self) -> bool: ...
    def setFormat(self, format: 'QQuick3DTextureData.Format') -> None: ...
    def format(self) -> 'QQuick3DTextureData.Format': ...
    def setSize(self, size: QtCore.QSize) -> None: ...
    def size(self) -> QtCore.QSize: ...
    def setTextureData(self, data: QtCore.QByteArray) -> None: ...
    def textureData(self) -> QtCore.QByteArray: ...
