import os       # Needed for OS operations (list files, mkdir...)
import shutil   # Needed to copy files

from datetime import datetime, timedelta


# Constant
FORMAT_JPG = '.JPG'
FORMAT_RAW = '.ARW'
DEBUG_LOG = True

# User Inputs
folder_name = input ("Enter an Event Name: ")
initial_date_str = input ("Initial Date (Format dd-mm-yyyy). ")
end_date_str = input ("End Date (Format dd-mm-yyyy). Enter for today's date. ")

# Variables
input_pictures = 'C:/Users/aleja/Scripts/100MSDCF/'
output_default = os.path.expanduser("~") + '/Pictures/' # By default, home directoy + Pictures

def process():
    # Get files from input folder
    if os.path.isdir(input_pictures):
        files = os.listdir(input_pictures)
    else:
        print(input_pictures + ' is not a directory!')
        return False

    # Check any
    if len(files) <= 0:
        print('No files found in ' + input_pictures)
        return False

    # Convert data desired
    initial_date = datetime.strptime(initial_date_str, '%d-%m-%Y')
    if not end_date_str:
        end_date = datetime.today()
    else:
        end_date = datetime.strptime(end_date_str, '%d-%m-%Y')

    # Filter unique name and datetime
    files_filtered = []
    datetime_folder_name = ''
    for file in files:
        if FORMAT_JPG in file:
            # file no extension (jpg and arw)
            file_noext = file.replace(FORMAT_JPG, '')
            
            # Get File modification datetime
            file_mod_time = datetime.fromtimestamp(os.stat(input_pictures + file).st_mtime)

            # Get datetime once for the folder name
            if not datetime_folder_name:
                datetime_folder_name = str(file_mod_time.year) + '-' + str(file_mod_time.month) + '-' + str(file_mod_time.day)

            # Compare this datetime with input
            if (file_mod_time - initial_date >= timedelta(minutes=0)) and (end_date - file_mod_time >= timedelta(minutes=0)):
                files_filtered.append(file_noext)
                if DEBUG_LOG:
                    print(file_noext, file_mod_time)
    
    # Ask user if continue
    user_continue = input (str(len(files_filtered)) + ' files will be copied. Do you want to continue? Yes (Default) / No : ')
    if 'no' in user_continue.lower():
        print("Cancel by user")
        return False

    # Output directories with datetime
    output_pictures = output_default + datetime_folder_name + ' ' + folder_name + '/'
    output_pictures_jpg = output_pictures + folder_name + '/'
    output_pictures_raw = output_pictures + folder_name + ' ' + 'RAW' + '/'

    # Mkdir output folder
    if not os.path.isdir(output_default):
        print('Something wrong getting home directory')

    if os.path.isdir(output_pictures) or os.path.isdir(output_pictures_jpg) or os.path.isdir(output_pictures_raw):
        print('Output folder already exists')
        return False
    os.mkdir(output_pictures)
    os.mkdir(output_pictures_jpg)
    os.mkdir(output_pictures_raw)

    # Files names, remove spaces
    filename_suffix_event_name = folder_name.replace(' ', '')

    # Copy Pictures
    for file in files_filtered:
        file_name_complete = input_pictures + file
        shutil.copy2(file_name_complete + FORMAT_RAW, output_pictures_raw + file + '_' + filename_suffix_event_name + FORMAT_RAW)
        shutil.copy2(file_name_complete + FORMAT_JPG, output_pictures_jpg + file + '_' + filename_suffix_event_name + FORMAT_JPG)

    return True

def main():
    err = process()
    if err == False:
        print('Error!')
        return False
    print('Done.')

if __name__ == "__main__":
    main()
