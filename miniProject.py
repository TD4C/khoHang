
kho = []
doanh_thu = 0


def nhap_hang():
    ma = input("Nhập mã sản phẩm: ")
    ten = input("Nhập tên sản phẩm: ")
    gia = float(input("Nhập giá: "))
    so_luong = int(input("Nhập số lượng: "))

    san_pham = {
        "ma": ma,
        "ten": ten,
        "gia": gia,
        "so_luong": so_luong
    }

    kho.append(san_pham)
    print("Đã thêm sản phẩm vào kho")

def ban_hang():
    global doanh_thu
    ma = input("Nhập mã sản phẩm cần bán: ")
    sl_ban = int(input("Nhập số lượng bán: "))

    for sp in kho:
        if sp["ma"] == ma:
            if sp["so_luong"] >= sl_ban:
                sp["so_luong"] -= sl_ban
                tien = sl_ban * sp["gia"]
                doanh_thu += tien
                print("Bán thành công, thu:", tien)
                return
            else:
                print("Không đủ số lượng trong kho")
                return

    print("Không tìm thấy sản phẩm")


def tim_kiem():
    ten = input("Nhập tên sản phẩm cần tìm: ")

    tim_thay = False
    for sp in kho:
        if ten.lower() in sp["ten"].lower():
            print(sp)
            tim_thay = True

    if not tim_thay:
        print("Không tìm thấy sản phẩm")


# ------------------------------
# Thống kê doanh thu
# ------------------------------
def thong_ke():
    print("Tổng doanh thu:", doanh_thu)


# ==============================
# MENU CHÍNH
# ==============================
while True:
    print("\n===== MENU QUẢN LÝ KHO =====")
    print("1. Nhập hàng")
    print("2. Bán hàng")
    print("3. Tìm kiếm sản phẩm")
    print("4. Thống kê doanh thu")
    print("0. Thoát")

    chon = input("Chọn chức năng: ")

    if chon == "1":
        nhap_hang()
    elif chon == "2":
        ban_hang()
    elif chon == "3":
        tim_kiem()
    elif chon == "4":
        thong_ke()
    elif chon == "0":
        print("Thoát chương trình")
        break
    else:
        print("Lựa chọn không hợp lệ")
