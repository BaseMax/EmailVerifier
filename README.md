# Email Verifier

EmailVerifier is a Python script that allows you to verify email addresses from a list of text files. It performs the following steps:

1. **Read Files:** The script reads a list of text files containing email addresses.
2. **Ignore Non-Email Lines:** It processes each file, ignoring lines that do not contain valid email addresses.
3. **Verify Emails:** The script verifies the validity of each email address and filters out invalid ones.
4. **Save Output:** It saves the verified and cleaned email addresses to an output file.

## Getting Started

### Prerequisites

Make sure you have Python 3.x installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/BaseMax/EmailVerifier.git
   ```

2. Change to the project directory:

    ```bash
    cd EmailVerifier
    ```

3. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

You can run the EmailVerifier script with the following command:

```bash
python email_verifier.py input.txt output.txt
```

Replace `input.txt` with the path to your input text file containing email addresses and `output.txt` with the desired output file name.

## Example

Let's assume you have a file named `input.txt` with the following content:

```
user1@example.com
invalid_email
user2@example.com
user3@example.com
```

Running the script:

```bash
python email_verifier.py input.txt verified_emails.txt
```

After the script execution, the verified_emails.txt file will contain the verified and cleaned email addresses:

```
user1@example.com
user2@example.com
user3@example.com
```

## License

This project is licensed under the GPL-3.0 License - see the LICENSE file for details.

## Acknowledgments

If you have any questions or feedback, please feel free to open an issue.

Happy verifying!

Copyright 2023, Max Base
