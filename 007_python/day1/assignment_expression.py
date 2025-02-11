# 3. Search for email addresses in a text file
import re

def find_emails(file_path):
    # Regular expression for finding emails
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Find all emails in the file
        emails = re.findall(email_pattern, content)
        
        if emails:
            print("Found emails:")
            for email in emails:
                print(email)
        else:
            print("No emails found.")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function with the corrected file path
find_emails(r'C:\Users\Administrator\Desktop\devops\007_python\day1\email.txt')

# find_emails(r'C:\Users\Administrator\Desktop\devops\007_python\day1\email.txt')