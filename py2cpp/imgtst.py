import ctypes as ct
import cv2

from CppImgReader import CppImgReader
from CppImgWriter import CppImgWriter

def show(img): 
    cv2.imshow(' ', img) 
    cv2.waitKey(0) 
    cv2.destroyWindow(' ')



CppImgWriter.loadLib(libname = '/home/antonio/Dropbox/projects/chicken/pyinterface/py2cpp/libPyImageReader.so')

writer = CppImgWriter(imgpath = '/home/antonio/tests/img2.jpg')


CppImgReader.loadLib(libname = '/home/antonio/Dropbox/projects/chicken/pyinterface/py2cpp/libPyImageWriter.so')

newobj = CppImgReader.lib.PyImgW_new
newobj.restype = ct.c_void_p
c_reader = CppImgReader(newobj(writer.getImg()))

