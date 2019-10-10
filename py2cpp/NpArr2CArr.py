from functools import reduce

from .Np2Ctype import np2Ctype
from .Np2MatType import np2CVMatType


def npArr2CArr(img):
    """npArr2CArr(img)
    converts a python opencv image(img) from np array
    to a ctypes flat array of the corresponding C type
    Doing so allows for passing the image easily to C++ functions

    returns a tuple containing the converted image,
    its original shape,
    and the corresponding cv::Mat type constant (eg: CV_8UC3, etc.)

    As of now, it assumes that the image's number of channels
    is the last dimension in its shape (img.shape[-1])
    """
    arr = np2Ctype(img.dtype)
    arr *= reduce(lambda x, y: x * y, img.shape)

    return (arr( *( img.flatten() )  ),
            img.shape,
            np2CVMatType(img.dtype, (img.shape[-1] if len(img.shape) >= 3 else 1)
                        )
           )
