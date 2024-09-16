import pytest

from ctiff.ctiff import *
from ctiff.easytif import *

@pytest.fixture
def tiff_api():
    tif = ctiff()
    yield tif

@pytest.fixture
def tiff_handle(tiff_api):
    return tiff_api.TiffOpen(b'image.tiff', b'r')

@pytest.mark.easytif
def test_easy_tif(tiff_api, tiff_handle):
    easy_tif = EasyTif(tiff_api, tiff_handle)
    assert easy_tif.GetHandle() == tiff_handle
    easy_tif.Close()
    assert easy_tif.GetHandle() is None

@pytest.mark.easytif
def test_get_field_value(tiff_api, tiff_handle):
    easy_tif = EasyTif(tiff_api, tiff_handle)
    field_value = easy_tif.GetFieldValue(TIFFTAG_IMAGEDESCRIPTION)
    assert field_value != -1
    assert isinstance(field_value, bytes)
    assert field_value.decode('utf-8').strip() == 'ImageJ=1.54f'
    easy_tif.Close()

@pytest.mark.easytif
def test_get_field_value_and_getattr(tiff_api, tiff_handle):
    easy_tif = EasyTif(tiff_api, tiff_handle)
    for tag, tag_name in TiffTags.items():
        attr_name = tag_name.split('_')[-1].lower()
        try:
            field_value_get = easy_tif.GetFieldValue(tag)
            field_value_attr = getattr(easy_tif, attr_name)
            assert field_value_get == field_value_attr
        except ValueError as e:
            print(f'Caught ValueError for {tag_name}: {e}')
        except AttributeError as e:
            print(f'Caught AttributeError for {tag_name}: {e}')
    easy_tif.Close()

@pytest.mark.easytif
def test_getattr_known_values(tiff_api, tiff_handle):
    easy_tif = EasyTif(tiff_api, tiff_handle)
    assert 474 == easy_tif.imagewidth
    assert 474 == easy_tif.imagelength
    assert 1  == easy_tif.SAMPLESPERPIXEL
    assert 8 == easy_tif.BITSPERSAMPLE
    assert 1 == easy_tif.PLANARCONFIG
    assert 'ImageJ=1.54f' == easy_tif.imagedescription.decode('utf-8').strip()

@pytest.mark.easytif
def test_get_field_info(tiff_api, tiff_handle):
    easy_tif = EasyTif(tiff_api, tiff_handle)
    for tag, tag_name in TiffTags.items():
        field_name, field_type = easy_tif.GetFieldInfo(tag)
        #print (tag_name, tag, field_name, field_type)
        error_msg = 'Unable to obtain field_info'
        if error_msg in field_name:
            assert False
        assert field_type is not None

    easy_tif.Close()
