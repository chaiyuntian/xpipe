# A demo for Johnny.

from PySide2 import QtGui

def get_image_width_height(image_path):
    img = QtGui.QImage(image_path)
    if img:
        return img.width(),img.height()

if __name__ == "__main__":
    w,h = get_image_width_height("seamonster.jpg")
    print(w,h)
