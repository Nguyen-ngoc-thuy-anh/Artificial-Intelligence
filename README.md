ĐỒ ÁN SỬ DỤNG THUẬT TOÁN THAM LAM (GREEDY ALGORITHM) ĐỂ GIẢI QUYẾT BÀI TOÁN FRACTIONAL KNAPSACK (BÀI TOÁN CÁI TÚI DẠNG PHÂN SỐ)
Giới Thiệu
Nội dung đồ án này đưa ra một triển khai của bài toán Knapsack Phân Số sử dụng thuật toán Tham Lam. Đồ án cũng bao gồm một giao diện thân thiện với người dùng được xây dựng bằng PyQt6 để cho phép người dùng nhập các tham số của bài toán, thêm các đồ vật và trực quan hóa giải pháp.

Mô Tả Vấn Đề:
Bài toán Knapsack Phân Số có thể được mô tả như sau:
- Đầu vào: Một tập hợp các đồ vật, mỗi đồ vậtg có trọng lượng và giá trị, và một trọng lượng tối đa cho túi.
- Đầu ra: Lựa chọn tối ưu các phần của đồ vật để bỏ vào trong túi sao cho tổng trọng lượng không vượt quá khả năng chứa và tổng giá trị được tối đa hóa.
Khác với bài toán cái túi dạng 0/1, các đồ vật có thể bị chia nhỏ thành các phần nhỏ hơn và bất kỳ phần nào của một đồ vật cũng có thể được bao gồm trong túi.

Phương Pháp:
Đồ án này sử dụng Thuật Toán Tham Lam để giải quyết bài toán Fractional Knapsack (Bài toán cái túi dạng phân số). Các bước như sau:
- Tính đơn giá bằng cách lấy tỷ lệ giá trị trên trọng lượng cho mỗi đồ vật.
- Sắp xếp các đồ vật theo tỷ lệ này theo thứ tự giảm dần.
- Bắt đầu bỏ các đồ vật vào túi từ tỷ lệ cao nhất cho đến khi túi đầy hoặc tất cả các đồ vật đã được xem xét.
  Nếu đồ vật tiếp theo chỉ có thể được bao gồm một phần, ta lấy phần phù hợp với trọng lượng mà túi còn có thể chứa.

Tính Năng
- Giải pháp hiệu quả nhưng đảm bảo sự tối ưu khi sử dụng Thuật Toán Tham Lam.
- Đầu ra chi tiết hiển thị các đồ vật đã chọn và các phần phân số của chúng.
- Giao diện thân thiện với người dùng được xây dựng bằng PyQt6 để nhập các tham số của bài toán và hiển thị kết quả.
- Khả năng thêm và xóa các đồ vật một cách linh hoạt.

Các File Code
Dự án này bao gồm ba file code:
- Knapsack_Solving.py: Chứa lớp Knapsack với chức năng triển khai Thuật Toán Tham Lam.
- Knapsack_App.py: Triển khai giao diện PyQt6 để tương tác với người dùng.
- Knapsack_main.py: Đầu vào của ứng dụng.
