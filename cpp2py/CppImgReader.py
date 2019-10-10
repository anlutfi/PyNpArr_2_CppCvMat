import numpy as np
from numpy.ctypeslib import ndpointer
from functools import reduce
import ctypes as ct

from .Mat2Ctype import mat2Ctype

class CppImgReader:
    """class CppImgReader

       responsible for reading an OpenCV image from C++
       and build a corresponding Python OpenCV image (numpy array).

       It is the counterpart of the PyImgWriter class,
       written in C++. PyImgWriter "writes" an image,
       so that CppImgReader can "read" it.
    """    
    
    ## binding to a c++ dynamic library,
    #  containing PyImgWriter's implementation
    lib = None
    
    
    @staticmethod
    def loadLib(libname = 'libPyImageWriter.so'): 
        """[STATIC] loadLib(libname = 'libPyImageWriter.so')
           
           Loads a dynamic library containing
           PyImgWriter's implementation and binds it
           to CppImgReader.lib
        """
        CppImgReader.lib = ct.CDLL(libname)


    def __init__(self, cobj, libname = 'libPyImageWriter.so'):
        """__init__(self, cobj, libname = 'libPyImageWriter.so')

           instantiates a CppImgReader
           
           cobj is a pointer of types ctypes.c_void_p
                to a C++ PyImgWriter object
           
           libname is the path to a shared library
                   containing PyImgWriter's implementation.
                   it's only used if CppImgReader.loadLib
                   has not yet been called
        """
        
        #load CppImgReader.lib if its not done so already
        if CppImgReader.lib is None:
            CppImgReader.loadLib(libname)
        
        self.cobj = cobj
        
        #get the image's number of dimensions
        getdims = CppImgReader.lib.PyImgW_getDims
        getdims.restype = ct.c_uint32
        
        ## the image's number of dimensions
        self.dims = getdims(self.cobj)
        
        #get the image's shape array
        getshape = CppImgReader.lib.PyImgW_getShape
        getshape.restype = ndpointer(dtype = np.uint32,
                                     shape = (self.dims,)
                                    )
        
        ## the image's shape array
        self.shape = getshape(self.cobj)
        
        # get the image's OpenCV Mat type constant
        gettype = CppImgReader.lib.PyImgW_getType
        gettype.restype = ct.c_uint32
        
        ## the image's type from ctypes, corresponding
        #  to the original cv::Mat's type
        self.ctype = mat2Ctype( gettype(self.cobj) )

        ## binding to function to get the raw image data
        #  from the C++ object
        self.grabimg = CppImgReader.lib.PyImgW_getImg
        
        ## flag that indicates if the source C++ object (self.cobj)
        #  still exists in memory
        self.existscobj = True


    def getImg(self, destroy = False):
        """getImg(self, destroy = False)
           
           function that gets a C++ OpenCV's image (cv::Mat)
           and returns a corresponding Python OpenCV's image (numpy array)

           if destroy is True, the underlying C++ object (self.cobj)
           is deleted after the image is retrieved
        """
        
        assert self.existscobj, "corresponding C object already deleted"

        #set grabimg return type to a buffer of
        # the necessary size,
        # according to self.shape and self.ctype
        self.grabimg.restype = ndpointer(dtype = self.ctype, 
                                   shape = (reduce(lambda x, y:
                                                x * y,
                                                self.shape
                                                  ),
                                           )
                                        )
                                   
        #grab the raw data and reshape it
        img = self.grabimg(self.cobj)
        img = np.reshape(img, tuple(self.shape))
        
        #delete the C++ object if it's the case
        if destroy:
            self.lib.PyImgW_delete(self.cobj)
            self.existscobj = False

        return img


    def debug(self):
        """debug(self)

           Outputs a CppImgReader's info, for debugging
        """
        if not self.existscobj:
            print('ATTENTION: CORRESPONDING C OBJECT ALREADY DELETED')
        print("dims: {}".format(self.dims))
        print("shape: {}".format(self.shape))
        print("ctype: {}".format(self.ctype))