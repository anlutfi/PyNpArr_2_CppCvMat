/** PyImgWriter.hpp
 * 
 *  Module containing the PyImgWriter class declaration
 *  and C functions that wrap its functionalities,
 *  to be used by python ctypes.
 *  
 *  PyImgWriter is responsible to serialize
 *  an OpenCV image (cv::Mat) so it can be consumed
 *  by a python function, that reconstructs it with Python's opencv
 * 
 *  This class is the counterpart of CppImgReader implemented in
 *  Python. PyImgWriter "writes" an image to Python.
 *  CppImgReader "reads" said image.
 * 
 */

#ifndef _PYIMGWRITER_H_
#define _PYIMGWRITER_H_


#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>

/** PyImgWriter
 *  class responsible for serializing an OpenCV Mat
 *  into an array of bytes so a Python function can
 *  reconstruct it 
*/
class PyImgWriter
{
    public:
    /* the source image
    */
    cv::Mat img;
    
    /* constructor that receives a pointer to the image
       to be serialized
    */
    PyImgWriter(cv::Mat* img);
    
    /* returns an array of bytes containing the image's raw data
    */
    unsigned char* getImg();
    
    /* returns an array with the sizes
       of each of the image's dimensions (example: h, w, depth)
    */
    unsigned int* getShape();
    
    /* returns the image's opencv Mat type constant,
       such as cv::CV_8UC3
    */
    int getType();
    
    /* returns the image's number of dimensions
       a grayscale image has 2 dimensions,
       an RGB has 3, for example
    */
    int getDims();
};

/** Wrappers for PyImgWriter's methods, to be called by python,
 *  through ctypes package. ctypes only interacts with C functions.
*/
extern "C"
{
    /** Wrapper that creates and returns a PyImgWriter
     *  same arguments as PyImgWriter's constructor
    */
    PyImgWriter* PyImgW_new(cv::Mat* img)
    {
        return new PyImgWriter(img);
    }
    
    
    /** Wrapper that returns a PyImgWriter's raw image data
    */
    unsigned char* PyImgW_getImg(PyImgWriter* obj)
    {
        return obj->getImg();
    }


    /** Wrapper that returns a PyImgWriter shape array
    */
    unsigned int* PyImgW_getShape(PyImgWriter* obj)
    {
        return obj->getShape();
    }


    /** Wrapper that returns a PyImgWriter OpenCV type constant
    */
    int PyImgW_getType(PyImgWriter* obj)
    {
        return obj->getType();
    }
    
    
    /** Wrapper that returns a PyImgWriter's number of dimensions
    */
    int PyImgW_getDims(PyImgWriter* obj)
    {
        return obj->getDims();
    }

    /** Wrapper that deletes a PyImgWriter
    */
    void PyImgW_delete(PyImgWriter* obj)
    {
        delete obj;
    }
}


#endif