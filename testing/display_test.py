from pie_ui.display import Display
from pie_core.logger import Logger


log = Logger()

display = Display()


log.info(
    f"Display detected: {display.info()}"
)


print(display.info())
