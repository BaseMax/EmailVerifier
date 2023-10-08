import re
import telnetlib

def is_valid_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+v[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email)

def check_email_exists(server, email):
    try:
        tn = telnetlib.Telnet(server, 25, timeout=5)
        response = tn.read_until(b'220', timeout=5)
        tn.write(b'HELO example.com\r\n')
        response = tn.read_until(b'250', timeout=5)

        tn.write(b'MAIL FROM:<example@example.com>\r\n')
        response = tn.read_until(b'250', timeout=5)

        tn.write(f'RCPT TO:<{email}>\r\n'.encode('utf-8'))
        response = tn.read_until(b'250', timeout=5)

        tn.write(b'QUIT\r\n')
        tn.close()

        return "250" in response.decode('utf-8')

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
