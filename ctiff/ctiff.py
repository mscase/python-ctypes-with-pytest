#!/usr/bin/env python3

import sys
import ctypes as C
import ctypes.util

#define from tiff.h
TIFFTAG_IMAGEWIDTH       = 256
TIFFTAG_IMAGELENGTH      = 257
TIFFTAG_SAMPLESPERPIXEL  = 277
TIFFTAG_BITSPERSAMPLE    = 258
TIFFTAG_ORIENTATION	     = 274
TIFFTAG_PLANARCONFIG     = 284
TIFFTAG_IMAGEDESCRIPTION = 270

TiffTags = {
    TIFFTAG_IMAGEWIDTH: 'TIFFTAG_IMAGEWIDTH',
    TIFFTAG_IMAGELENGTH: 'TIFFTAG_IMAGELENGTH',
    TIFFTAG_SAMPLESPERPIXEL: 'TIFFTAG_SAMPLESPERPIXEL',
    TIFFTAG_BITSPERSAMPLE: 'TIFFTAG_BITSPERSAMPLE', 
    TIFFTAG_ORIENTATION: 'TIFFTAG_ORIENTATION',
    TIFFTAG_PLANARCONFIG: 'TIFFTAG_PLANARCONFIG',
    TIFFTAG_IMAGEDESCRIPTION: 'TIFFTAG_IMAGEDESCRIPTION',
}

def GetTiffTagId(ttag):
    for (id, name) in TiffTags.items():
        if (ttag == name):
            return id
    return -1

TiffTags2 = {
    'TIFFTAG_IMAGEWIDTH': TIFFTAG_IMAGEWIDTH,
    'TIFFTAG_IMAGELENGTH': TIFFTAG_IMAGELENGTH,
    'TIFFTAG_SAMPLESPERPIXEL': TIFFTAG_SAMPLESPERPIXEL,
    'TIFFTAG_BITSPERSAMPLE': TIFFTAG_BITSPERSAMPLE, 
    'TIFFTAG_ORIENTATION': TIFFTAG_ORIENTATION,
    'TIFFTAG_PLANARCONFIG': TIFFTAG_PLANARCONFIG,
    'TIFFTAG_IMAGEDESCRIPTION': TIFFTAG_IMAGEDESCRIPTION,
}

class TIFF(C.Structure):
    pass

pTIFF = C.POINTER(TIFF)
TTAG_T = C.c_uint32


class TIFFDataType(C.c_int):
    TIFF_NOTYPE = 0
    TIFF_BYTE = 1
    TIFF_ASCII = 2
    TIFF_SHORT = 3
    TIFF_LONG = 4
    TIFF_RATIONAL = 5
    TIFF_SBYTE = 6
    TIFF_UNDEFINED = 7
    TIFF_SSHORT = 8
    TIFF_SLONG = 9
    TIFF_SRATIONAL = 10
    TIFF_FLOAT = 11
    TIFF_DOUBLE = 12
    TIFF_IFD = 13
    TIFF_LONG8 = 16
    TIFF_SLONG8 = 17
    TIFF_IFD8 = 18

TIFFDataType_dict = {
    0: 'TIFF_NOTYPE',
    1: 'TIFF_BYTE',
    2: 'TIFF_ASCII',
    3: 'TIFF_SHORT',
    4: 'TIFF_LONG',
    5: 'TIFF_RATIONAL',
    6: 'TIFF_SBYTE',
    7: 'TIFF_UNDEFINED',
    8: 'TIFF_SSHORT',
    9: 'TIFF_SLONG',
    10: 'TIFF_SRATIONAL',
    11: 'TIFF_FLOAT',
    12: 'TIFF_DOUBLE',
    13: 'TIFF_IFD',
    16: 'TIFF_LONG8',
    17: 'TIFF_SLONG8',
    18: 'TIFF_IFD8',
}

class TIFFSetGetFieldType(C.c_int):
    TIFF_SETGET_UNDEFINED = 0
    TIFF_SETGET_ASCII = 1
    TIFF_SETGET_UINT8 = 2
    TIFF_SETGET_SINT8 = 3
    TIFF_SETGET_UINT16 = 4
    TIFF_SETGET_SINT16 = 5
    TIFF_SETGET_UINT32 = 6
    TIFF_SETGET_SINT32 = 7
    TIFF_SETGET_UINT64 = 8
    TIFF_SETGET_SINT64 = 9
    TIFF_SETGET_FLOAT = 10
    TIFF_SETGET_DOUBLE = 11
    TIFF_SETGET_IFD8 = 12
    TIFF_SETGET_INT = 13
    TIFF_SETGET_UINT16_PAIR = 14
    TIFF_SETGET_C0_ASCII = 15
    TIFF_SETGET_C0_UINT8 = 16
    TIFF_SETGET_C0_SINT8 = 17
    TIFF_SETGET_C0_UINT16 = 18
    TIFF_SETGET_C0_SINT16 = 19
    TIFF_SETGET_C0_UINT32 = 20
    TIFF_SETGET_C0_SINT32 = 21
    TIFF_SETGET_C0_UINT64 = 22
    TIFF_SETGET_C0_SINT64 = 23
    TIFF_SETGET_C0_FLOAT = 24
    TIFF_SETGET_C0_DOUBLE = 25
    TIFF_SETGET_C0_IFD8 = 26
    TIFF_SETGET_C16_ASCII = 27
    TIFF_SETGET_C16_UINT8 = 28
    TIFF_SETGET_C16_SINT8 = 29
    TIFF_SETGET_C16_UINT16 = 30
    TIFF_SETGET_C16_SINT16 = 31
    TIFF_SETGET_C16_UINT32 = 32
    TIFF_SETGET_C16_SINT32 = 33
    TIFF_SETGET_C16_UINT64 = 34
    TIFF_SETGET_C16_SINT64 = 35
    TIFF_SETGET_C16_FLOAT = 36
    TIFF_SETGET_C16_DOUBLE = 37
    TIFF_SETGET_C16_IFD8 = 38
    TIFF_SETGET_C32_ASCII = 39
    TIFF_SETGET_C32_UINT8 = 40
    TIFF_SETGET_C32_SINT8 = 41
    TIFF_SETGET_C32_UINT16 = 42
    TIFF_SETGET_C32_SINT16 = 43
    TIFF_SETGET_C32_UINT32 = 44
    TIFF_SETGET_C32_SINT32 = 45
    TIFF_SETGET_C32_UINT64 = 46
    TIFF_SETGET_C32_SINT64 = 47
    TIFF_SETGET_C32_FLOAT = 48
    TIFF_SETGET_C32_DOUBLE = 49
    TIFF_SETGET_C32_IFD8 = 50
    TIFF_SETGET_OTHER = 51

# Define the TIFFFieldArray struct (assuming a simple placeholder)
class TIFFFieldArray(C.Structure):
    _fields_ = [
        # Add appropriate fields here
    ]

class TIFFField(ctypes.Structure):
    _fields_ = [
        ('field_tag', TTAG_T),
        ('field_readcount', C.c_short),
        ('field_writecount', C.c_short),
        ('field_type', TIFFDataType),
        ('reserved', C.c_uint32),
        ('set_field_type', TIFFSetGetFieldType),
        ('get_field_type', TIFFSetGetFieldType),
        ('field_bit', C.c_ushort),
        ('field_oktochange', C.c_ubyte),
        ('field_passcount', C.c_ubyte),
        ('field_name', C.c_char_p),
        ('field_subfields', C.POINTER(TIFFFieldArray))
    ]

def InitLibFunctionSignatures(lib):
    lib.TIFFOpen.argtypes = [C.c_char_p, C.c_char_p]
    lib.TIFFOpen.restype = pTIFF
    lib.TIFFClose.argtypes = [pTIFF]
    lib.TIFFClose.restype = None
    lib.TIFFGetVersion.argtypes = []
    lib.TIFFGetVersion.restype = C.c_char_p
    lib.TIFFGetField.argtypes = [pTIFF, TTAG_T, C.c_void_p]
    lib.TIFFGetField.restype = C.c_int
    # field info
    lib.TIFFFieldWithTag.argtypes = [pTIFF, TTAG_T]
    lib.TIFFFieldWithTag.restype = C.POINTER(TIFFField)
    lib.TIFFFieldName.argtypes = [C.POINTER(TIFFField)]
    lib.TIFFFieldName.restype = C.c_char_p
    lib.TIFFFieldDataType.argtypes = [C.POINTER(TIFFField)]
    lib.TIFFFieldDataType.restype = TIFFDataType

class DynamicLibrary:
    def __init__(self):
        libname = 'tiff'
        libpath = ctypes.util.find_library(libname)
        if libpath:
            print(f'Library {libname} found at {libpath}')
        else:
            print(f'Library {libname} not found')
            sys.exit(1)
        try:
            self.lib = C.cdll.LoadLibrary(libpath)
        except OSError as e:
            print(f'Error loading library: {e}')
            sys.exit(1)

        InitLibFunctionSignatures(self.lib)

    def __str__(self):
        return str(self.lib)

    __repr__ = __str__


    def TIFFOpen(self, filename, filemode):
        return self.lib.TIFFOpen(filename, filemode)

    def TIFFClose(self, tiffobj):
        return self.lib.TIFFClose(tiffobj)

    def TIFFGetVersion(self):
        return self.lib.TIFFGetVersion().decode('utf-8')

    def TIFFFieldWithTag(self, tiffobj, ttag):
        res = self.lib.TIFFFieldWithTag(tiffobj, ttag)
        if res is not None:
            try:
                if res.contents is not None:
                    return res
                else:
                    print ('res.contents is None')
            except ValueError as e:
                print(f'Exception: {e}')
                raise
        else:
            print ('TIFFFieldWithTag returned NULL')
            raise ValueError('NULL value')

    def TIFFFieldName(self, fieldobj):
        return self.lib.TIFFFieldName(fieldobj).decode('utf-8')

    def TIFFFieldDataType(self, fieldobj):
        return self.lib.TIFFFieldDataType(fieldobj).value

    def TIFFGetField(self, tiffobj, ttag):
        field_info = self.lib.TIFFFieldWithTag(tiffobj, ttag)
        data_type = self.lib.TIFFFieldDataType(field_info).value
        if data_type == TIFFDataType.TIFF_LONG:
            value = C.c_uint32()
        elif data_type == TIFFDataType.TIFF_SHORT:
            value = C.c_uint16()
        elif data_type  == TIFFDataType.TIFF_ASCII:
            value = C.c_char_p()
        else:
            raise ValueError(f'unknown data_type')
        res = self.lib.TIFFGetField(tiffobj, ttag, C.byref(value))
        if res:
            return value.value
        else:
            raise ValueError(f'Failed to get value for [{TiffTags[ttag]}]')

class ctiff:
    def __init__(self):
        self.lib = DynamicLibrary()

    def __str__(self):
        return f'{self.lib.TIFFGetVersion()}'

    def __repr__(self):
        return f'{str(self.lib)}\nversion={self.lib.TIFFGetVersion()}'
        
    def TiffOpen(self, image_file, mode):
        return self.lib.TIFFOpen(image_file, mode)

    def TiffClose(self, tiff_handle):
        return self.lib.TIFFClose(tiff_handle)
