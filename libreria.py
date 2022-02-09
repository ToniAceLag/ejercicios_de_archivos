MSG_ID="Insert the student ID: "
MSG_SN="Insert the student name: "
MSG_SR="Insert the student surname: "
MSG_CR="Insert the student course: "
FILE_NAME_COUNT="."
TXT_FILE=".txt"
def valid_filename(txt_input):
    file_name = input(txt_input)
    if file_name.count(FILE_NAME_COUNT) != 1:
        file_name = file_name+TXT_FILE
    return file_name


def valid(num):
    num_regs = int(input(num))
    while num_regs<1:
        num_regs = int(input(num))
    return num_regs


def alumnos(file_name, num_regs):
    f = open("file/"+file_name, "a")
    numb = 1
    for i in range(num_regs):
        student_id = int(input(MSG_ID))
        student_name = input(MSG_SN)
        surname = input(MSG_SR)
        course = input(MSG_CR)
        student = {
            "Student_ID": student_id,
            "Student_Name": student_name,
            "Surname": surname,
            "Course": course
        }
        if numb == 1:
            f.write("  |"+"ID"+"|"+"Student Name"+" |"+"Course"+"|"+"\n")
        f.write(str(numb)+"."+"|"+str(student["Student_ID"]) + "|" + str(student["Student_Name"]) + " " + str(student["Surname"]) + "|" + str(student["Course"]+"|"+"\n"))
        numb += 1
    f.close()