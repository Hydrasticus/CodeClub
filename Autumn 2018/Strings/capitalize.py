def capitalizing_this(input_string):
    input_arr = str.lower(input_string)
    input_arr = str.split(input_arr, ' ')

    output_arr = []

    for word in input_arr:
        word = str.capitalize(word)
        output_arr.append(word)

    output_string = str.join(' ', output_arr)

    return output_string
