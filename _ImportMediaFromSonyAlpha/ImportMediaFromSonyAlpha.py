import os       # Needed for OS operations (list files, mkdir...)
import shutil   # Needed to copy files
from datetime import datetime, timedelta, date

# Constant
FORMAT_JPG = '.JPG'
FORMAT_RAW = '.ARW'
DEBUG_LOG = True

# Variables
input_pictures = 'C:/Users/aleja/Scripts/100MSDCF/'    # D:/DCIM/100MSDCF/  # C:/Users/aleja/Scripts/100MSDCF/
output_default = os.path.expanduser("~") + '/Pictures/'                             # By default, homedirectoy + Pictures
output_default_archives = os.path.expanduser("~") + '/Pictures/' + 'Archives/'      # By default, homedirectoy + Pictures + Archives

# var video # TODO
input_video_mp4 = 'D:/PRIVATE/M4ROOT/CLIP/'
input_video_mp4_thumb = 'D:/PRIVATE/M4ROOT/THMBNL/'

def userInput():
    # User Inputs
    event_name = input ("Enter an Event Name: ")
    initial_date_str = input ("Initial Date:\n\t-> dd-mm-yyyy\n\t-> 'f' for first event.\n\t")
    end_date_str = input ("End Date:\n\t-> dd-mm-yyyy \n\t-> 'Enter' for today's date.\n\t-> 'n' for up to next event.\n\t")

    # Convert data desired
    # Initial date
    first_event = False
    if 'f' in initial_date_str.lower():
        initial_date = date.fromisoformat('2000-01-13')  #Min first date, won't be used
        first_event = True
    else:
        initial_date = datetime.strptime(initial_date_str, '%d-%m-%Y')

    # End date
    next_event = False
    if not end_date_str:
        end_date = datetime.today()
    elif 'n' in end_date_str.lower():
        end_date = datetime.today() # Max end date, but won't be used
        next_event = True
    else:
        end_date = datetime.strptime(end_date_str, '%d-%m-%Y')

    return event_name, initial_date, end_date, first_event, next_event

def filterMedia(Files, InputMedia, InitialDate, EndDate, FirstEvent, NextEvent):
    # Filter unique name and datetime
    files_filtered = []
    datetime_folder_name = ''
    first_file_mod_time = ''
    for file in Files:
        if FORMAT_JPG in file:
            # file no extension (jpg and arw)
            file_noext = file.replace(FORMAT_JPG, '')
            
            # Get File modification datetime
            file_mod_time = datetime.fromtimestamp(os.stat(InputMedia + file).st_mtime)
            if not first_file_mod_time:
                first_file_mod_time = file_mod_time

            # Get datetime once for the folder name (From the first file)
            if not datetime_folder_name:
                datetime_folder_name = file_mod_time.date().strftime("%Y-%m-%d")
            
            # Check if first event
            if FirstEvent:
                InitialDate = first_file_mod_time

            # Check if end date up to the next event, or end_date defined
            if NextEvent:
                if first_file_mod_time.date() != file_mod_time.date():
                    # Means we are already in the next datetime event, so, break
                    break
            
            # Compare this datetime with input
            if (file_mod_time - InitialDate >= timedelta(minutes=0)) and (EndDate - file_mod_time >= timedelta(minutes=0)):
                files_filtered.append(file_noext)
                if DEBUG_LOG:
                    print(file_noext, file_mod_time)

    return files_filtered, datetime_folder_name

def process(EventName, InitialDate, EndDate, FirstEvent, NextEvent):
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

    # Filter unique name and datetime
    files_filtered, datetime_folder_name = filterMedia(files, input_pictures, InitialDate, EndDate, FirstEvent, NextEvent)
    
    # Ask user if continue
    user_continue = input (str(len(files_filtered)) + ' files will be copied. Do you want to continue? Yes (Default) / No : ')
    if 'yes' in user_continue.lower() or not user_continue:
        if DEBUG_LOG:
            print('Continue.')
    else:
        print("Cancel by user.")
        return False

    # Output directories with datetime
    folder_name = datetime_folder_name + ' ' + EventName
    output_pictures = output_default + folder_name + '/'
    output_pictures_jpg = output_pictures + folder_name + '/'
    output_pictures_raw = output_pictures + folder_name + ' ' + 'RAW' + '/'
    output_pictures_archives = output_default_archives + folder_name + '/'

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
    count_file = 0
    for file in files_filtered:
        file_name_complete = input_pictures + file
        shutil.copy2(file_name_complete + FORMAT_JPG, output_pictures_jpg + file + '_' + filename_suffix_event_name + FORMAT_JPG)
        if os.path.isfile(file_name_complete + FORMAT_RAW):
            shutil.copy2(file_name_complete + FORMAT_RAW, output_pictures_raw + file + '_' + filename_suffix_event_name + FORMAT_RAW)
        else:
            print('File RAW not found : ' + file + FORMAT_RAW)
        count_file = count_file + 1
        print(str(count_file) + ' / ' + str(len(files_filtered)) + ' : ' + file)
    
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
    event_name, initial_date, end_date, first_event, next_event = userInput()
    err = process(event_name, initial_date, end_date, first_event, next_event)
    if err == False:
        print('Error!')
        return False
    print('Done.')

if __name__ == "__main__":
    main()
