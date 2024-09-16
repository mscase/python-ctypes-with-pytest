#!/usr/bin/env python3

from ctiff.ctiff import *
from ctiff.easytif import *

TIF = ctiff()
print(TIF)

htiff = TIF.TiffOpen(b'image.tiff', b'r')
print (f'TIF Info\n{repr(htiff)}')
print (f'Tiff Version: {TIF.lib.TIFFGetVersion()}')
print (f'CTIFF.Get imagewidth = {TIF.lib.TIFFGetField(htiff, TIFFTAG_IMAGEWIDTH)}')
fieldobj = TIF.lib.TIFFFieldWithTag(htiff, TIFFTAG_IMAGEWIDTH)
print (f'FieldName={TIF.lib.TIFFFieldName(fieldobj)}, DataType={TIFFDataType_dict[TIF.lib.TIFFFieldDataType(fieldobj)]}')
try:
    print (TIF.lib.TIFFFieldWithTag(htiff, 1233545))
except Exception as e:
    print (e)
TIF.TiffClose(htiff)

img = TIF.TiffOpen(b'image.tiff', b'r')
easytif = EasyTif(TIF, img)

print(easytif)

print(f'TiffTags[TIFFTAG_IMAGEWIDTH] = {easytif.GetFieldValue(TIFFTAG_IMAGEWIDTH)}')
print(f'TiffTags[256] = {easytif.GetFieldValue(256)}')
print(f'easytif.imagewidth = {easytif.imagewidth}')
print(f'{TiffTags[TIFFTAG_IMAGELENGTH]} = {easytif.IMAGELENGTH}')
print(f'{TiffTags[TIFFTAG_SAMPLESPERPIXEL]} = {easytif.sAmPLESPeRPIXEL}')
print(f'{TiffTags[TIFFTAG_BITSPERSAMPLE]} = {easytif.bitspersample}')
try:
    print(f'{TiffTags[TIFFTAG_ORIENTATION]} = {easytif.GetFieldValue(TIFFTAG_ORIENTATION)}')
except ValueError as e:
    print(f'Error retrieving {TiffTags[TIFFTAG_ORIENTATION]}: {e}')
print(f'{TiffTags[TIFFTAG_PLANARCONFIG]} = {easytif.planarconfig}')
print(f'easytif.imagedescription = {easytif.imagedescription}')
print(f'easytif.imagedescription field_info = {easytif.GetFieldInfo(TIFFTAG_IMAGEDESCRIPTION)}')
print(f'easytif.123456 field_info = {easytif.GetFieldInfo(123456)}')

easytif.Close()
