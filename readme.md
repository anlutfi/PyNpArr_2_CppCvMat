PyNpArr_2_CppCvMat is a simple interface to send OpenCV images from Python to C++ and vice-versa

OpenCV code in Python, although practical to write, can run quite slowly. Pixel-wise operations, if not done inside OpenCV's calls, can make real-time applications impossible.

On the other hand, while it runs much faster, C++ code can be quite a pain to debug, due to the lack of a practical console.

Implementing the heavy part in C++ and running it from Python is the best of both worlds.

While sending basic types and data structures between the two is easy, sending images is not. This tool focuses on this specific problem. Although there are solutions that could handle the task, such as Boost, they tend to be quite bulky. This code was written using the ctypes Python package, which is in its standard distribution.


cpp2py contains the tools to convert from a OpenCV C++ image(cv::Mat) to a Python OpenCV image(numpy array)

py2cpp does the opposite



imgtst.py is a file that tests sending an image from Python to C++ and back.


cpp2py files:

    -PyImgWriter.hpp and PyImgWriter.cpp: C++ implementation of the PyImgWriter class.
                It serializes a cv::Mat's raw data, so Python can read it as an array of bytes.
                
    -CppImgReader.py: Python implementation of the CppImgReader class.
                It fetches the PyImgWriter's raw image data and the original image's
                spatial and type attributes and rebuilds the image as a numpy array.
                
    -Mat2Ctype.py: Responsible for corresponding cv::Mat types (constants such as CV_8UC3, for example)
                to their ctypes counterparts. Used internally by CppImgReader.
                
                                
py2cpp files:

    -PyImgReader.hpp and PyImgReader.cpp: C++ implementation of the PyImgReader class.
                It receives a byte array containing the raw image data, together with
                its spatial and type attributes, so it can construct a cv::Mat from it.
                
    -CppImgWriter.py: Python Implementation of the CppImgWriter. It serializes a numpy array
                that contains an image and sends it to a PyImgReader.
                
    NpArr2CArr.py: serializes a numpy array into a ctypes array of its corresponding type.
                Used internally by CppImgWriter.
                
    Np2Ctype.py: Responsible for corresponding numpy array data types to their ctypes counterparts.
                 Used internally by NpArr2CArr.py.
                
    Np2MatType.py: Responsible for corresponding numpy array data types 
                to their cv:Mat types counterparts (constants such as CV_8UC3, for example).
                Used internally by NpArr2CArr.py.
    
    
    
DEPENDENCIES:
    Development was done in an enviroment with these characteristics:
    
    Python modules:
        Python 3.6.8
        OpenCV 4.1.0
        ctypes 1.1.0
        numpy 1.17.0
        
    C++ modules:
        OpenCV 4.1.1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
