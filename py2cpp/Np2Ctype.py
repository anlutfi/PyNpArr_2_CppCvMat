import numpy as np
import ctypes as ct

def np2Ctype(nptype):
    """np2Ctype(nptype)
    returns a type from ctypes that corresponds
    to the numpy type(nptype) provided as argument
    """
    try:
        return typedict[nptype]

    except KeyError:
        print( "ERROR: key {} not present in Np2Ctype.typedict".format(nptype) )
        raise(KeyError)


typedict = {np.dtype('uint8'): ct.c_uint8,
            np.dtype('byte'): ct.c_char,
            np.dtype('uint16'): ct.c_uint16,
            np.dtype('int16'): ct.c_int16,
            np.dtype('int32'): ct.c_int32,
            np.dtype('float'): ct.c_float
           }
