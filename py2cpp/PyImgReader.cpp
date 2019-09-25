/**
build:  g++ -shared -fPIC -o libPyImageReader.so PyImgReader.cpp -lopencv_core -lopencv_imgcodecs -std=c++11
*/

#include "PyImgReader.hpp"


PyImgReader::PyImgReader(void* data, int h, int w, int type)
{
    cv::Mat img(h, w, type, data);
    this->img = img.clone();
}


cv::Mat* PyImgReader::getImg()
{
    return &(this->img);
}
