## 1. Vì sao cần sử dụng log?
* Thông thường khi chúng ta muốn quan sát những gì đang xảy ra bên trong chương trình, thói quen của nhiều người
mới học Python kể cả mình đó chính là sử dụng hàm `print()` để in lên terminal. Thay vào đó thì ở trong bài viết 
này tôi sẽ chỉ cho các bạn cách để một chương trình vừa chạy vừa có thể ghi log (Dưới dạng file hoặc terminal)
giúp cho việc theo dõi lịch sử của chương trình rõ ràng hơn. 

## 2. Làm sao sử dụng log trong python?
* Python có thư viện chuẩn hỗ trợ cho viết ghi log là `logging`. Thư viện viết theo hướng `multithreading` nên
giảm nhẹ được khối lượng công việc cho luồng code chính của bạn rất nhiều.
  
> Tham khảo về cơ chế đa luồng: [Đa luồng trong Python (multithreading)](https://viblo.asia/p/da-luong-trong-python-multithreading-WAyK8MO6ZxX)

## 3. Có bao nhiêu log mà lập trình viên thường xài?
<center style="font-style: italic">Thứ tự quan trọng của các mức tăng dần từ trên xuống</center>

| Mức            | Nội dung |
| -----------    | ----------- |
| **DEBUG**      | Thông tin `chi tiết`, thường là thông tin để tìm lỗi.|
| **INFO**       | Thông báo `thông thường`, các thông tin in ra khi chương trình chạy theo đúng kịch bản.|
| **WARNING**    | Thông báo khi `nghi vấn` bất thường hoặc lỗi có thể xảy ra, tuy nhiên chương trình vẫn có thể hoạt động.|
| **ERROR**      | `Lỗi`, chương trình có thể không hoạt động được một số chức năng hoặc nhiệm vụ nào đó, thường thì nên dùng ghi bắt được Exception.|
| **CRITICAL**   | `Lỗi`, chương trình gặp lỗi nghiêm trọng không thể giải quyết được và bắt buộc phải dừng lại.|

## 4. Thực hành

### 4.1. Sử dụng module logging cơ bản
```python
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
```
### 4.2. Format logging cho đẹp!
```python
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
```
### 4.3. Log ra _file_ + _console_ cùng lúc 
```python
import logging

# ===============================================
#           Tạo instance logging
# ===============================================
logger = logging.getLogger()
NEW_FORMAT = '[%(asctime)s] - [%(levelname)s] - %(message)s'

# ===============================================
#       Cấu hình logger để ghi ra file
# ===============================================
file_logger = logging.FileHandler('logfile.log')
file_logger_format = logging.Formatter(NEW_FORMAT)
file_logger.setFormatter(file_logger_format)
logger.addHandler(file_logger)

# ===============================================
#       Cấu hình logger để in lên console
# ===============================================
console_logger = logging.StreamHandler()
console_logger_format = logging.Formatter(NEW_FORMAT)
console_logger.setFormatter(console_logger_format)
logger.addHandler(console_logger)

# Hiển thị các log từ DEBUG -> CRITICAL
logger.setLevel(logging.DEBUG)

# Testingggggg!!!!!!
logger.debug("This is a debug message!")
logger.info("This is an info message!")
logger.warning("This is a warning message!")
```
### 4.4. Logging trong nhiều module
```python
import logging
from Package import module

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info('Started')
    module.do_something()
    logging.info('Finished')

if __name__ == '__main__':
    main()
```
file module.py
```python
import logging

def do_something() -> None:
    logging.info('Doing something')
```

### 4.5. Logging trong exception
```python
import logging

LOGGER = logging.getLogger()  # Tạo instance logging
LOG_LEVEL = logging.DEBUG  # Level để in log


def config_file() -> None:
    """
    Cấu hình logger để in lên console
    :return: None
    """
    console_logger = logging.FileHandler('FILE_LOG.log')
    LOGGER.addHandler(console_logger)


def main():
    try:
        open('/path/to/does/not/exist.txt', 'rb')
    except Exception as e:
        LOGGER.error('Failed to open file', exc_info=False)


if __name__ == '__main__':
    config_file()
    LOGGER.setLevel(LOG_LEVEL)
    main()
```
## 5. Working tree
```
├── ./README.md
├── ./__pycache__
├── ./logfile.log
├── ./src
├── ./src/Package
│  ├── ./src/Package/__init__.py
│  ├── ./src/Package/__pycache__
│  └── ./src/Package/module.py
├── ./src/__init__.py
├── ./src/log_basic.py
├── ./src/log_exception.py
├── ./src/log_format.py
├── ./src/log_handles.py
└── ./src/log_modules.py
```
## 6. Tài liệu tham khảo
* [Documents python](https://docs.python.org/3/library/logging.html)
* [Sử dụng logging trong Python](https://cuccode.com/python_logging.html)