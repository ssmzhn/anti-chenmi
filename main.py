import datetime
def isValidIdNumber(id_num):
    num_list=('0','1','2','3','4','5','6','7','8','9')
    num_X_list=('0','1','2','3','4','5','6','7','8','9','X','x')
    if len(id_num)!=18:
        return False
    for x in id_num[:17]:
        if not x in num_list:
            return False
    if not id_num[-1] in num_X_list:
        return False
    # 身份证字符无问题，开始校验码验证
    id_num_list=list(id_num[::-1])
    if id_num_list[17] in ('x','X'):
        id_num_list[17]='10'
    verify = 0 # 存放校验结果
    for i in range(len(id_num_list)):
        weight = 2**i%11
        a = int(id_num_list[i])
        verify += weight * a

    # %11 == 1，证明合法
    if verify % 11 == 1:
        return True
    return False
def verifyDate(id_num): # 成没成年啊 id_num 为 str
    # birthday = datetime.date(int(id_num[6:10]),int(id_num[10:12]),int(id_num[12:14]))
    # 此处不用datetime.timedelta，因为不好处理年份
    birth_year = int(id_num[6:10])
    birth_month = int(id_num[10:12])
    birth_day = int(id_num[12:14])
    current_year = datetime.date.today().year
    current_month = datetime.date.today().month
    current_day = datetime.date.today().day
    if current_year - birth_year > 18:
        return True
    elif current_year - birth_year == 18:
        if current_month > birth_month:
            return True
        elif current_month == birth_month:
            if current_day > birth_day:
                return True
    return False

def main():
    test=input('让我开开盒罢: ')
    if isValidIdNumber(test):
        print('是正常的身份证号捏')
        if verifyDate(test):
            print('您成年了！')
        else:
            print('主播还没成年呐')
    else:
        print('这是什么几把，我看不懂')

if __name__ == '__main__':
    main()
