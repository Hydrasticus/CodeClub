# TODO: complete challenge


def sort_file(contents, insep=',', inend="\n", outsep="", outend=""):
    if outsep == "":
        outsep = insep

    if outend == "":
        outend = inend

    sorted_contents = ""

    for letter in contents:
        if letter == insep:
            sorted_contents += outsep
        elif letter == inend:
            sorted_contents += outend
        elif letter == "":
            continue
        else:
            sorted_contents += letter

    print(sorted_contents)


test_string = "2,3,d\n1,4,d\n8,2,z\n2,4,x\n2,4,a,"
sort_file(test_string)
