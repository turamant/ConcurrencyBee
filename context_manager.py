class File:
    def __init__(self, name_file, method):
        self.name_file = name_file
        self.method = method

    def __enter__(self):
        self.file_obj = open(self.name_file, self.method)
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()


if __name__ == '__main__':
    with File("context.txt", 'w') as file:
        file.write("hello amigo!")

    with File("context.txt", 'a') as file:
        file.write("morgen david")


    with File("context.txt", 'r') as file:
        print(file.read())

