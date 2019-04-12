# coding: utf-8
#!/usr/bin/env python
import re
import platform
'''
身分證字號規則： 
字母(ABCDEFGHJKLMNPQRSTUVXYWZIO)對應一組數(10~35)， 
令其十位數為X1，個位數為X2；( 如Ａ：X1=1 , X2=0 )；D表示2~9數字 
Y = X1 + 9*X2 + 8*D1 + 7*D2 + 6*D3 + 5*D4 + 4*D5 + 3*D6 + 2*D7+ 1*D8 + D9 
如Y能被10整除，則表示該身分證號碼為正確，否則為錯誤。
'''

def check(ID):
    try:
        ID=str.upper(ID)
        bir_code={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'H':17,'I':34,'J':18,'K':19,'L':20,'M':21,
                  'N':22,'O':35,'P':24,'Q':24,'R':25,'S':26,'T':27,'U':28,'V':29,'W':32,'X':30,'Y':31,'Z':33
            }
        X=str(bir_code[ID[0]])
        X1=int(X[0])
        X2=int(X[1])*9
        D1=int(ID[1])*1
        D2=int(ID[2])*2
        D3=int(ID[3])*3
        D4=int(ID[4])*4
        D5=int(ID[5])*5
        D6=int(ID[6])*6
        D7=int(ID[7])*7
        D8=int(ID[8])*8
        D9=int(ID[9])
        Y=X1+X2+D1+D2+D3+D4+D5+D6+D7+D8+D9
    
        if Y%10==0:
            return True
        else:
            return False
    except:
        pass

if __name__=="__main__":
    version=platform.python_version()

    while 1:
        if re.search('^2.',version):
            ID=raw_input("請輸入身份證字號：")
        else:
            ID=input("請輸入身份證字號")

        if check(ID):
            print('正確')
        else:
            print('錯誤，請重新輸入')