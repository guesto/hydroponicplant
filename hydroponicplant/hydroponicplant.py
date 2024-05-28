from gpiozero import OutputDevice, DigitalInputDevice
from hardware import actionOutputDevice

# Настройка логирования
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="hydroponicplant.log",
    filemode="a",
    format="%(asctime)s %(levelname)s %(message)s")

# Обработка завершения работы 
import atexit

@atexit.register
def exit_handler():
    logging.info("[Stop]")

# Запуск
logging.info("[Start]")


