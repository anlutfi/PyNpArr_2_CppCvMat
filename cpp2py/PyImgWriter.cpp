/**
build:  g++ -shared -fPIC -o libPyImageWriter.so PyImgWriter.cpp -lopencv_core -lopencv_imgcodecs -std=c++11
*/
#include "PyImgWriter.hpp"

PyImgWriter::PyImgWriter(cv::Mat* img)
{
    //copies the content of img to the object, for memory safety
    this->img = img->clone();
}


unsigned char* PyImgWriter::getImg()
{
    return this->img.data;
}


unsigned int* PyImgWriter::getShape()
{
    unsigned int* result = (unsigned int*)malloc(3 * sizeof(unsigned int));

    result[0] = this->img.rows;
    result[1] = this->img.cols;
    result[2] = this->img.channels();

    return result;
}


int PyImgWriter::getType()
{
    return this->img.type();
}


int PyImgWriter::getDims()
{
    return (this->img.dims
            + ( (this->img.channels() > 1) ? 1 : 0 )
           );
}
