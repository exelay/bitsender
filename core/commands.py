from cleo import Command

from core.services import Sender


class RunCommand(Command):
    """
    Start messaging to telegram users from user list.
    run
        {config-file? : Path to the configuration *.yaml file}
    """
    default_config_file = 'configurations/config.yaml'  # TODO сделать путь абсолютным

    def handle(self):
        config_file = self.argument('config-file')
        if not config_file:
            config_file = self.default_config_file
        sender = Sender(config_file)
        sender.send()
