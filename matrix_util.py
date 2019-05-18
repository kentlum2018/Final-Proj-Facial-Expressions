
import numpy as np

def reflect_horizontally(img_orig):
    
    img_new = np.flipud(img_orig)
    return img_new

def reflect_vertically(img_orig):

    img_new = np.fliplr(img_orig)
    return img_new

def rotate_right(img_orig):
    
    img_new = np.rot90(img_orig,k=3)
    return img_new

def rotate_left(img_orig):
    
    img_new = np.rot90(img_orig)
    return img_new

def rotate_180(img_orig):
    
    img_new = np.flip(img_orig)
    return img_new