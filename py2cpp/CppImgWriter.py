import ctypes as ct
import cv2

from NpArr2CArr import npArr2CArr

class CppImgWriter:
    """class CppImgWriter

       responsible for searializing a Python OpenCV image (numpy array)
       so it can be read by a C++ function and made into
       a C++ Opencv image (cv::Mat)

       It is the counterpart of the PyImgReader class,
       written in C++. CppImgWriter "writes" an image,
       so that PyImgReader can "read" it.
    """
    
    ## binding to a c++ dynamic library,
    #  containing PyImgReader's implementation
    lib = None
    
    @staticmethod
    def loadLib(lib = None, libname = 'libPyImageReader.so'): 
        """[STATIC] loadLib(lib = None, libname = 'libPyImageReader.so')
           
           Loads a dynamic library containing
           PyImgReader's implementation and binds it
           to CppImgReader.lib
        """

        CppImgWriter.lib = lib if lib is not None else ct.CDLL(libname)
    
    
    def __init__(self,
                 img = None,
                 imgpath = '',
                 libname = 'libPyImageReader.so'
                ):
        """__init__(self,
                    img = None,
                    imgpath = '',
                    libname = 'libPyImageReader.so'
                   )

           instantiates a CppImgWriter
           
           img is an OpenCV image (numpy array)

           imgpath is the path containing an image to be loaded,
                   in case img argument was not provided
           
           libname is the path to a shared library
                   containing PyImgReader's implementation.
                   it's only used if CppImgWriter.loadLib
                   has not yet been called
        """
        
        assert (img is not None or imgpath != ''), "No Image Provided"

        # load CppImgWriter.lib if it has not been done so
        if CppImgWriter.lib is None:
            CppImgWriter.loadLib(libname)

        if img is None:
            img = cv2.imread(imgpath)
        
        # serialize img's data, storing its original shape
        # and OpenCV Mat type
        (arr, shape, cvtype) = npArr2CArr(img)
        
        # instantiate a C++ PyImgReader object and store
        # its reference
        newwriter = CppImgWriter.lib.PyImgR_new
        newwriter.restype = ct.c_void_p
        
        # a reference to a C++ PyImgReader object
        self.cobj = newwriter(arr, shape[0], shape[1], cvtype)

    
    def sendImg(self):
        """sendImg(self)
           
           To be used
        """
        return self.cobj
    
    
    def getImg(self):
        """getImg(self)
           
           for debugging purposes.

           grabs a pointer to a cv::Mat of type ctypes.c_void_p
           This is the image stored by C++ PyImgReader object,
           stored in self.cobj
        """
        
        grabimg = CppImgWriter.lib.PyImgR_getImg
        grabimg.restype = ct.c_void_p
        return grabimg(self.cobj)