class Crop:

    width = 0 # width of smaller image
    height = 0 # height of smaller image
    curr_w = 0 # placeholder for image width
    curr_h = 0 # placeholder for image height
    shift = 5 # the amount of pixels to shift by
    cropped = dict() # create an array of cropped images taken from original image

    def __init__(self, image, w, h):
        self.width = w
        self.height = h

    # Crops the given image to the specified width and height
    def crop(self, width, height, image):
        # stub
        if self.inBounds():
            # if in bounds then take the array of

    # Checks if the pixels are greater than the width or height of the given image
    def inBounds(self, num, dir):
        if dir == "right"
            if (num + self.shift) > self.width:
                return False
        elif dir == "down"
            if (num + self.shift) > self.height:
                return False

        return True