import logging


# ====================================================================================================================
#                                           In ra terminal hay ghi ra file?
# logging.basicConfig(level=logging.DEBUG) # In log ra terminal
# logging.basicConfig(filename='logfile.log', level=logging.DEBUG) # Ghi log ra file, log sẽ ghi tiếp các từ trước đó
# logging.basicConfig(filename='logfile.log', level=logging.DEBUG, filemode='w') # Ghi log ra file, log sẽ ghi đè file
# ====================================================================================================================

def main():
    logging.basicConfig(level=logging.INFO)  # Hiển thị các log từ INFO -> CRITICAL

    try:
        logging.info('Trying to open the file')
        filePointer = open('appFile.txt', 'r')
        try:
            logging.info('Trying to read the file content')
            content = filePointer.readline()
        finally:
            filePointer.close()
    except IOError as e:
        logging.error('Error occurred ' + str(e))


if __name__ == '__main__':
    main()
