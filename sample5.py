import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as ttkfont
import os
import re

main_window = tk.Tk()
main_window.geometry("1400x900")
main_window.title("GUI APPLICATION")

# creating frames for the main window
frame_one = ttk.Frame(main_window)
frame_two = ttk.Frame(main_window)
frame_three = ttk.Frame(main_window)
frame_four = ttk.Frame(main_window)
frame_five = ttk.Frame(main_window)
listbox_frame = ttk.Frame(main_window)
txt_file_name = "\\run.log.txt"

warning_window_dictionary = {
    "shelf_entry": "Shelf Entry!!!",
    "test_entry": "Testcase name!!!",
    "test_search": "Search not Entered",
    "notest": "No Testcase is Found!!!",
    "none_search": "No Testcases are found!!!"
}


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


def find_test_list():
    test_list = []
    for root, dirs, files in os.walk('.//RUN_PATH/PRAVEEN'):
        for dir_name in dirs:
            test_list.append(dir_name)
    return test_list


def find_file_path(test_case_name):
    flag = 0
    path = ""
    for root, dirs, files in os.walk('.'):
        for dir_name in dirs:
            if dir_name == test_case_name:
                flag = 1
                path = os.path.join(root, dir_name)
    if flag != 1:
        print("File not found")
        return ""
    else:
        return path


widget_style = ttk.Style()
widget_style.configure("TLabel", font=('courier', 13))
widget_style.configure("TButton", font=('courier', 13))
widget_style.configure("TCombobox", font=('courier', 13))
combobox_font = ttkfont.Font(family="courier", size=13)
main_window.option_add("*TCombobox*Listbox*Font", combobox_font)

frame_one.place(x=100, y=100)
shelf_label = ttk.Label(frame_one, text="Shelf No", width=18)
shelf_entry_var = tk.StringVar()
shelf_entry = ttk.Entry(frame_one, textvariable=shelf_entry_var, font=('courier', 13), width=15)
submit_button = ttk.Button(frame_one, text="Submit", width=15)
frame_one_status_label = ttk.Label(frame_one, width=15)

# adding widgets to frame one
frame_one_index = 0
for widget in frame_one.winfo_children():
    widget.grid(row=0, column=frame_one_index, padx=15, pady=0)
    frame_one_index += 1

# creating widgets for frame two
frame_two.place(x=100, y=160)
item_selected = tk.StringVar()
test_case_label = ttk.Label(frame_two, width=18, text="Testcase List")
test_case_combobox = ttk.Combobox(frame_two, width=15, textvariable=item_selected, values=find_test_list(),
                                  font=combobox_font)
wildcard_search_test_entry_var = tk.StringVar()
wildcard_search_test_entry = ttk.Entry(frame_two, textvariable=wildcard_search_test_entry_var, font=("courier", 13),
                                       width=15)
search_button = ttk.Button(frame_two, text="Search", width=15)
clear_button = ttk.Button(frame_two, text="Clear", width=10)


# adding widgets to frame one
frame_two_index = 0
for widget in frame_two.winfo_children():
    widget.grid(row=0, column=frame_two_index, padx=15, pady=0)
    frame_two_index += 1

wildcard_search_test_entry.grid(padx=5)

# creating widgets for middle frame
frame_three.place(x=100, y=220)
testcase_label = ttk.Label(frame_three, text="TestCase", width=18)
test_entry_var = tk.StringVar()
testcase_entry = ttk.Entry(frame_three, textvariable=test_entry_var, width=15, font=('courier', 13))
run_button = ttk.Button(frame_three, text="Run", width=15)
frame_three_status_label = ttk.Label(frame_three, width=15)

# adding widgets to the middle frame
frame_three_index = 0
for widget in frame_three.winfo_children():
    widget.grid(row=0, column=frame_three_index, padx=15, pady=0)
    frame_three_index += 1

listbox_frame.place(x=1000, y=160)
search_list_listbox = tk.Listbox(listbox_frame, font=combobox_font, width=20, height=10)
search_list_scrollbar = ttk.Scrollbar(listbox_frame)
select_button = ttk.Button(listbox_frame, text="Select", width=20)
search_list_listbox.grid(row=0, column=0)
search_list_scrollbar.grid(row=0, column=1, sticky="NS")
select_button.grid(row=1, column=0, padx=0, pady=5)
search_list_listbox.config(yscrollcommand=search_list_scrollbar.set)
search_list_scrollbar.config(command=search_list_listbox.yview)

frame_four.place(x=100, y=280)
log_file_label = ttk.Label(frame_four, text="Log File", width=18)
log_file_entry_var = tk.StringVar()
log_file_entry = ttk.Entry(frame_four, textvariable=log_file_entry_var, width=15, font=('courier', 13))
open_log_button = ttk.Button(frame_four, text="Open", width=15)

# adding widgets to frame four
frame_four_index = 0
for widget in frame_four.winfo_children():
    widget.grid(row=0, column=frame_four_index, padx=15, pady=0)
    frame_four_index += 1


frame_five.place(x=100, y=340)
wave_form_label = ttk.Label(frame_five, text="Wave Form", width=18)
wave_form_entry_var = tk.StringVar()
wave_form_entry = ttk.Entry(frame_five, textvariable=wave_form_entry_var, width=15, font=('courier', 13))
open_waveform_button = ttk.Button(frame_five, text="Open", width=15)

# adding widgets to frame four
frame_five_index = 0
for widget in frame_five.winfo_children():
    widget.grid(row=0, column=frame_five_index, padx=15, pady=0)
    frame_five_index += 1


def warning_window_display(root_window_object, warning_str):
    warning_window = tk.Toplevel(root_window_object)  # displaying warning window if file no not entered
    warning_window.title("Warning!!!")
    warning_window.geometry("400x200")
    warning_window_label = ttk.Label(warning_window)
    warning_window_label.place(x=120, y=50)
    warning_window_button = ttk.Button(warning_window, text="OK", width=10,
                                       command=warning_window.destroy)
    warning_window_button.place(x=120, y=120)
    for warning_key in warning_window_dictionary:
        if warning_key == warning_str:
            warning_window_label.config(text=warning_window_dictionary[warning_key])
    return root_window_object


def command_execution_submit(file_entry, path):
    if pass_in_file(path) == 1:
        frame_one_status_label.config(text="  PASS!!!", foreground="white", background="green")
    else:
        frame_one_status_label.config(text="  Fail!!!", foreground="white", background="red")


def submit_button_action(buttonevent):
    file_num = shelf_entry.get()
    if file_num == "":
        warning_window_display(main_window, "shelf_entry")
    else:
        file_path = find_file_path("test1")
        command_execution_submit(file_num, file_path)


def search_button_action(searchbuttonevent):
    search_list_listbox.delete(0, tk.END)
    temp_search_string = wildcard_search_test_entry.get()
    if temp_search_string == "":
        warning_window_display(main_window, "test_search")
    else:
        search_string = temp_search_string.strip("*") + "+"
        all_test_cases = find_test_list()
        found_list = []
        for test_case in all_test_cases:
            test_found = re.search(search_string, test_case)
            if test_found is None:
                pass
            else:
                found_list.append(test_found.string)
        if found_list:
            search_list_listbox.grid(row=0, column=0)
            index = 0
            for case in found_list:
                search_list_listbox.insert(index, case)
                index += 1
        else:
            warning_window_display(main_window, "none_search")


def combobox_action(combobox_event):
    combobox_selected = item_selected.get()
    test_entry_var.set(combobox_selected)
    log_file_entry_var.set(combobox_selected)
    wave_form_entry_var.set(combobox_selected)


def select_button_action(select_button_event):
    search_listbox_selected = search_list_listbox.get(search_list_listbox.curselection())
    test_entry_var.set(search_listbox_selected)
    log_file_entry_var.set(search_listbox_selected)
    wave_form_entry_var.set(search_listbox_selected)


def command_execution_run(path):
    if pass_in_file(path) == 1:
        main_window.after(1000)
        frame_three_status_label.config(text="   Pass!!!", foreground="white", background="green")
    else:
        main_window.after(1000)
        frame_three_status_label.config(text="   Fail!!!", foreground="white", background="red")


def run_button_action(button_event):
    test_case = testcase_entry.get()
    if test_case == "":
        warning_window_display(main_window, "test_entry")
    else:
        file_path = find_file_path(test_case)
        if file_path == "":
            warning_window_display(main_window, "notest")
        else:
            frame_three_status_label.config(text="   In Progress!!!", foreground="white", background="blue")
            main_window.update_idletasks()
            command_execution_run(file_path)


def clear_button_action(clear_button_event):
    test_entry_var.set("")
    log_file_entry_var.set("")
    wave_form_entry_var.set("")
    frame_one_status_label.config(text="", foreground="", background="")
    frame_three_status_label.config(text="", foreground="", background="")
    search_list_listbox.delete(0, tk.END)
    test_case_combobox.set("")
    wildcard_search_test_entry_var.set("")
    shelf_entry_var.set("")


def open_log_button_action(open_log_event):
    print("in open log")


def open_waveform_button_action(open_wave_event):
    print("In open Wave form")


submit_button.bind("<Button>", submit_button_action)
search_button.bind("<Button>", search_button_action)
test_case_combobox.bind("<<ComboboxSelected>>", combobox_action)
select_button.bind("<Button>", select_button_action)
run_button.bind("<Button>", run_button_action)
clear_button.bind("<Button>", clear_button_action)
open_log_button.bind("<Button>", open_log_button_action)
open_waveform_button.bind("<Button>", open_waveform_button_action)

main_window.mainloop()

