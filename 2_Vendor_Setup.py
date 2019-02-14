import cv2
import numpy as np

#--------------------------------------------------------------------------------------------------------------------#
master_vendor_dictionary = {}

#--------------------------------------------------------------------------------------------------------------------#

def vendor_setup(invoice):
    im = cv2.imread(invoice)

    # Resize image so invoice fits on screen when displayed:
    imS = cv2.resize(im, (640, 880))

    # If invoice not recognized, show the invoice, then begin vendor setup process:

    cv2.imshow('image', imS)
    cv2.waitKey(3)

    #User prompted to enter Vendor Name
    vendor = input("Please Enter the Vendor Name:  ")
    cv2.destroyAllWindows()

    # Select Region Of Interest: Invoice Number
    r_number_templ = cv2.selectROI(im)
    r_number_info = cv2.selectROI(im)

    # Select Region Of Interest: Invoice Date
    r_date_templ = cv2.selectROI(im)
    r_date_info = cv2.selectROI(im)

    # Select Region Of Interest: Invoice Total
    r_total_templ = cv2.selectROI(im)
    r_total_info = cv2.selectROI(im)

    # Crop images: Invoice Number
    number_templ = im[int(r_number_templ[1]):int(r_number_templ[1]+r_number_templ[3]), int(r_number_templ[0]):int(r_number_templ[0]+r_number_templ[2])]

    number_info = im[int(r_number_info[1]):int(r_number_info[1]+r_number_info[3]), int(r_number_info[0]):int(r_number_info[0]+r_number_info[2])]


    cv2.imwrite('/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/' + vendor + '_number_templ.png', number_templ)

    number_templ_path = ('/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/' + vendor + '_number_templ.png')

    #template_number = cv2.imread(number_templ_path)

    ### Setting offsets:
    number_right_offset = r_number_info[0] - r_number_templ[0]
    number_down_offset = r_number_info[1] - r_number_templ[1]

    # if info is to the right of the templ
    """if r_number_templ[0] + 25 < r_number_info[0]:
        number_right_offset = r_number_info[0] - r_number_templ[0]
        number_down_offset = 0

    # if info is below the templ
    else:
        number_right_offset = 0
        number_down_offset = r_number_info[1] - r_number_templ[1]"""

    # Get size of info ROI:
    number_info_x_size = r_number_info[2]
    number_info_y_size = r_number_info[3]

    # Crop images: Invoice Date
    date_templ = im[int(r_date_templ[1]):int(r_date_templ[1]+r_date_templ[3]), int(r_date_templ[0]):int(r_date_templ[0]+r_date_templ[2])]

    date_info = im[int(r_date_info[1]):int(r_date_info[1]+r_date_info[3]), int(r_date_info[0]):int(r_date_info[0]+r_date_info[2])]


    cv2.imwrite('/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/' + vendor + '_date_templ.png', date_templ)

    date_templ_path = ('/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/' + vendor + '_date_templ.png')

    #template_date = cv2.imread(date_templ_path)

    ### Setting offsets:
    date_right_offset = r_date_info[0] - r_date_templ[0]
    date_down_offset = r_date_info[1] - r_date_templ[1]

    """# if info is to the right of the templ
    if r_date_templ[0] + 25 < r_date_info[0]:
        date_right_offset = r_date_info[0] - r_date_templ[0]
        date_down_offset = 0

    # if info is below the templ
    else:
        date_right_offset = 0
        date_down_offset = r_date_info[1] - r_date_templ[1]"""

    # Get size of info ROI:
    date_info_x_size = r_date_info[2]
    date_info_y_size = r_date_info[3]

    # Crop images: Invoice Total
    total_templ = im[int(r_total_templ[1]):int(r_total_templ[1]+r_total_templ[3]), int(r_total_templ[0]):int(r_total_templ[0]+r_total_templ[2])]

    total_info = im[int(r_total_info[1]):int(r_total_info[1]+r_total_info[3]), int(r_total_info[0]):int(r_total_info[0]+r_total_info[2])]


    cv2.imwrite('/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/' + vendor + '_total_templ.png', total_templ)

    total_templ_path = ('/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Templates/' + vendor + '_total_templ.png')

    #template_total = cv2.imread(total_templ_path)

    ### Setting offsets:
    total_right_offset = r_total_info[0] - r_total_templ[0]
    total_down_offset = r_total_info[1] - r_total_templ[1]

    """# if info is to the right of the templ
    if r_total_templ[0] + 25 < r_total_info[0]:
        total_right_offset = r_total_info[0] - r_total_templ[0]
        total_down_offset = 0

    # if info is below the templ
    else:
        total_right_offset = 0
        total_down_offset = r_total_info[1] - r_total_templ[1]"""

    # Get size of info ROI:
    total_info_x_size = r_total_info[2]
    total_info_y_size = r_total_info[3]

    #--------------------------------------------------------------------------------------------------------------------#

    master_vendor_dictionary[vendor] = {}
    master_vendor_dictionary[vendor]['vendor']              = vendor
    master_vendor_dictionary[vendor]['number_templ_path']   = number_templ_path
    master_vendor_dictionary[vendor]['date_templ_path']     = date_templ_path
    master_vendor_dictionary[vendor]['total_templ_path']    = total_templ_path
    master_vendor_dictionary[vendor]['number_right_offset'] = number_right_offset
    master_vendor_dictionary[vendor]['number_down_offset']  = number_down_offset
    master_vendor_dictionary[vendor]['date_right_offset']   = date_right_offset
    master_vendor_dictionary[vendor]['date_down_offset']    = date_down_offset
    master_vendor_dictionary[vendor]['total_right_offset']  = total_right_offset
    master_vendor_dictionary[vendor]['total_down_offset']   = total_down_offset
    master_vendor_dictionary[vendor]['number_info_x_size']  = number_info_x_size
    master_vendor_dictionary[vendor]['number_info_y_size']  = number_info_y_size
    master_vendor_dictionary[vendor]['date_info_x_size']    = date_info_x_size
    master_vendor_dictionary[vendor]['date_info_y_size']    = date_info_y_size
    master_vendor_dictionary[vendor]['total_info_x_size']   = total_info_x_size
    master_vendor_dictionary[vendor]['total_info_y_size']   = total_info_y_size

    print(master_vendor_dictionary)


invoice = ('/Users/KevinWAguiar/Desktop/GA_DSI/Capstone_Project/Final_Sample_Set/ROI_Testing/p45-1.png')

vendor_setup(invoice)
