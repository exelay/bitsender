from cleo import Application
from core.commands import RunCommand

application = Application()
application.add(RunCommand())

if __name__ == "__main__":
    application.run()
