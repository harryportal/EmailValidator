import re

print('THIS PROGRAM VALIDATES AN EMAIL ADDRESS USING REGULAR EXPRESSION')


def check_mail(emails):
    pattern = re.compile('^[^0-9]+.+@.+\.com')  # pattern to match email address
    """
    The idea is for the email to not start with number, this is done with the ^[^0-9]+
    """
    match = pattern.findall(emails)
    if match:
        print(f'"{emails}" is a valid Email Address!')
    else:
        print(f'"{emails}" is not a valid Email Address!')


response = 'yes'
proceed_Resp = 'yes'
while response.lower() == proceed_Resp:
    email = input("\nEnter the email to be validated: ")
    check_mail(email)
    response = input("Wanna try again? [yes/no]:")
