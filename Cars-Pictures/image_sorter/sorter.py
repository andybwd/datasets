import os
from PIL import Image
from PIL import ImageColor
import webcolors
import shutil

#Images Path
image_Source_Directory = "C:\\Users\\abawa\\Downloads\\cars_test\\"
image_Target_Directory = "C:\\Users\\abawa\\Downloads\\sorted\\"
image_TumbnailSizeh = 15
image_TumbnailSizew = 90


def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name



#Image Colour Processing 
for filename in os.listdir(image_Source_Directory):
    print(image_Source_Directory + filename)
    original = Image.open(image_Source_Directory + filename) # open RGB image
  
    cropped_img = crop_center(original, image_TumbnailSizew, image_TumbnailSizeh)
    

    reduced = cropped_img.convert("P", palette=Image.ADAPTIVE) # convert to web palette (216 colors)
    palette = reduced.getpalette() # get palette as [r,g,b,r,g,b,...]
    palette = [palette[3*n:3*n+3] for n in range(256)] # group 3 by 3 = [[r,g,b],[r,g,b],...]
    color_count = [(n, palette[m]) for n,m in reduced.getcolors()]

    color_Count_Totals = []
    color_count.sort(reverse=True)
    colcode = (color_count[0][1][0],color_count[0][1][1],color_count[0][1][2])
        
    actual_name, closest_name = get_colour_name(colcode)
   
    print("closest colour name:", closest_name)

    CHECK_FOLDER = os.path.isdir(image_Target_Directory + closest_name)
    
    if not CHECK_FOLDER: 
        colordir = image_Target_Directory + closest_name
        os.makedirs(colordir)
        print("created folder : ", colordir)
        fullpaths = image_Source_Directory + filename
        fullpatht = colordir + '/' + filename
        shutil.copyfile(fullpaths,fullpatht)
        cropped_img.save(colordir + '/' +'tn_' + filename )
    else:
        print(colordir, "folder already exists.")
        fullpaths = image_Source_Directory + filename
        fullpatht = colordir + '/' + filename
        shutil.copyfile(fullpaths,fullpatht)
        cropped_img.save(colordir + '/tn_' + filename )