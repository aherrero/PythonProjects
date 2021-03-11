import os       # Needed for OS operations (list files, mkdir...)
import shutil   # Needed to copy files

from datetime import datetime, timedelta


# Constant
FORMAT_JPG = '.JPG'
FORMAT_RAW = '.ARW'
DEBUG_LOG = True

# User Inputs
event_name = input ("Enter an Event Name: ")
initial_date_str = input ("Initial Date (Format dd-mm-yyyy). ")
end_date_str = input ("End Date (Format dd-mm-yyyy). Enter for today's date. 'n' for up to next event. ")

# Variables
input_pictures = 'D:/DCIM/100MSDCF/'    # D:/DCIM/100MSDCF/  # C:/Users/aleja/Scripts/100MSDCF/
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
    next_event = False
    initial_date = datetime.strptime(initial_date_str, '%d-%m-%Y')
    if not end_date_str:
        end_date = datetime.today()
    elif 'n' in end_date_str.lower():
        end_date = datetime.today() # Max end date, but won't be use
        next_event = True
    else:
        end_date = datetime.strptime(end_date_str, '%d-%m-%Y')

    # Filter unique name and datetime
    files_filtered = []
    datetime_folder_name = ''
    first_file_mod_time = ''
    for file in files:
        if FORMAT_JPG in file:
            # file no extension (jpg and arw)
            file_noext = file.replace(FORMAT_JPG, '')
            
            # Get File modification datetime
            file_mod_time = datetime.fromtimestamp(os.stat(input_pictures + file).st_mtime)
            if not first_file_mod_time:
                first_file_mod_time = file_mod_time

            # Get datetime once for the folder name (From the first file)
            if not datetime_folder_name:
                datetime_folder_name = file_mod_time.date()

            # Check if end date up to the next event, or end_date defined           ## TODO VERIFY IF WORKING
            # if next_event:
            #     if first_file_mod_time.date() is not file_mod_time.date():
            #         print(first_file_mod_time)
            #         print(file_mod_time)
            #         print(first_file_mod_time.date())
            #         print(file_mod_time.date())
            #         # Means we are already in the next datetime event, so, break
            #         break
            
            # Compare this datetime with input
            if (file_mod_time - initial_date >= timedelta(minutes=0)) and (end_date - file_mod_time >= timedelta(minutes=0)):
                files_filtered.append(file_noext)
                if DEBUG_LOG:
                    print(file_noext, file_mod_time)
    
    # Ask user if continue
    user_continue = input (str(len(files_filtered)) + ' files will be copied. Do you want to continue? Yes (Default) / No : ')
    if 'yes' in user_continue.lower() or not user_continue:
        if DEBUG_LOG:
            print('Continue.')
    else:
        print("Cancel by user.")
        return False

    # Output directories with datetime
    folder_name = datetime_folder_name + ' ' + event_name
    output_pictures = output_default + folder_name + '/'
    output_pictures_jpg = output_pictures + folder_name + '/'
    output_pictures_raw = output_pictures + folder_name + ' ' + 'RAW' + '/'
    output_pictures_archives = output_default + 'Archives/' + folder_name + '/'

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
        shutil.copy2(file_name_complete + FORMAT_JPG, output_pictures_jpg + file + '_' + filename_suffix_event_name + FORMAT_JPG)
        if os.path.isfile(file_name_complete + FORMAT_RAW):
            shutil.copy2(file_name_complete + FORMAT_RAW, output_pictures_raw + file + '_' + filename_suffix_event_name + FORMAT_RAW)
        else:
            print('File RAW not found : ' + file + FORMAT_RAW)
        
    
    # Ask user if move files
    user_continue = input ('Do you want to remove the files from SD Card? Yes / No : ')
    if 'yes' in user_continue.lower():
        # Mkdir Archives folder
        if os.path.isdir(output_pictures_archives):
            print(output_pictures_archives + ' : Output folder already exists')
            return False
        os.mkdir(output_pictures_archives)

        # Move files
        for file in files_filtered:
            file_name_complete = input_pictures + file
            shutil.move(file_name_complete + FORMAT_JPG, output_pictures_archives + file + FORMAT_JPG)
            if os.path.isfile(file_name_complete + FORMAT_RAW):
                shutil.move(file_name_complete + FORMAT_RAW, output_pictures_archives + file + FORMAT_RAW)
            
    else:
        print("Cancel remove from source by the user")

    return True

def main():
    err = process()
    if err == False:
        print('Error!')
        return False
    print('Done.')

if __name__ == "__main__":
    main()
