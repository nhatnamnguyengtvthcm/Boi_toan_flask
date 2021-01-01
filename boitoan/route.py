#web tham khảo
# https://liu.com.vn/bai-viet/xem-bang-tra-cung-menh-vo-chong-co-hop-nhau-hay-khong
# https://goldviet24k.vn/cach-tinh-menh-ngu-hanh.htm

# Thu vien standard
import  math
# ThirdParty
from flask import Blueprint, jsonify, request, json,make_response
from flask import render_template
import http
# Thu vien ben trong

# Blueprint
boitoan = Blueprint("boitoan", __name__)


# làm thế nào để định nghĩa POST, GET


# app decorator
@boitoan.route('/boitoan/', methods=('GET', 'POST'))
def boi_toan():
    if request.method == 'POST':
        ret = _post_boi_toan(request)
        return ret


    elif request.method == 'GET':
        # ret = _get_boi_toan(request)
        return render_template('index.html')


# Module: function noi bo nen them _(protect), __(private)
def _post_boi_toan(req):
    # Nhận thông tin năm và xử lý
    # Query Parameter
    # Body (Json) {'fun': 0, 'man_year': 0, 'woman_year': 0}
    body = req.json
    print("body = {}".format(body))

    year_of_man = body.get("man_year")
    print("year_of_man = {}".format(year_of_man))

    # nhận thông tin của nữ
    year_of_woman = body.get("woman_year")
    print("year_of_woman={}".format(year_of_woman))

    # nhận function(ngũ hành hay xem tuổi)
    fun = body.get("fun")
    if fun == 0: #coi ngũ hành
        man_can = _ngu_hanh_can(year_of_man)
        man_chi = _ngu_hanh_chi(year_of_man)
        woman_can = _ngu_hanh_can(year_of_woman)
        woman_chi = _ngu_hanh_chi(year_of_woman)
        man_menh = _ngu_hanh(man_can, man_chi)
        woman_menh = _ngu_hanh(woman_can, woman_chi)
        can = {'man_can_chi': man_can + " " + man_chi, 'woman_can_chi': woman_can + " " + woman_chi, 'man_menh': man_menh, 'woman_menh': woman_menh}
        return jsonify(can), http.HTTPStatus.OK

    if fun == 1: #coi hợp tuổi
        man = _cung_nam(year_of_man)
        woman = _cung_nu(year_of_woman)
        both = _cung_ket_hop(man, woman)
        temp = _hop_tuoi(both)
        kq = {'cung_nam': man, 'cung_nu': woman, 'cung_ket_hop': both, 'ket_qua': temp}
        return jsonify(kq), http.HTTPStatus.OK


def _get_boi_toan(req):
    return "index.html"


def _ngu_hanh_can(year):
    can = year % 10
    if can == 0:
        return "Canh"
    elif can == 1:
        return "Tân"
    elif can == 2:
        return "Nhâm"
    elif can == 3:
        return "Quý"
    elif can == 4:
        return "Giáp"
    elif can == 5:
        return "Ất"
    elif can == 6:
        return "Bính"
    elif can == 7:
        return "Đinh"
    elif can == 8:
        return "Mậu"
    elif can == 9:
        return "Kỷ"

def _ngu_hanh_chi(year):
    chi = year % 100
    temp = chi % 12
    if temp == 0:
        return "Tỷ"
    elif temp == 1:
        return "Sửu"
    elif temp == 2:
        return "Dần"
    elif temp == 3:
        return "Mão"
    elif temp == 4:
        return "Thìn"
    elif temp == 5:
        return "Tỵ"
    elif temp == 6:
        return "Ngọ"
    elif temp == 7:
        return "Mùi"
    elif temp == 8:
        return "Thân"
    elif temp == 9:
        return "Dậu"
    elif temp == 10:
        return "Tuất"
    elif temp == 11:
        return "Hợi"

def _ngu_hanh(can, chi):
    if can == "Giáp" or can == "Ất":
        temp_can = 1
    elif can == "Bính" or can == "Đinh":
        temp_can = 2
    elif can == "Mậu" or can == "Kỷ":
        temp_can = 3
    elif can == "Canh" or can == "Tân":
        temp_can = 4
    elif can == "Nhâm" or can == "Quý":
        temp_can = 5
    if chi == "Tý" or chi == "Sửu" or chi == "Ngọ" or chi == "Mùi":
        temp_chi = 0
    elif chi == "Dần" or chi == "Mão" or chi == "Thân" or chi == "Dậu":
        temp_chi = 1
    else:
        temp_chi = 2

    temp = (temp_can + temp_chi) % 5
    if temp == 1:
        return "Kim"
    elif temp == 2:
        return "Thủy"
    elif temp == 3:
        return "Hỏa"
    elif temp == 4:
        return "Mộc"
    elif temp == 5:
        return "Thổ"

def _sum_num(num):   # tính tổng các chữ số của 1 số
    sum = 0
    while num > 0:
        sum = sum + num % 10
        num = math.floor(num / 10)
    return sum


def _cung_nam(year): # tính cung mệnh nam
    sum = _sum_num(year)
    cung = sum % 9
    if cung == 1:
        return "Khảm"
    elif cung == 2:
        return "Ly"
    elif cung == 3:
        return "Cấn"
    elif cung == 4:
        return "Đoài"
    elif cung == 5:
        return "Càn"
    elif cung  == 6:
        return "Khôn"
    elif cung == 7:
        return "Tốn"
    elif cung == 8:
        return "Chấn"
    elif cung == 9 or cung == 9:
        return "Khôn"


def _cung_nu(year):#tính cung mệnh nữ
    sum = _sum_num(year)
    cung = sum % 9
    if cung == 1:
        return "Cấn"
    elif cung == 2:
        return "Càn"
    elif cung == 3:
        return "Đoài"
    elif cung == 4:
        return "Cấn"
    elif cung == 5:
        return "Ly"
    elif cung == 6:
        return "Khảm"
    elif cung == 7:
        return "Khôn"
    elif cung == 8:
        return "Chấn"
    elif cung == 9 or cung == 9:
        return "Tốn"


def _cung_ket_hop(man_year,woman_year): #tính ra cung kết hơp
    man = man_year
    woman = woman_year
    temp = ""
    if man == "Càn":
        if woman == "Càn":
            temp = "Phục Vị"
        elif woman == "Khảm":
            temp = "Lục Sát"
        elif woman == "Cấn":
            temp = "Thiên Y"
        elif woman == "Chấn":
            temp = "Ngũ Quý"
        elif woman == "Tốn":
            temp = "Họa Hại"
        elif woman == "Ly":
            temp = "Tuyệt Mệnh"
        elif woman == "Khôn":
            temp = "Diên Niên"
        elif woman == "Đoài":
            temp = "Sinh Khí"
    elif man == "Khảm":
        if woman == "Càn":
            temp = "Lục Sát"
        elif woman == "Khảm":
            temp = "Phục vị"
        elif woman == "Cấn":
            temp = "Ngủ Quỷ"
        elif woman == "Chấn":
            temp = "Thiên Y"
        elif woman == "Tốn":
            temp = "Sinh Khí"
        elif woman == "Ly":
            temp = "Diên Niên"
        elif woman == "Khôn":
            temp = "Tuyệt Mệnh"
        elif woman == "Đoài":
            temp = "Họa Hại"
    elif man == "Cấn":
        if woman == "Càn":
            temp = "Thiên Y"
        elif woman == "Khảm":
            temp = "Ngủ Quỷ"
        elif woman == "Cấn":
            temp = "Phụ Vị"
        elif woman == "Chấn":
            temp = "Lục Sát"
        elif woman == "Tốn":
            temp = "Tuyệt Mệnh"
        elif woman == "Ly":
            temp = "Họa Hại"
        elif woman == "Khôn":
            temp = "Sinh Khí"
        elif woman == "Đoài":
            temp = "Diên Niên"
    elif man == "Chấn":
        if woman == "Càn":
            temp = "Ngủ Quỷ"
        elif woman == "Khảm":
            temp = "Thiên Y"
        elif woman == "Cấn":
            temp = "Ngủ Quỷ"
        elif woman == "Chấn":
            temp = "Phụ Vị"
        elif woman == "Tốn":
            temp = "Diên Niên"
        elif woman == "Ly":
            temp = "Sinh Khí"
        elif woman == "Khôn":
            temp = "Họa Hại"
        elif woman == "Đoài":
            temp = "Tuyệt Mệnh"
    elif man == "Tốn":
        if woman == "Càn":
            temp = "Họa Hại"
        elif woman == "Khảm":
            temp = "Sinh Khí"
        elif woman == "Cấn":
            temp = "Tuyệt Mệnh"
        elif woman == "Chấn":
            temp = "Diên Niên"
        elif woman == "Tốn":
            temp = "Phụ Vị"
        elif woman == "Ly":
            temp = "Thiên Y"
        elif woman == "Khôn":
            temp = "Ngủ Quỷ"
        elif woman == "Đoài":
            temp = "Lục Sát"
    elif man == "Ly":
        if woman == "Càn":
            temp = "Tuyệt Mạng"
        elif woman == "Khảm":
            temp = "Diên Niên"
        elif woman == "Cấn":
            temp = "Họa Hại"
        elif woman == "Chấn":
            temp = "Sinh Khí"
        elif woman == "Tốn":
            temp = "Thiên Y"
        elif woman == "Ly":
            temp = "Phục Vị"
        elif woman == "Khôn":
            temp = "Lục Sát"
        elif woman == "Đoài":
            temp = "Ngũ Quý"
    elif man == "Khôn":
        if woman == "Càn":
            temp = "Diên Niên"
        elif woman == "Khảm":
            temp = "Tuyệt Mệnh"
        elif woman == "Cấn":
            temp = "Sinh Khí"
        elif woman == "Chấn":
            temp = "Họa Hại"
        elif woman == "Tốn":
            temp = "Ngũ Quỷ"
        elif woman == "Ly":
            temp = "Lục sát"
        elif woman == "Khôn":
            temp = "Phục Vị"
        elif woman == "Đoài":
            temp = "Thiên Y"
    elif man == "Đoài":
        if woman == "Càn":
            temp = "Sinh Khí"
        elif woman == "Khảm":
            temp = "Họa Hại"
        elif woman == "Cấn":
            temp = "Diên Niên"
        elif woman == "Chấn":
            temp = "Tuyệt Mệnh"
        elif woman == "Tốn":
            temp = "Lục Sát"
        elif woman == "Ly":
            temp = "Ngũ Quý"
        elif woman == "Khôn":
            temp = "Thiên Y"
        elif woman == "Đoài":
            temp = "Phục Vị"
    return  temp


def _hop_tuoi(cung): #tính hợp tuổi
    if cung == "Sinh Khí" or cung == "Diên Niên" or cung == "Thiên Y" or cung == "Phục Vị":
        return "Cát"
    else:
        return "Hung"