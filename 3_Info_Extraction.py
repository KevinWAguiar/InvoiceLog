import pandas as pd
import cv2
import pytesseract
import numpy as np
import re
from PIL import Image, ImageEnhance, ImageFilter
import warnings
warnings.filterwarnings("ignore")

master_vendor_dictionary = {}

"""master_vendor_dictionary['HD_Supply'] = {'vendor': 'HD_Supply',
                                         'number_templ_path': '/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/HD_Supply_number_templ.png',
                                         'date_templ_path': '/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/HD_Supply_date_templ.png',
                                         'total_templ_path': '/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/HD_Supply_total_templ.png',
                                         'number_right_offset': 0,
                                         'number_down_offset': 31,
                                         'date_right_offset': 0,
                                         'date_down_offset': 32,
                                         'total_right_offset': 295,
                                         #'total_right_offset': 350,
                                         'total_down_offset': 0,
                                         'number_info_x_size': 354,
                                         'number_info_y_size': 29,
                                         'date_info_x_size': 354,
                                         'date_info_y_size': 29,
                                         'total_info_x_size': 167,
                                         #'total_info_x_size': 250,
                                         'total_info_y_size': 36}"""

master_vendor_dictionary['HD_Supply'] = {'vendor': 'HD_Supply', 'number_templ_path': '/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/HD_Supply_number_templ.png', 'date_templ_path': '/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/HD_Supply_date_templ.png', 'total_templ_path': '/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/HD_Supply_total_templ.png', 'number_right_offset': 2, 'number_down_offset': 31, 'date_right_offset': 0, 'date_down_offset': 30, 'total_right_offset': 292, 'total_down_offset': 4, 'number_info_x_size': 356, 'number_info_y_size': 32, 'date_info_x_size': 356, 'date_info_y_size': 33, 'total_info_x_size': 174, 'total_info_y_size': 36}

"""master_vendor_dictionary['Naughton Energy Corp.'] = {'vendor': 'Naughton Energy Corp.',
 'number_templ_path': '/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/Naughton Energy Corp._number_templ.png', 'date_templ_path': '/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/Naughton Energy Corp._date_templ.png', 'total_templ_path': '/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/Naughton Energy Corp._total_templ.png', 'number_right_offset': 168, 'number_down_offset': 0, 'date_right_offset': 179, 'date_down_offset': 0, 'total_right_offset': 252, 'total_down_offset': 0, 'number_info_x_size': 135, 'number_info_y_size': 29, 'date_info_x_size': 128, 'date_info_y_size': 31, 'total_info_x_size': 148, 'total_info_y_size': 29}"""

master_vendor_dictionary['Naughton Energy Corp.'] = {'vendor': 'Naughton Energy Corp.', 'number_templ_path': '/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/Naughton Energy Corp._number_templ.png', 'date_templ_path': '/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/Naughton Energy Corp._date_templ.png', 'total_templ_path': '/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/Naughton Energy Corp._total_templ.png', 'number_right_offset': 177, 'number_down_offset': -2, 'date_right_offset': 150, 'date_down_offset': -1, 'total_right_offset': 238, 'total_down_offset': 9, 'number_info_x_size': 122, 'number_info_y_size': 34, 'date_info_x_size': 124, 'date_info_y_size': 33, 'total_info_x_size': 150, 'total_info_y_size': 27}


"""master_vendor_dictionary['Quill.com'] = {'vendor': 'Quill.com', 'number_templ_path': '/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/Quill.com_number_templ.png', 'date_templ_path': '/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/Quill.com_date_templ.png', 'total_templ_path': '/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/Quill.com_total_templ.png', 'number_right_offset': 125, 'number_down_offset': 0, 'date_right_offset': 172, 'date_down_offset': 0, 'total_right_offset': 216, 'total_down_offset': 0, 'number_info_x_size': 117, 'number_info_y_size': 28, 'date_info_x_size': 149, 'date_info_y_size': 30, 'total_info_x_size': 183, 'total_info_y_size': 34}"""

master_vendor_dictionary['Quill.com'] = {'vendor': 'Quill.com', 'number_templ_path': '/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/Quill.com_number_templ.png', 'date_templ_path': '/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/Quill.com_date_templ.png', 'total_templ_path': '/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/Quill.com_total_templ.png', 'number_right_offset': 129, 'number_down_offset': 4, 'date_right_offset': 170, 'date_down_offset': 1, 'total_right_offset': 214, 'total_down_offset': 4, 'number_info_x_size': 123, 'number_info_y_size': 32, 'date_info_x_size': 154, 'date_info_y_size': 36, 'total_info_x_size': 183, 'total_info_y_size': 38}

"""master_vendor_dictionary['Staples'] = {'vendor': 'Staples',
 'number_templ_path': '/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/Staples_number_templ.png',
 'date_templ_path': '/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/Staples_date_templ.png',
 'total_templ_path': '/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/Staples_total_templ.png',
 'number_right_offset': 179,
 'number_down_offset': 0,
 'date_right_offset': 0,
 'date_down_offset': 43,
 'total_right_offset': 280,
 'total_down_offset': 0,
 'number_info_x_size': 121,
 'number_info_y_size': 21,
 'date_info_x_size': 185,
 'date_info_y_size': 27,
 'total_info_x_size': 155,
 'total_info_y_size': 21}"""

master_vendor_dictionary['Staples'] = {'vendor': 'Staples', 'number_templ_path': '/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/Staples_number_templ.png', 'date_templ_path': '/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/Staples_date_templ.png', 'total_templ_path': '/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/Staples_total_templ.png', 'number_right_offset': 177, 'number_down_offset': -3, 'date_right_offset': 3, 'date_down_offset': 41, 'total_right_offset': 278, 'total_down_offset': -3, 'number_info_x_size': 132, 'number_info_y_size': 26, 'date_info_x_size': 197, 'date_info_y_size': 28, 'total_info_x_size': 144, 'total_info_y_size': 22}

#----------------------------------------------------------------------------------------------------------------------------#
df = pd.read_csv('/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/testrun.csv')

for i in range(len(df['vendor'])):
#for i in range(3):


    vendor = df['vendor'][i]

    part_1 = '/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Final_Sample_Set/ROI_Testing/p'
    part_2 = df['file_name'][i]

    file_path = part_1 + part_2
    file_name = part_2

    invoice = file_path

    im = cv2.imread(invoice)

    cushion = 1
    basewidth = 750

    #----------------------------------------------------------------------------------------------------------------------------------#
    ### Invoice Number
    try:
        templ_number_part_1 = '/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/'
        templ_number_part_2 = vendor
        templ_number_part_3 = '_number_templ.png'
        templ_number_path = templ_number_part_1 + templ_number_part_2 + templ_number_part_3

        templ_number = cv2.imread(templ_number_path)


        result_number = cv2.matchTemplate(im, templ_number, cv2.TM_CCOEFF_NORMED)
        temp_tuple_number = np.unravel_index(result_number.argmax(),result_number.shape)

        r_number_final=(temp_tuple_number[1] + master_vendor_dictionary[vendor]['number_right_offset'], temp_tuple_number[0] + master_vendor_dictionary[vendor]['number_down_offset'], master_vendor_dictionary[vendor]['number_info_x_size'] + cushion, master_vendor_dictionary[vendor]['number_info_y_size'] + cushion)

        number_temp = im[int(r_number_final[1]):int(r_number_final[1]+r_number_final[3]), int(r_number_final[0]):int(r_number_final[0]+r_number_final[2])]

        img_inv_number = Image.fromarray(number_temp, 'RGB')

        # Invoice Number A-Za-z0-9


        wpercent_inv_number = (basewidth/float(img_inv_number.size[0]))
        hsize_inv_number = int((float(img_inv_number.size[1])*float(wpercent_inv_number)))
        img_inv_number = img_inv_number.resize((basewidth,hsize_inv_number), Image.ANTIALIAS)
        inv_number = pytesseract.image_to_string(img_inv_number)

        """if len(re.findall('\w+\d+\w+\d+', inv_number)) == 0:
            inv_number = ""
        else:
            inv_number = re.findall('\w+\d+\w+\d+', inv_number)[0]"""

        #inv_number  = pytesseract.image_to_string(Image.fromarray(number_temp, 'RGB'))

    except cv2.error as e:
        continue

    #----------------------------------------------------------------------------------------------------------------------------------#
    ### Invoice Date
    try:
        templ_date_part_1 = '/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/'
        templ_date_part_2 = vendor
        templ_date_part_3 = '_date_templ.png'
        templ_date_path = templ_date_part_1 + templ_date_part_2 + templ_date_part_3

        templ_date = cv2.imread(templ_date_path)


        result_date = cv2.matchTemplate(im, templ_date, cv2.TM_CCOEFF_NORMED)
        temp_tuple_date = np.unravel_index(result_date.argmax(),result_date.shape)

        r_date_final=(temp_tuple_date[1] + master_vendor_dictionary[vendor]['date_right_offset'], temp_tuple_date[0] + master_vendor_dictionary[vendor]['date_down_offset'], master_vendor_dictionary[vendor]['date_info_x_size'] + cushion, master_vendor_dictionary[vendor]['date_info_y_size'] + cushion)

        date_temp = im[int(r_date_final[1]):int(r_date_final[1]+r_date_final[3]), int(r_date_final[0]):int(r_date_final[0]+r_date_final[2])]

        #inv_date  = pytesseract.image_to_string(Image.fromarray(date_temp, 'RGB'))
        img_inv_date = Image.fromarray(date_temp, 'RGB')

        # Invoice Date


        wpercent_inv_date = (basewidth/float(img_inv_date.size[0]))
        hsize_inv_date = int((float(img_inv_date.size[1])*float(wpercent_inv_date)))
        img_inv_date = img_inv_date.resize((basewidth,hsize_inv_date), Image.ANTIALIAS)
        inv_date = pytesseract.image_to_string(img_inv_date)

    except cv2.error as e:
        continue


    #----------------------------------------------------------------------------------------------------------------------------------#
    ### Invoice Total
    try:
        templ_total_part_1 = '/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/'
        templ_total_part_2 = vendor
        templ_total_part_3 = '_total_templ.png'
        templ_total_path = templ_total_part_1 + templ_total_part_2 + templ_total_part_3

        templ_total = cv2.imread(templ_total_path)


        result_total = cv2.matchTemplate(im, templ_total, cv2.TM_CCOEFF_NORMED)
        temp_tuple_total = np.unravel_index(result_total.argmax(),result_total.shape)

        r_total_final=(temp_tuple_total[1] + master_vendor_dictionary[vendor]['total_right_offset'], temp_tuple_total[0] + master_vendor_dictionary[vendor]['total_down_offset'], master_vendor_dictionary[vendor]['total_info_x_size'] + cushion, master_vendor_dictionary[vendor]['total_info_y_size'] + cushion)

        total_temp = im[int(r_total_final[1]):int(r_total_final[1]+r_total_final[3]), int(r_total_final[0]):int(r_total_final[0]+r_total_final[2])]

        #inv_total = pytesseract.image_to_string(Image.fromarray(total_temp, 'RGB'))
        img_inv_total = Image.fromarray(total_temp, 'RGB')

        """img_inv_total = img_inv_total.filter(ImageFilter.MedianFilter())
        #img_inv_total = img_inv_total.filter(ImageFilter.BLUR)
        enhancer = ImageEnhance.Contrast(img_inv_total)
        img_inv_total = enhancer.enhance(3)
        img_inv_total = img_inv_total.convert('1')"""


        #cv2.imwrite('/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Total_Info_Capture/' + vendor + df['file_name'][i] + '_total_info.png', total_temp)
        # Invoice Total


        wpercent_inv_total = (basewidth/float(img_inv_total.size[0]))
        hsize_inv_total = int((float(img_inv_total.size[1])*float(wpercent_inv_total)))
        img_inv_total = img_inv_total.resize((basewidth,hsize_inv_total), Image.ANTIALIAS)
        inv_total = pytesseract.image_to_string(img_inv_total)

        """if len(re.findall('\-?\(?\d+.\d+\)?', inv_total)) == 0:
            inv_total = ""
        else:
            inv_total = re.findall('\-?\(?\d+.\d+\)?', inv_total)[0]"""

    except cv2.error as e:
        continue


    #---------------------------------------

    df['Invoice Number'][i] = inv_number
    df['Invoice Date'][i]   = inv_date
    df['Invoice Total'][i]  = inv_total

    #cv2.imshow('image', number_temp)
    #cv2.imwrite('GUAJIRO.png', number_temp)
    #print(inv_number, inv_date, inv_total)
    #cv2.selectROI(number_temp)
    cv2.waitKey(5)

df.to_csv('FINAL_FROM_TEST_9.csv', sep=',', index=False)
