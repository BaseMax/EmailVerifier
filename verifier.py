import re

def is_valid_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+v[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email)

def verify_emails(input_file, output_file):
    verified_emails = []

    with open(input_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if is_valid_email(line):
                verified_emails.append(line)

    with open(output_file, 'w') as file:
        for email in verified_emails:
            file.write(email + '\n')

if __name__ == "__main__":
    input_file = input("Enter the path to the input file: ")
    output_file = input("Enter the path to the output file: ")

    verify_emails(input_file, output_file)

    print("Email verification completed. Verified emails saved to", output_file)
