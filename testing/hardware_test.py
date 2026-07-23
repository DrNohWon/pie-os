from pie_core.hardware import Hardware
from pie_core.logger import Logger


log = Logger()

hw = Hardware()


log.boot(
    "Hardware detection test"
)


info = hw.get_system_info()


for item, value in info.items():

    log.info(
        f"{item}: {value}"
    )


print(info)
