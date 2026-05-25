print("--- HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN ---")
name_patient = input("Nhập tên bệnh nhân : ")

# Ép kiểu dữ liệu từ str sang float để có thể tính toán
weight = float(input("Nhập cân nặng bệnh nhân (kg) : "))

print("\n--- KIỂM TRA DỮ LIỆU LƯU TRỮ ---")
print("Bệnh nhân : ", name_patient)
print("Cân nặng đã nhập : ", weight)

# Kiểm tra lại kiểu dữ liệu
print("CẢNH BÁO - Kiểu dữ liệu đang lưu là : ", type(weight))

# Thử tính toán demo (ví dụ chia đôi cân nặng)
print("Cân nặng sau khi chia đôi là:", weight / 2)