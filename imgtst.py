import ctypes as ct
import cv2

import sys
sys.path.append('/home/antonio/Dropbox/projects/PyNpArr_2_CppCvMat/cpp2py')
sys.path.append('/home/antonio/Dropbox/projects/PyNpArr_2_CppCvMat/py2cpp')

from cpp2py.CppImgReader import CppImgReader
from py2cpp.CppImgWriter import CppImgWriter


def show(img): 
    cv2.imshow(' ', img) 
    cv2.waitKey(0) 
    cv2.destroyWindow(' ')



CppImgWriter.loadLib(libname = '/home/antonio/Dropbox/projects/PyNpArr_2_CppCvMat/py2cpp/libPyImageReader.so')
CppImgReader.loadLib(libname = '/home/antonio/Dropbox/projects/PyNpArr_2_CppCvMat/cpp2py/libPyImageWriter.so')

writer = CppImgWriter(imgpath = '/home/antonio/tests/img2.jpg')

lib = ct.CDLL('/home/antonio/Dropbox/projects/PyNpArr_2_CppCvMat/libdrawrect.so')

drawRect = lib.drawRect

drawRect.restype = ct.c_void_p

makereader = lambda writer: CppImgReader(drawRect(writer.sendImg()))

reader = makereader(writer)

show(reader.getImg())





# newobj = CppImgReader.lib.PyImgW_new
# newobj.restype = ct.c_void_p
# c_reader = CppImgReader(newobj(writer.getImg()))

