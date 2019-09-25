import ctypes as ct
import cv2

def mat2Ctype(mattype):
    """mat2Ctype(mattype)
    returns a type from ctypes that corresponds to the
    opencv pixel type constant given as argument
    """
    try:
        supertype = supertypes[mattype]
    
    except KeyError:
        print( "ERROR: key {} not present in Mat2Ctype.supertypes".format(mattype) )
        raise KeyError

    try:
        return typedict[supertype]
    
    except KeyError:
        print( "ERROR: key {} not present in Mat2Ctype.typedict".format(supertype) )
        raise KeyError    



typedict = {"CV_8U": ct.c_uint8,
            "CV_8S": ct.c_char,
            "CV_16U": ct.c_uint16,
            "CV_16S": ct.c_int16,
            "CV_32S": ct.c_int32,
            "CV_32F": ct.c_float
           }

supertypes = {cv2.CV_8UC1: "CV_8U",
              cv2.CV_8UC2: "CV_8U",
              cv2.CV_8UC3: "CV_8U",
              cv2.CV_8UC4: "CV_8U",
              cv2.CV_8SC1: "CV_8S",
              cv2.CV_8SC2: "CV_8S",
              cv2.CV_8SC3: "CV_8S",
              cv2.CV_8SC4: "CV_8S",
              cv2.CV_16UC1: "CV_16U",
              cv2.CV_16UC2: "CV_16U",
              cv2.CV_16UC3: "CV_16U",
              cv2.CV_16UC4: "CV_16U",
              cv2.CV_16SC1: "CV_16S",
              cv2.CV_16SC2: "CV_16S",
              cv2.CV_16SC3: "CV_16S",
              cv2.CV_16SC4: "CV_16S",
              cv2.CV_32SC1: "CV_32S",
              cv2.CV_32SC2: "CV_32S",
              cv2.CV_32SC3: "CV_32S",
              cv2.CV_32SC4: "CV_32S",
              cv2.CV_32FC1: "CV_32F",
              cv2.CV_32FC2: "CV_32F",
              cv2.CV_32FC3: "CV_32F",
              cv2.CV_32FC4: "CV_32F",
              cv2.CV_64FC1: "CV_64F",
              cv2.CV_64FC2: "CV_64F",
              cv2.CV_64FC3: "CV_64F",
              cv2.CV_64FC4: "CV_64F"
             }