## 1. Vì sao cần sử dụng log?
* Đôi khi chúng ta muốn quan sát những gì đang xảy ra bên trong chương trình của chúng ta, thay vì
phải in lên terminal thì ta có thể ghi log (Dưới dạng file hoặc terminal) giúp cho việc theo dõi lịch
sử mà chương trình đã chạy. 

## 2. Làm sao sử dụng log trong python?
* Python có thư viện chuẩn hỗ trợ cho viết ghi log là `logging`. Để tận dụng hiệu quả thư viện
`logging` thì ta sẽ sử dụng thêm thư viện `threading` để chia luồng riêng cho thư viện này.
  
> Tham khảo về đa luồng: [Đa luồng trong Python (multithreading)](https://viblo.asia/p/da-luong-trong-python-multithreading-WAyK8MO6ZxX)

## 3. Có bao nhiêu log mà lập trình viên thường xài?
| Mức            | Nội dung |
| -----------    | ----------- |
| **DEBUG**      | Thông tin `chi tiết`, thường là thông tin để tìm lỗi.|
| **INFO**       | Thông báo `thông thường`, các thông tin in ra khi chương trình chạy theo đúng kịch bản.|
| **WARNING**    | Thông báo khi `nghi vấn` bất thường hoặc lỗi có thể xảy ra, tuy nhiên chương trình vẫn có thể hoạt động.|
| **ERROR**      | `Lỗi`, chương trình có thể không hoạt động được một số chức năng hoặc nhiệm vụ nào đó, thường thì nên dùng ghi bắt được Exception.|
| **CRITICAL**   | `Lỗi`, chương trình gặp lỗi nghiêm trọng không thể giải quyết được và bắt buộc phải dừng lại.|

