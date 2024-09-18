#!/usr/bin/env python3

from ctiff.ctiff import *
from ctiff.easytif import *

TIF = ctiff()
print(TIF)

print('testing ctiff')
htiff = TIF.TiffOpen(b'image.tiff', b'r')
print (f'TIF Info\n{repr(htiff)}')
print (f'Tiff Version: {TIF.lib.TIFFGetVersion()}')
print('\nread image width')
print (f'CTIFF.Get imagewidth = {TIF.lib.TIFFGetField(htiff, TIFFTAG_IMAGEWIDTH)}')
fieldobj = TIF.lib.TIFFFieldWithTag(htiff, TIFFTAG_IMAGEWIDTH)
print (f'FieldName={TIF.lib.TIFFFieldName(fieldobj)}, DataType={TIFFDataType_dict[TIF.lib.TIFFFieldDataType(fieldobj)]}')
print('\nread an unknown field')
try:
    print (TIF.lib.TIFFFieldWithTag(htiff, 1233545))
except Exception as e:
    print (e)
print('\nset software field value')
print (TIF.lib.TIFFSetField(htiff, TIFFTAG_SOFTWARE, "software-value"))
print (TIF.lib.TIFFGetField(htiff, TIFFTAG_SOFTWARE))
TIF.TiffClose(htiff)


print('\ntesting easytif')
img = TIF.TiffOpen(b'image.tiff', b'r')
easytif = EasyTif(TIF, img)

print(easytif)

print ('\nreading ImageWidth in different ways')
print(f'TiffTags[TIFFTAG_IMAGEWIDTH] = {easytif.GetFieldValue(TIFFTAG_IMAGEWIDTH)}')
print(f'TiffTags[256] = {easytif.GetFieldValue(256)}')
print(f'easytif.imagewidth = {easytif.imagewidth}')
print(f'{TiffTags[TIFFTAG_IMAGELENGTH]} = {easytif.IMAGELENGTH}')
print ('\n read some other properties using different cases')
print(f'{TiffTags[TIFFTAG_SAMPLESPERPIXEL]} = {easytif.sAmPLESPeRPIXEL}')
print(f'{TiffTags[TIFFTAG_BITSPERSAMPLE]} = {easytif.bitspersample}')
print(f'\nNo actual value for orientation in this case')
try:
    print(f'{TiffTags[TIFFTAG_ORIENTATION]} = {easytif.GetFieldValue(TIFFTAG_ORIENTATION)}')
except ValueError as e:
    print(f'Error retrieving {TiffTags[TIFFTAG_ORIENTATION]}: {e}')
print(f'{TiffTags[TIFFTAG_PLANARCONFIG]} = {easytif.planarconfig}')
print(f'easytif.imagedescription = {easytif.imagedescription}')
print(f'easytif.imagedescription field_info = {easytif.GetFieldInfo(TIFFTAG_IMAGEDESCRIPTION)}')
print(f'\nBad value 123456')
print(f'easytif.123456 field_info = {easytif.GetFieldInfo(123456)}')
print(f'\nReadall')
easytif.readall
print(f'\nSetting some text field values.')
print(f'file is opened read-only so they are not persistent from test to test')
print(f'\twith SetFieldValue')
easytif.SetFieldValue(TIFFTAG_HOSTCOMPUTER, 'host-computer')
print(f'\t\t{easytif.hostcomputer}')
print(f'\twith __setattr__')
easytif.hostcomputer='new-computer'
print(f'\t\t{easytif.hostcomputer}')

easytif.Close()
