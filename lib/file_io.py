def write_file(file_name, file_content):
    with open('file_name.txt', mode='w') as file:
        file.write(file_content)
        
    # with open(file_name, 'w') as file:
    #     file.write(file_content)


def append_file(file_name, append_content):
    pass

def read_file(file_name):
    with open(f'{file_name}.txt' , mode = 'r') as file:
        content = file.read()
    return content


# text_file = open("file_nam", "mode")
# contents = read(text_file)
# print(contents)


