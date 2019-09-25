# PyNpArr_2_CppCvMat

__PyNpArr_2_CppCvMat__ is a simple interface to send OpenCV images from Python to C++ and vice-versa

OpenCV code in Python, although practical to write, can run quite slowly. Pixel-wise operations, if not done inside OpenCV's calls, can make real-time applications impossible.

On the other hand, while it runs much faster, C++ code can be quite a pain to debug, due to the lack of a practical console.

Implementing the heavy part in C++ and running it from Python is the best of both worlds.

While sending basic types and data structures between the two is easy, sending images is not. This tool focuses on this specific problem. Although there are solutions that could handle the task, such as Boost, they tend to be quite bulky. This code was written using the ctypes Python package, which is in its standard distribution.


cpp2py contains the tools to convert from a OpenCV C++ image(cv::Mat) to a Python OpenCV image(numpy array)

py2cpp does the opposite
<br><br><br><br><br><br>
## FILES

imgtst.py is a file that tests sending an image from Python to C++ and back.


### cpp2py files:

  __-PyImgWriter.hpp and PyImgWriter.cpp:__ C++ implementation of the `PyImgWriter` class.
       It serializes a `cv::Mat`'s raw data, so Python can read it as an array of bytes.
                
  __-CppImgReader.py:__ Python implementation of the `CppImgReader` class.
       It fetches the `PyImgWriter`'s raw image data and the original image's
       spatial and type attributes and rebuilds the image as a numpy array.
              
  __-Mat2Ctype.py__: Responsible for corresponding `cv::Mat` types (constants such as `cv::CV_8UC3`, for example)
       to their ctypes counterparts. Used internally by `CppImgReader`.<br><br><br><br>
### py2cpp files:

  __-PyImgReader.hpp and PyImgReader.cpp:__ C++ implementation of the `PyImgReader` class.
       It receives a byte array containing the raw image data, together with
       its spatial and type attributes, so it can construct a `cv::Mat` from it.
                
  __-CppImgWriter.py__: Python Implementation of the `CppImgWriter`. It serializes a numpy array
       that contains an image and sends it to a `PyImgReader`.
                
  __NpArr2CArr.py__: serializes a numpy array into a ctypes array of its corresponding type.
       Used internally by `CppImgWriter`.
                
  __Np2Ctype.py__: Responsible for corresponding numpy array data types to their ctypes counterparts.
       Used internally by `NpArr2CArr.py`.
                
  __Np2MatType.py__: Responsible for corresponding numpy array data types 
       to their `cv:Mat` types counterparts (constants such as `cv::CV_8UC3`, for example).
       Used internally by `NpArr2CArr.py`.
<br><br><br><br><br><br>
## USAGE


### When designing a C++ function that has to return an image to python:

Instead of:
    
```c++
cv::Mat* someFunction(...)
{
    cv::Mat* img = new cv::Mat(...);
    ...
    return img
}
```


Do:

```c++
extern "C"
{
    PyImgWriter* someFunction(...)
    {
        cv::Mat* img = new cv::Mat(...);
        ...
        return new PyImgWriter(img);
    }
}
/* Note that ctypes only deals with C functions, hence the extern declaration
   In order to make a member of an object visible to python,
   make a C wrapper around it
*/
```
    

Receiving the image with Python:

```python
import ctypes as ct

lib = ct.CDLL(path_to_C_lib_containing_someFunction)
lib.someFunction.restype = ct.c_void_p
...
reader = CppImgReader(lib.someFunction(someargs))

img = reader.getImg()
```
<br><br><br><br>
### When designing a C++ function that needs to receive an image from Python:

Instead of:
    
```c++
returntype someFunction(cv::Mat* img)
```    
    
    
Do:

```c++   
returntype someFunction(PyImgReader* reader)
{
    cv::Mat* img = reader->getImg();
    ...
}
```
    
    
Sending the image with Python:

```python
import ctypes as ct

lib = ct.CDLL(path_to_C_lib_containing_someFunction)
...
img = someimage OR imgpath = path_to_some_image
...
writer = CppImgWriter(img=img OR imgpath=imgpath)

someresult = lib.someFunction(writer.sendImg())
```
<br><br><br><br><br><br>
## DEPENDENCIES:
<br>Development was done in an enviroment with these characteristics:
    
 &nbsp;&nbsp;&nbsp;&nbsp;Python modules:
<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Python 3.6.8
<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OpenCV 4.1.0
<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ctypes 1.1.0
<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;numpy 1.17.0
       
<br> &nbsp;&nbsp;&nbsp;&nbsp;C++ modules:
<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OpenCV 4.1.1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
