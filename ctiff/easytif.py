import ctypes as C

from .ctiff import *

class EasyTif():
    def __init__(self, tiff_api, hTiff):
        if tiff_api is None:
            raise ValueError('need tiff_api')
        if tiff_api.lib is None:
            raise ValueError('need tiff_api.lib')
        if hTiff is None:
            raise ValueError('need hTiff')

        self._lib = tiff_api.lib
        self._hTiff = hTiff

    def __str__(self):
        imgdesc = self._lib.TIFFGetField(self._hTiff, TIFFTAG_IMAGEDESCRIPTION) \
            .decode('utf-8') \
            .strip()
        return f'EasyTif: tiff_api={self._lib}, hTiff={self._hTiff}, imgdesc={imgdesc}'

    __repr__ = __str__

    def Close(self):
        try:
            self._lib.TIFFClose(self._hTiff)
        except:
            pass
        self._hTiff = None

    def GetHandle(self):
        return self._hTiff

    def GetFieldInfo(self, field_name):
        try:
            field_info = self._lib.TIFFFieldWithTag(self._hTiff, field_name)
        except:
            return (f'Unable to obtain field_info for {field_name}', None)
        field_name = self._lib.TIFFFieldName(field_info)
        field_type = self._lib.TIFFFieldDataType(field_info)
        return (field_name, field_type)

    def GetFieldValue(self, field_name):
        res = self._lib.TIFFGetField(self._hTiff, field_name)
        if res == 0:
            return -1
        return res

    def __getattr__(self, ttag):
        ttag = ttag.upper()
        ttag = 'TIFFTAG_' + ttag

        ttag_id = GetTiffTagId(ttag)
        if (-1 != ttag_id):
            return self.GetFieldValue(ttag_id)
        raise AttributeError(ttag)
