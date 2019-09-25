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