import re
import smtplib
from email.utils import parseaddr

def is_valid_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email)

def check_email_exists(server, email):
    try:
        username, domain = parseaddr(email)
        if not domain:
            return False

        with smtplib.SMTP(server) as smtp:
            code, message = smtp.helo()

            if code != 250:
                return False

            code, message = smtp.mail("example@example.com")
            if code != 250:
                return False

            code, message = smtp.rcpt(email)
            if code == 250:
                return True

    except Exception as e:
        print(f"Error: {str(e)}")
    return False

def verify_and_check_emails(input_file, output_file, server):
    verified_emails = []

    with open(input_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if is_valid_email(line) and check_email_exists(server, line):
                verified_emails.append(line)

    with open(output_file, 'w') as file:
        for email in verified_emails:
            file.write(email + '\n')

if __name__ == "__main__":
    input_file = input("Enter the path to the input file: ")
    output_file = input("Enter the path to the output file: ")
    server = input("Enter the SMTP server address (e.g., smtp.example.com): ")

    verify_and_check_emails(input_file, output_file, server)

    print("Email verification completed. Verified emails saved to", output_file)
