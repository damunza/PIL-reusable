import os

def get_images(path, types):
    """
    takes in the directory and list of image formats and returns a list of all the images
    """
    a = 0
    # images for the first type
    first = [os.path.join(path, i) for i in os.listdir(path) if i.endswith(types[a])]
    # images for every type offered 
    while a < (len(types) - 1):
        a +=1
        first += [os.path.join(path, i) for i in os.listdir(path) if i.endswith(types[a])]

    return first