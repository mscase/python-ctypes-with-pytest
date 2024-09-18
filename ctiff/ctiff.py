#!/usr/bin/env python3

import sys
import ctypes as C
import ctypes.util

#define from tiff.h
TIFFTAG_IMAGEWIDTH       = 256
TIFFTAG_IMAGELENGTH      = 257
TIFFTAG_SAMPLESPERPIXEL  = 277
TIFFTAG_BITSPERSAMPLE    = 258
TIFFTAG_ORIENTATION      = 274
TIFFTAG_PLANARCONFIG     = 284
TIFFTAG_IMAGEDESCRIPTION = 270
TIFFTAG_SOFTWARE         = 305
TIFFTAG_HOSTCOMPUTER     = 316

TiffTags = {
    TIFFTAG_IMAGEWIDTH: 'TIFFTAG_IMAGEWIDTH',
    TIFFTAG_IMAGELENGTH: 'TIFFTAG_IMAGELENGTH',
    TIFFTAG_SAMPLESPERPIXEL: 'TIFFTAG_SAMPLESPERPIXEL',
    TIFFTAG_BITSPERSAMPLE: 'TIFFTAG_BITSPERSAMPLE', 
    TIFFTAG_ORIENTATION: 'TIFFTAG_ORIENTATION',
    TIFFTAG_PLANARCONFIG: 'TIFFTAG_PLANARCONFIG',
    TIFFTAG_IMAGEDESCRIPTION: 'TIFFTAG_IMAGEDESCRIPTION',
    TIFFTAG_SOFTWARE: 'TIFFTAG_SOFTWARE',
    TIFFTAG_HOSTCOMPUTER: 'TIFFTAG_HOSTCOMPUTER',
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
    'TIFFTAG_SOFTWARE': TIFFTAG_SOFTWARE,
    'TIFFTAG_HOSTCOMPUTER': TIFFTAG_HOSTCOMPUTER,
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
    pass

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
    # field info
    lib.TIFFGetField.argtypes = [pTIFF, TTAG_T, C.c_void_p]
    lib.TIFFGetField.restype = C.c_int
    lib.TIFFSetField.argtypes = [pTIFF, TTAG_T, C.c_void_p]
    lib.TIFFSetField.restype = C.c_int
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

    def TIFFSetField(self, tiffobj, ttag, value):
        field_info = self.lib.TIFFFieldWithTag(tiffobj, ttag)
        data_type = self.lib.TIFFFieldDataType(field_info).value
        if data_type == TIFFDataType.TIFF_ASCII:
            newvalue = C.c_char_p(value.encode('utf-8'))
            try:
                res = self.lib.TIFFSetField(tiffobj, ttag, newvalue)
            except TypeError:
                raise
        else:
            raise ValueError(f'unsupported data_type')
        
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
