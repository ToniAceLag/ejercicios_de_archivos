import libreria as l

TXT_VALIDAR_FILENAME="Insert the file name: "
TXT_VALIDAR = "Insert the number of student you want: "


def main():
    file_name = l.valid_filename(TXT_VALIDAR_FILENAME)
    num_regs = l.valid(TXT_VALIDAR)
    l.alumnos(file_name,num_regs)

if __name__ == '__main__':
    main()
