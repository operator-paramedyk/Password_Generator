# Password Generator
by www.operator-paramedyk.pl

## Introduction

PasswordGenerator module allows user to generate one or more random passwords with the use of secrets library (https://docs.python.org/3/library/secrets.html).

It is designed to work in two modes:
- individual password generator, where script returns one password of set parameters until user decides to quit,
- batch password generator, where set of passwords of set parameters is returned as a textfile.

## Single password generation

To generate single password, please select a charts set used for password generation and password length.

Please remember that generated password **isn't** saved and will disappear when you turn off the script.

**And I strongly do not recommend to write the password down or save it in non-encrypted form.**

When password is generated, you can generate another one. To exit the script, please press ```q``` and ```ENTER``` after password generations.

## Batch password generation

You can generate a set of passwords with set parameters in one batch. This may be used for example as tokens - one-time passwords.

To generate batch of passwords, you need to specify parameters of them - charts to be used and token's length - simirarly to individual password mode. Moreover, you need to define number of tokens to be generated.

By default, tokens are saved in tokens_generated.txt file. You can change it by modifying variable ```self.filename```.