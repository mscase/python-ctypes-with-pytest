import pytest
from ctiff.ctiff import *

@pytest.fixture
def tiff_api():
    return ctiff()

@pytest.fixture
def tiff_handle(tiff_api):
    return tiff_api.TiffOpen(b'image.tiff', b'r')

@pytest.mark.ctiff
def test_tiff_open_close(tiff_api):
    tiff_handle = tiff_api.TiffOpen(b'image.tiff', b'r')
    assert tiff_handle is not None
    tiff_api.TiffClose(tiff_handle)

@pytest.mark.ctiff
def test_tiff_get_field_imagewidth(tiff_api, tiff_handle):
    value = tiff_api.lib.TIFFGetField(tiff_handle, TIFFTAG_IMAGEWIDTH)
    assert value is not None
    assert isinstance(value, int)

@pytest.mark.ctiff
def test_tiff_get_field_imagelength(tiff_api, tiff_handle):
    value = tiff_api.lib.TIFFGetField(tiff_handle, TIFFTAG_IMAGELENGTH)
    assert value is not None
    assert isinstance(value, int)

@pytest.mark.ctiff
def test_tiff_get_field_samplesperpixel(tiff_api, tiff_handle):
    value = tiff_api.lib.TIFFGetField(tiff_handle, TIFFTAG_SAMPLESPERPIXEL)
    assert value is not None
    assert isinstance(value, int)

@pytest.mark.ctiff
def test_tiff_get_field_bitspersample(tiff_api, tiff_handle):
    value = tiff_api.lib.TIFFGetField(tiff_handle, TIFFTAG_BITSPERSAMPLE)
    assert value is not None
    assert isinstance(value, int)

@pytest.mark.ctiff
def test_tiff_get_field_planarconfig(tiff_api, tiff_handle):
    value = tiff_api.lib.TIFFGetField(tiff_handle, TIFFTAG_PLANARCONFIG)
    assert value is not None
    assert isinstance(value, int)

@pytest.mark.ctiff
def test_tiff_get_field_imagedescription(tiff_api, tiff_handle):
    value = tiff_api.lib.TIFFGetField(tiff_handle, TIFFTAG_IMAGEDESCRIPTION)
    assert value is not None
    assert isinstance(value, bytes)
    assert value.decode('utf-8').strip() == 'ImageJ=1.54f'

@pytest.mark.ctiff
def test_tiff_get_field_orientation(tiff_api, tiff_handle):
    with pytest.raises(ValueError) as excinfo:
        value = tiff_api.lib.TIFFGetField(tiff_handle, TIFFTAG_ORIENTATION)
    assert str(excinfo.value) == f'Failed to get value for [{TiffTags[TIFFTAG_ORIENTATION]}]'

@pytest.mark.ctiff
def test_tiff_get_field_with_tag(tiff_api, tiff_handle):
    field_info = tiff_api.lib.TIFFFieldWithTag(tiff_handle, TIFFTAG_IMAGEWIDTH) 
    field_name = tiff_api.lib.TIFFFieldName(field_info)
    field_type = tiff_api.lib.TIFFFieldDataType(field_info)
    assert field_name == 'ImageWidth'
    assert field_type == TIFFDataType.TIFF_LONG

@pytest.mark.ctiff
def test_tiff_get_field_nameerror(tiff_api, tiff_handle):
    with pytest.raises(NameError) as excinfo:
        value = tiff_api.lib.TIFFGetField(tiff_handle, TIFFTAG_BADVALUE)
    assert str(excinfo.value) == f"name 'TIFFTAG_BADVALUE' is not defined"

@pytest.mark.ctiff
def test_tiff_tags_match():
    # Ensure both dictionaries have the same keys
    assert set(TiffTags.keys()) == set(TiffTags2.values()), 'Keys of TiffTags do not match values of TiffTags2'

    # Ensure both dictionaries have the same values
    for key, value in TiffTags.items():
        assert TiffTags2[value] == key, f'Value mismatch for key {key}: {TiffTags2[value]} != {key}'

@pytest.mark.ctiff
def test_tiff_set_field(tiff_api, tiff_handle):
    tiff_api.lib.TIFFSetField(tiff_handle, TIFFTAG_HOSTCOMPUTER, 'host-computer') 
    host_computer = tiff_api.lib.TIFFGetField(tiff_handle, TIFFTAG_HOSTCOMPUTER)
    assert host_computer == b'host-computer'
    tiff_api.lib.TIFFSetField(tiff_handle, TIFFTAG_HOSTCOMPUTER, 'computer-host') 
    computer_host = tiff_api.lib.TIFFGetField(tiff_handle, TIFFTAG_HOSTCOMPUTER)
    assert computer_host == b'computer-host'

