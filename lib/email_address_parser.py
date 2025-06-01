import re

class EmailAddressParser:
    def __init__(self, addresses):
        self.addresses = addresses

    def parse(self):
        # Split by comma or whitespace
        parts = re.split(r'[,\s]+', self.addresses)
        # Regex pattern for valid email addresses
        email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        # Filter valid emails and remove duplicates by using a set
        unique_emails = {email for email in parts if email_pattern.match(email)}
        # Return sorted list
        return sorted(unique_emails)
