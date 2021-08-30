import yaml
from bit import wif_to_key, Key


class Sender:
    config: dict
    key: Key

    def __init__(self, config_file):
        self.config_file = config_file

    def send(self):
        self._parse_config_file()
        self._set_key()
        self._send_bitcoins()

    def _parse_config_file(self):
        with open(self.config_file, 'r') as f:
            self.config = yaml.safe_load(f)

    def _set_key(self):
        self.key = wif_to_key(self.config['key'])

    def _send_bitcoins(self):
        fee = self.config['fee']
        outputs = self.config['recipients']
        tx_hash = self.key.send(outputs, fee=fee)

        print(f"Your transaction hash is: {tx_hash}")
