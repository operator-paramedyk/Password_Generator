import secrets

class PasswordGenerator:

    def __init__(self):
        """Object is initiated without parameters."""
        """All argumnets are set by default blank and will be set in further steps."""
        self.charts_included = '' # chosen set of charts for password generation
        self.pass_length = 0 # password length, allowed between pass_min_length and pass_max_length signs,
                            # set to 0 to make sure loop password_length is asking user for correct value
        self.pass_min_length = 4 # by default, individual password can't be shorter than 4 charts...
        self.pass_max_length = 100 # ... nor longer than 100 charts
        self.token_number = 0 # number of tokens to be generated in token_generator method
        self.mode = '0' # variable setting the mode of password generator (token or individual password)
        self.filename = 'tokens_generated.txt' #file to be used in token mode

    def charts_select(self):
        """Define a set of charts to be used in your password"""
        low_letters = 'abcdefghijklmnopqrstuvwxyz'
        upp_letters = low_letters.upper()
        nums = '0123456789'
        symbols = '`~!@#$%^&*()_+-=[]{};". \/>?,<\':'
        charts_setup = ''

        # set options and prompt options to the user
        charts_options = {
            'a': low_letters + upp_letters + nums + symbols,
            'b': low_letters + upp_letters + nums,
            'c': low_letters + upp_letters,
            'd': low_letters + nums,
            'e': nums,
            'f': upp_letters,
            'g': low_letters
        }

        print('a. lower and upper letters, digits, and special charts,\n'
              'b. digits, lower and upper letters,\n'
              'c. lower and upper letters,\n'
              'd. digits and lower letters,\n'
              'e. digits only,\n'
              'f. upper letters only,\n'
              'g. lower letters only.\n')

        # awaiting until user choose one of the sets available
        while charts_setup not in charts_options.keys():
            charts_setup = input("\nWhich signs should be included in your passwerd? (select option a-g): ")

        # method returns to the object set of charts to be used during password generation
        self.charts_included = charts_options.get(charts_setup)
        print(f"Following charts will be considered to compose your secure password: {self.charts_included}.\n")
        # return charters to be used for password generation
        return(self.charts_included)

    def password_length(self):
        """Method prompting for user input on password length (5 to 100 signs)."""
        # user will be prompted until value between pass_min_length and pass_max_length is provided
        print(f"Password length should be a positive integer between {self.pass_min_length} and {self.pass_max_length}.")
        while self.pass_length < self.pass_min_length or self.pass_length > self.pass_max_length or ValueError:
            # check if user provided numeric value
            try:
                self.pass_length = int(input('How long your new password should be? '))
            except ValueError:
                print('Please try again.')
                pass
            else:
                # check if value provided is within acceptable password length
                if self.pass_length < self.pass_min_length or self.pass_length > self.pass_max_length:
                    print('Please try again.')
                else:
                    #return value used for password(s) generation
                    return(self.pass_length)

    def set_password(self, password_length, charts_included):
        """Random password generation"""
        # Creating a blank string
        # Then add to it randomly selected number (defined by length) of charts
        # Chosen from charts_included string.
        password = ''
        for i in range(0,password_length):
            password += secrets.choice(charts_included)
        # returns password
        return(password)

    def individual_password(self):
        """Method to define password in individual mode"""
        n = True
        # looping method, so user can generate multiple passwords (same length and set of charts) during one session

        while n == True:
#            self.pass_length = self.password_length()
            print(f"Your new password is: {self.set_password(self.pass_length, self.charts_included)}.")
            print("\nPlease remember your password isn't stored anywhere!")
            print("\nBut I definitely do not recommend to write it down.")

            # checking if user wants to generate next password
            next_password = input("\nPress 'q' to quit. Any other key will generate another password for you. ")
            if next_password.lower() == 'q':
                n = False
            else:
                pass

    def tokens_to_file(self, number, charts, length):
        """Method to generate batch of passwords, to be used e.g. as tokens"""
        with open(self.filename, 'w') as f:
            for i in range(0,number):
                f.write(f"{self.set_password(self.pass_length, self.charts_included)}\n")
        print(f"Successfully saved {self.token_number} passwords in file {self.filename}.")
        f.close()

    def token_generator(self):
        """Method asking user for parameters of passwords to be saved in file"""
        print('This will generate a list of tokens saved in a txt file.\n')

        # ask user how many tokes does he need
        while self.token_number <= 0:
            # check if user provided numeric value
            try:
                self.token_number = int(input('How many tokens do you need? '))
            except ValueError:
                print('Non-numeric value provided. Please try again.')
                pass
            else:
                # check if the value provided is positive
                if self.token_number <= 0:
                    print('Number of tokens must be positive! Please try again')
                else:
                    # ask for parameters and generate set of tokens
                    self.charts_select()
                    self.password_length()
                    self.tokens_to_file(self.token_number, self.charts_included, self.pass_length)



    def menu(self):
        """Method asks user what mode of password generator does he want to use"""
        modes = {
            1: 'individual password generator,',
            2: 'batch password (tokens) generator.'
        }
        print("Select generator's mode:")
        print(modes)
        # choose mode o password generator - individual passwords or tokens
        while self.mode != 1 and self.mode != 2:
            try:
                self.mode = int(input('Mode selected (1 or 2): '))
            except ValueError:
                print('Please select mode 1 or 2.')
            else:
                # individual password mode
                if self.mode == 1:
                    # individual password mode
                    self.charts_select() # set of charts
                    self.password_length() # password length
                    self.individual_password() # generate and print password
                # token mode
                elif self.mode == 2:
                    # token mode
                    self.token_generator()
                else:
                    print('Please select mode 1 or 2.')


