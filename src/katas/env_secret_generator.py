import re
import secrets


class SecretKeyGenerator:

    env_variable_key = 'SECRET_KEY'
    file = '.env'

    def __init__(self, file=None):
        self.file = file if file is not None else self.file

    def write_to_file(self):
        if not self.check_str_in_lines(self.env_variable_key):
            with open(self.file, 'a+') as env_file:
                env_file.write(self.make_key_and_value())

    def generate_skey(self):
        return secrets.token_urlsafe(16)

    def make_key_and_value(self):
        line = self.env_variable_key + '=' + self.generate_skey()
        return line.rstrip('\r\n') + '\n'

    def check_str_in_lines(self, check):
        with open(self.file, 'r+') as file:
            for line in file.readlines():
                line = re.sub(r'[\n\t\s]*', '', line)
                if check in line:
                    return True
            else:
                return False
