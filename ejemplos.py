from hashlib import sha3_512
from os.path import abspath

def FilterEncrypt(password_user, list_password):
    """
    Filter Password from dict list
    """
    result_filter = filter(lambda x : Encrypt(x.rstrip()) == password_user, list_password)
    convert_list_result_filter = list(result_filter)
    return convert_list_result_filter


def Encrypt(encrypt_password):
    """
    : encrypt_password param password/user
    """
    param_encrypt_password = encrypt_password.encode("utf-8")
    encrypt_process = sha3_512(param_encrypt_password)
    encrypt_finish = encrypt_process.hexdigest()
    return encrypt_finish


def ReadDictPassword(rut):
    """
    :rut path from dict
    """
    rut_dict = abspath(rut)
    with open(rut_dict, "r") as dict_password:
        extract_list_password = dict_password.readlines()
        dict_password.close()
    return extract_list_password


def UserInterfaceConsole():
    password_user = input("Password => \t")
    dict_result = ReadDictPassword("./dicts/1_basic.txt")
    result_filter = FilterEncrypt(password_user, dict_result)
    return result_filter


result_finish = UserInterfaceConsole()
print(result_finish)

# 