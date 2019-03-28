import json


class Config:

    def __init__(self):
        self.token: str = ""
        self.prefix: str = ""
        self.db_user: str = ""
        self.db_pass: str = ""
        self.db_name: str = ""

        try:
            with open("config.json", 'x') as file:
                self.write_file(file)
                file.close()

        except FileExistsError:
            with open("config.json") as file:
                self.read_file(file)
                file.close()

    @staticmethod
    def write_file(file):
        output = {
            "token": " ",
            "prefix": " ",
            "db_user": " ",
            "db_pass": " ",
            "db_name": " "
        }
        file.write(json.dumps(output))

    def read_file(self, file):
        config_in = file.read()
        config_parsed = json.loads(config_in)
        self.token = config_parsed['token']
        self.prefix = config_parsed['prefix']
        self.db_user = config_parsed['db_user']
        self.db_pass = config_parsed['db_pass']
        self.db_name = config_parsed['db_name']