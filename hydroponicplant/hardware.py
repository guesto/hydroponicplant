import logging

def actionOutputDevice(device, activation):
    if activation and not device.is_active:
        device.on()
        logging.info(f"[ON] {device.pin}")
    if not activation and device.is_active:
        device.off()
        logging.info(f"[OFF] {device.pin}")

