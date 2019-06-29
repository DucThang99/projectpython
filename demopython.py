n = ' '
while n.len() < 8 and n.isalpha() != True n.isdigit() != True  and n.isalnum() != True or n.find(' ') == 1 :
    n = input('mời bạn nhập pass: ')

print('a:'+n)    


'''
string.isalpha()#kiểm tra chuỗi có 
#chứa mỗi ksy tự chữ ko nếu chứa mỗi chữ thì trả về true
string.isdigit()# hàm keierm tra chwuas mỗi số 
#hay không    số true
string.isalnum()# kiểm tra chuỗi cso chứa các ký tự kahcs ngoãi chữ và số(có ký tự đặc biệt không) có ký tự đặc biệt thì trả về false
string.find(' ')# nếu trong chuỗi không có ký tự cần tìm thì trả về -1
'''