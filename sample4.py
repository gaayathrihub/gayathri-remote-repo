import os


txt_file_name = "\\run.log.txt"


# *************************** finding the test case list for .//RUN_PATH/PRAVEEN *******************
def find_test_list():
    test_list = []
    for root, dirs, files in os.walk('.//RUN_PATH/PRAVEEN'):
        for dir_name in dirs:
            test_list.append(dir_name)
    return test_list


# **************************** finding file path of the given test case name*********************
def find_file_path(test_case_name):
    flag = 0
    path = ""
    for root, dirs, files in os.walk('.'):
        for dir_name in dirs:
            if dir_name == test_case_name:
                flag = 1
                path = os.path.join(root, dir_name)
    if flag:
        return path
    else:
        return ""


# ************************************** Checking the file for "pass" ****************************
def pass_in_file(path_of_file):
    flag_file_found = 0
    filename = open(path_of_file + txt_file_name, "r+")
    for line in filename:
        data = line.split()
        for item in data:
            if item == "pass":
                flag_file_found = 1
            break
    filename.close()
    return flag_file_found


