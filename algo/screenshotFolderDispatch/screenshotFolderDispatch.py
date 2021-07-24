import glob
from PIL import Image
import os
import shutil

category_set = set()
threshold_ratio_r2g = 0.1
threshold_ratio_r2b = 0.1
threshold_ratio_g2b = 0.1
threshold_ratio_b2g = 0.1
threshold_hour = 0
threshold_minute = 5

# 0                    , 1   , 2   , 3    , 4    , 5 , 6
def is_in_category(r , g , b , date , hour , minute , category_set):
    ratio_r2g = round(1.0 * r/g,2)
    ratio_g2r = round(1.0 * g/r,2)

    ratio_b2r = round(1.0 * b/r,2)
    ratio_r2b = round(1.0 * r/b,2)

    ratio_g2b = round(1.0 * g/b,2)
    ratio_b2g = round(1.0 * b/g,2)

    #print (ratio_r2g, ratio_b2r, ratio_g2b, ratio_r2b, ratio_b2g, ratio_g2r )
    date = int(date)
    hour = int(hour)
    minute = int(minute)

    folder_output_prefix = ["~/Downloads/", "/home/phil/CameraTemp/"][1]

    for k in category_set:
        #print(k)
        """
        if  (k[0] - threshold_ratio_r2g) <= ratio_r2g <= (k[0] + threshold_ratio_r2g) and \
            (k[1] - threshold_ratio_r2b) <= ratio_r2b <= (k[1] + threshold_ratio_r2b) and \
            (k[1] - threshold_ratio_r2b) <= ratio_r2b <= (k[1] + threshold_ratio_r2b) and \
            (k[2]- threshold_hour) <= hour <= (k[2]+ threshold_hour) and \
            (k[3]- threshold_minute) <= minute <= (k[3]+ threshold_minute):
        """

        if   (k[0] - threshold_ratio_r2g) <= ratio_r2g <= (k[0] + threshold_ratio_r2g) and \
             (k[1] - threshold_ratio_g2b) <= ratio_g2r <= (k[1] + threshold_ratio_g2b) and \
             (k[2] - threshold_ratio_r2b) <= ratio_r2b <= (k[2] + threshold_ratio_r2b) and \
             (k[3] - threshold_ratio_g2b) <= ratio_b2r <= (k[3] + threshold_ratio_g2b) and \
             (k[4] - threshold_ratio_g2b) <= ratio_g2b <= (k[4] + threshold_ratio_g2b) and \
             (k[5] - threshold_ratio_b2g) <= ratio_b2g <= (k[5] + threshold_ratio_b2g) and \
             (k[6]- threshold_hour) <= hour <= (k[6]+ threshold_hour) and \
             (k[7]- threshold_minute) <= minute <= (k[7]+ threshold_minute):

            folder_output = folder_output_prefix + f'_{k[0]}_{k[1]}_{k[2]}_{k[3]}_{k[4]}_{k[5]}_{date}_{k[6]}{k[7]}/'

            if not os.path.exists(folder_output): os.makedirs(folder_output)

            return (True, folder_output)

    category_set.add((ratio_r2g, ratio_g2r, ratio_r2b, ratio_b2r, ratio_g2b, ratio_b2g, hour, minute ))
    folder_output = folder_output_prefix + f'_{ratio_r2g}_{ratio_b2r}_{ratio_g2b}_{ratio_r2b}_{ratio_b2g}_{ratio_g2r}_{date}_{hour}{minute}/'

    #category_set.add((ratio_r2g, ratio_r2b, ratio_g2b, int(date), int(hour), int(minute)))
    if not os.path.exists(folder_output): os.makedirs(folder_output)
    return (False,folder_output)

################################################# {{{2 {

def dispatch3(feature_vector):
    """
    Camera pictures
    """
    #dimension = feature_vector[0] *  feature_vector[1]
    (filepath,tempfilename) = os.path.split(feature_vector[-1])
    (shortname,extension) = os.path.splitext(tempfilename)
    shortname_list = shortname.strip().split('_')
    date = shortname_list[1]
    hour, minute, second = shortname_list[2][0:2],  shortname_list[2][2:4],  shortname_list[2][4:6]
    #print(date, hour, minute)
    
    _is_in_category = is_in_category(feature_vector[3], feature_vector[4], feature_vector[5], date, hour, minute, category_set)

    shutil.move(feature_vector[-1], _is_in_category[1]+tempfilename)

def dispatch2(feature_vector):
    """
    '/Users/y0f00k5/Pictures/screenshot/*',
     2020-07-28 at 5.57.39 PM.png
    """
    dimension = feature_vector[0] *  feature_vector[1]
    (filepath,tempfilename) = os.path.split(feature_vector[-1])
    (shortname,extension) = os.path.splitext(tempfilename)
    shortname_list = shortname.strip().split()
    date = shortname_list[0].replace('-','')
    (hour, minute, second) = shortname_list[2].split('.')
    
    _is_in_category = is_in_category(feature_vector[3], feature_vector[4], feature_vector[5], date, hour, minute, category_set)

    shutil.move(feature_vector[-1], _is_in_category[1]+tempfilename)

def dispatch1(feature_vector):
    """
    '/Users/y0f00k5/Pictures/Monosnap/*'
    """
    (filepath,tempfilename) = os.path.split(feature_vector[-1])
    (shortname,extension) = os.path.splitext(tempfilename)
    #folder_output_prefix = "~/Downloads/"
    shortname_list = shortname.strip().split()
    _shortname_list = shortname_list[-1].split('_')
    date = _shortname_list[0]
    hour, minute, second = _shortname_list[1][0:2],  _shortname_list[1][2:4],  _shortname_list[1][4:6]
    
    _is_in_category = is_in_category(feature_vector[3], feature_vector[4], feature_vector[5], date, hour, minute, category_set)

    shutil.move(feature_vector[-1], _is_in_category[1]+tempfilename)

def dispatch4(feature_vector):
    """
    2021_0717_2015 
    on ubuntu
     ~/Documents/b/toD/pic/Camera/
    """
    (filepath,tempfilename) = os.path.split(feature_vector[-1])
    (shortname,extension) = os.path.splitext(tempfilename)
    #folder_output_prefix = "~/Downloads/"
    shortname_list = shortname.strip().split()
    _shortname_list = shortname_list[-1].split('_')
    date = _shortname_list[1]
    hour, minute, second = _shortname_list[2][0:2],  _shortname_list[2][2:4],  _shortname_list[2][4:6]
    
    _is_in_category = is_in_category(feature_vector[3], feature_vector[4], feature_vector[5], date, hour, minute, category_set)
    #print(    _is_in_category)

    #print(feature_vector[-1], _is_in_category[1]+tempfilename)
    shutil.move(feature_vector[-1], _is_in_category[1]+tempfilename)

################################################# } 2}}}

def dispatch(feature_vector):
    return dispatch4(feature_vector)

def main():

    folder_src = ['/home/phil/Documents/b/toD/pic/Camera/','/Users/y0f00k5/Documents/b/toD/todo/screenshot20201105_ks/','/Users/y0f00k5/Pictures/screenshot/', '/Users/y0f00k5/Pictures/Monosnap/'][0] + '*'

    for ele in glob.glob(folder_src):
        print (ele)
        if 'psd' in ele or 'mp4' in ele:
            continue
        
        im = Image.open(ele) # Can be many different formats.
        pix = im.load()

        channel_num = len(pix[1,1])
        accumulative_r = 0
        accumulative_g = 0
        accumulative_b = 0

        for x in range(im.size[0]):
            for y in range(im.size[1]):
                if len(pix[x,y])==4:
                    (r,g,b,_) = pix[x,y]
                else:
                    (r,g,b) = pix[x,y]

                accumulative_r += r
                accumulative_g += g
                accumulative_b += b

        # 0                              , 1          , 2           , 3              , 4              , 5              , 6    , 7
        feature_vector = [im.size[0] , im.size[1] , channel_num , accumulative_r , accumulative_g , accumulative_b , ele]
        #print (feature_vector) 
        try:
            dispatch(feature_vector)
        except:
            continue

    print (category_set)

if __name__ == '__main__':
    main()
