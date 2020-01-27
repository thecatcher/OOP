def input_passwd():
    pwd = input("请输入密码:")

    if len(pwd) >= 8:
        return pwd
    ex = Exception("密码长度不够")
    raise ex


try:
    user_pwd = input_passwd()
    print(user_pwd)
except Exception as result:
    print(result)
