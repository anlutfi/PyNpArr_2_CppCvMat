PyNpArr_2_CppCvMat is a simple interface to send OpenCV images from Python to C++ and vice-versa

OpenCV code in Python, although practical to write, can run quite slowly. Pixel-wise operations, if not done inside OpenCV's calls, can make real-time applications impossible.

On the other hand, while it runs much faster, C++ code can be quite a pain to debug, due to the lack of a practical console.

Implementing the heavy part in C++ and running it from Python is the best of both worlds.

While sending basic types and data structures between the two is easy, sending images is not. This tool focuses on this specific problem. Although there are solutions that could handle the task, such as Boost, they tend to be quite bulky. This code was written using the ctypes Python package, which is in its standard distribution.


cpp2py contains the tools to convert from a OpenCV C++ image(cv::Mat) to a Python OpenCV image(numpy array)

py2cpp does the opposite


cpp2py files:

    -PyImgWriter.hpp and PyImgWriter.cpp: C++ implementation of the PyImgWriter class.
                It serializes a cv::Mat's raw data, so Python can read it as an array of bytes.
                
    -CppImgReader.py: Python implementation of the CppImgReader class.
                It fetches the PyImgWriter's raw image data and the original image's
                spatial attributes and rebuilds the image as a numpy array
                
    -
