import os
import shutil
import time

def name():
    deletedFolderCount = 0
    deletedFileCount = 0

    path = "/Users/kritvikalani/Desktop/k"
    days = 30
    sec = time.time() - (days*24*60*60)

    if os.path.exists(path):
        for root_folder, folders, files in os.walk(path):
            if sec >= get_file_or_folder_age(root_folder):
                remove_folder(root_folder)
                deletedFolderCount += 1
                break;

            else:
                for folder in folders:
                    folder_path = os.path.join(root_folder, folder)

                    if sec >= get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deletedFolderCount += 1
                    
                for file in files:
                    file_path = os.path.join(root_folder, file)

                    if sec >= get_file_or_folder_age(file_path):
                        remove_file(file_path)
                        deletedFileCount += 1

        else:
            if sec >= get_file_or_folder_age(path):
                remove_file(path)
                deletedFileCount += 1

    else:
        print('"{path}" is not found')
        deletedFileCount += 1
    
    print("Total folders deleted: " + deletedFolderCount)
    print("Total folders deleted: " + deletedFileCount)

def remove_folder(path):
    if not shutil.rmtree(path):
        print("{path} is removed successfully")
    else:
        print("Unable to delete" + {path})

def remove_file(path):
    if not os.remove(path):
        print("{path} is removed successfully")
    else:
        print("Unable to delete" + {path})

def get_file_or_folder_age(path):
    ctime = os.stat(path).st_ctime
    return ctime;

if __name__ = '__main__':
    main();