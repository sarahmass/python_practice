'''
    CS50p Week1 problemset 1: file extensions
    In a file called extensions.py, implement a program that prompts the user for the name of a file
    and then outputs that file's media type if the file's name ends, case-insensitively, in any of these suffixes:

        .gif --> image/gif
        .jpg --> image/jpg
        .jpeg --> image/jpeg
        .png --> image/png
        .pdf --> application/pdf
        .txt --> text/plain
        .zip --> application/zip
    If the file's name ends with some other suffix or has no suffix at all, output application/octet-stream instead,
    which is a common default.
'''

def main():
    file_name = input("Enter your file name: ").lower().strip()
    extension = get_extension(file_name)
    media_type = get_media_type(extension)
    print(media_type, end='')

def get_extension(name):
    ''' name(str): name of file
        return(str): file extension if provided else "no extension"
    '''
    # check if an extension is provided and return it
    if "." in name:
        name_split = name.split('.')
        extension = name_split[-1]
        return extension
    else:
        return "no extension"

def get_media_type(ext):
    '''
        input(str) file extention
        return(str) media type or application/octet-stream as default
    '''
    match ext:
        case "gif":
            return "image/gif"
        case "jpg" | "jpeg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "application/zip"
        case _:
            return "application/octet-stream"

main()