from gpiozero import OutputDevice, DigitalInputDevice
from hardware import actionOutputDevice
import sched, time

# Настройка логирования
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="hydroponicplant.log",
    filemode="a",
    format="%(asctime)s %(levelname)s %(message)s")

# Устройства

# Освещение растений
lamp = OutputDevice(17)
lamp.active_high = False
lamp.off()

# Датчик освещения
lightSensor = DigitalInputDevice(18)

# Помпа накачки воды
pomp = OutputDevice(27)
pomp.active_high = False
pomp.off()

# Клапан слива воды
valve = OutputDevice(23)
valve.active_high = False
valve.off()

# Аэратор
aero = OutputDevice(22)
aero.active_high = False
aero.off()

# Параметры устройств

lampDelayTime = 10
pompRunTime = 10
valveRunTime = 10
aeroRunTime = 10

# Обработчики устройств

def lampСontrol(scheduler) :
    scheduler.enter(lampDelayTime, 1, lampСontrol, (scheduler,))

def pompСontrol(scheduler) :
    scheduler.enter(pompRunTime, 1, pompСontrol, (scheduler,))

def valveСontrol(scheduler) :
    scheduler.enter(valveRunTime, 1, valveСontrol, (scheduler,))

def aeroСontrol(scheduler) :
    scheduler.enter(aeroRunTime, 1, aeroСontrol, (scheduler,))

# Обработка завершения работы 
import atexit

@atexit.register
def exit_handler():
    logging.info("[Stop]")

# Запуск
logging.info("[Start]")

main_scheduler = sched.scheduler(time.time, time.sleep)

main_scheduler.enter(1, 1, lampСontrol, (main_scheduler,))

main_scheduler.enter(1, 1, pompСontrol, (main_scheduler,))

main_scheduler.enter(1, 1, aeroСontrol, (main_scheduler,))

main_scheduler.run()
