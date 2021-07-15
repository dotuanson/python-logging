import logging


# =======================================================================================
# SYNOPSIS
#    '%([PARAMETERS])[TYPE]'
# PARAMETERS
#    levelname: Tên mức
#    filename: Tên file đang thực thi
#    funcName: Tên hàm
#    lineno: Dòng gọi logging
#    messsage: Thông điệp truyền vào
#    asctime: Thời gian thực thi
# TYPE
#    d: integer
#    s: string
#    f: float
# =======================================================================================

def main():
    NEW_FORMAT = '[%(asctime)s] - [%(levelname)s] - %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=NEW_FORMAT)

    # Testingggggg!!!!!!
    logging.debug("This is a debug message!")
    logging.info("This is an info message!")
    logging.warning("This is a warning message!")


if __name__ == '__main__':
    main()
