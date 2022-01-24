"""Strong password generator"""
# importing secrets library and functions for password generations
import secrets
from PasswordGeneratorClass import PasswordGenerator

# pogram bodu

# initializing PasswordGenerator object

password = PasswordGenerator()

print('         PASSWORD GENERATOR')
print('    by www.operator-paramedyk.pl\n')

# running menu method to choose mode of password generator
password.menu()

