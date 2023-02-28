import hashlib
from hashlib import algorithms_guaranteed
from os.path import abspath
import time

_algorithms_encrypt = set(algorithms_guaranteed)


def filter_compared(arg_temp: str, password: str) -> bool:
    """ 
    Compare and return boolean for result the from `filter_encrypt` function 
    """
    clean_argument = arg_temp.rstrip()

    def def_lambda_convert(item_iter_hash):
        return encrypt(clean_argument, item_iter_hash)

    option_iter_hash = map(def_lambda_convert, _algorithms_encrypt)
    option_hash = set(option_iter_hash)

    return password in option_hash


def filter_encrypt(list_password: str, password: str) -> str:
    """
    Filter Password from dict list
    """
    def temporal_filter_compared(item_password_hash):
        return filter_compared(item_password_hash, password)

    result_filter = filter(temporal_filter_compared, list_password)

    convert_list_result_filter = list(result_filter)
    """ convert_list_result_filter = set(i for i in list_password if filter_compared(i, password)) """

    return convert_list_result_filter


def encrypt(encrypt_password: str, type_algorithm: str) -> str:
    """
    :Encrypt_password param password/user 
    """
    param_encrypt_password = encrypt_password.encode("utf-8")
    list_arguments_encrypt = [
        param_encrypt_password
    ]
    encrypt_process = getattr(hashlib, type_algorithm)(*list_arguments_encrypt)
    try:
        encrypt_finish = encrypt_process.hexdigest()
    except TypeError:
        encrypt_finish = encrypt_process

    return encrypt_finish


def read_dict_password(rut: str) -> list[str]:
    """
    :rut path from dict
    """
    rut_dict = abspath(rut)
    with open(rut_dict, "r") as dict_password:
        extract_list_password = dict_password.readlines()
        dict_password.close()
    return extract_list_password


def user_interface_console():
    password_user = "2a378eb0084619596cbd97a9573fc89ea83eab13235afa536e8e894f0f6fa398a90fb836c99666756bf0b4d62dee040bce3026eb2f49249ba8f78e66bc206109"
    dict_result = read_dict_password("../dicts/1_basic.txt")
    result_filter = filter_encrypt(dict_result, password_user)
    return result_filter


start = time.time()

result = user_interface_console()
print(result)

end = time.time()
good_time = end - start
print(good_time)
