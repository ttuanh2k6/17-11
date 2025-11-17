try:
    Van = float(input('Nhap diem Van: '))
    Toan = float(input('Nhap diem Toan: '))
    Anh = float(input('Nhap diem Anh: '))
except ValueError:
    print('Sai kieu nhap lieu!')
else:
    DTB = (Toan + Van + Anh)/3
    if Van < 0 or Van > 10 or Toan < 0 or Toan > 10 or Anh < 0 or Anh > 10:
        print('Sai kieu nhap lieu')
    else:
        if DTB > 9:
            print('Xuat sac!')
        elif DTB > 8:
            print('Gioi!')
        elif DTB > 7:
            print('Kha!')
        elif DTB > 5:
            print('Trung binh!')
        else:
            print('Yeu!')