import numpy as np 
import cv2

def np2CVMatType(nptype, channels):
    """np2CVMatType(nptype, channels)
    returns the opencv pixel type constant of a given image

    nptype is the numpy type of each of the image's channel
    channels is the number of channels in the pixel
    """
    try:
        name = typedict[nptype] + 'C{}'.format(channels)
    
    except KeyError:
        print( "ERROR: key {} not present in Np2MatType.typedict".format(nptype) )
        raise(KeyError)

    try:    
        return cvmattypes[name]
    
    except KeyError:
        print( "ERROR: key {} not present in Np2MatType.cvmattypes".format(name) )
        raise(KeyError)



typedict = {np.dtype('uint8'): "CV_8U",
            np.dtype('byte'): "CV_8S",
            np.dtype('uint16'): "CV_16U",
            np.dtype('int16'): "CV_16S",
            np.dtype('int32'): "CV_32S",
            np.dtype('float'): "CV_32F"
           }

cvmattypes = {"CV_8UC1": cv2.CV_8UC1,
              "CV_8UC2": cv2.CV_8UC2,
              "CV_8UC3": cv2.CV_8UC3,
              "CV_8UC4": cv2.CV_8UC4,
              "CV_8SC1": cv2.CV_8SC1,
              "CV_8SC2": cv2.CV_8SC2,
              "CV_8SC3": cv2.CV_8SC3,
              "CV_8SC4": cv2.CV_8SC4,
              "CV_16UC1": cv2.CV_16UC1,
              "CV_16UC2": cv2.CV_16UC2,
              "CV_16UC3": cv2.CV_16UC3,
              "CV_16UC4": cv2.CV_16UC4,
              "CV_16SC1": cv2.CV_16SC1,
              "CV_16SC2": cv2.CV_16SC2,
              "CV_16SC3": cv2.CV_16SC3,
              "CV_16SC4": cv2.CV_16SC4,
              "CV_32SC1": cv2.CV_32SC1,
              "CV_32SC2": cv2.CV_32SC2,
              "CV_32SC3": cv2.CV_32SC3,
              "CV_32SC4": cv2.CV_32SC4,
              "CV_32FC1": cv2.CV_32FC1,
              "CV_32FC2": cv2.CV_32FC2,
              "CV_32FC3": cv2.CV_32FC3,
              "CV_32FC4": cv2.CV_32FC4,
              "CV_64FC1": cv2.CV_64FC1,
              "CV_64FC2": cv2.CV_64FC2,
              "CV_64FC3": cv2.CV_64FC3,
              "CV_64FC4": cv2.CV_64FC4
             }




























