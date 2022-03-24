name=input("请输入您的用户名")
password=input("请输入您的密码")
def user_login(user_name,user_password):
    user_file="user.txt"
    password_file="password.txt"
    t=0
    k=0
    with open(user_file,"r") as f1:
        f1_line=f1.readlines()
    for line in f1_line:
        if user_name == line.strip():
            k=1
            break
        t=t+1
    if k==1:
        with open(password_file,"r") as f2:
            f2_line=f2.readlines()
            if user_password == f2_line[t].strip():
                print(f"欢迎您回来,尊敬的{user_name}")
            else:
                print("密码输入错误")
    else:
        x=input("是否创建新用户?(yes/no)\n")
        if x == 'yes':
            print(f"创建成功，欢迎{user_name}")
            with open(user_file,"a") as f3:
                f3.write(user_name)
                f3.write("\n")
            with open(password_file,"a") as f4:
                f4.write(user_password)
                f4.write("\n")
        elif x == 'no':
            print("已退出,欢迎您下次登录")
        else:
            print("输入错误，已退出")
    return k

