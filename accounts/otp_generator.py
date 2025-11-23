"""in this file i will be making otp"""
from random import randint


"""generating otp over here"""
def generate_otp():
    x = randint(1000,9999)
    return x


print(generate_otp() )