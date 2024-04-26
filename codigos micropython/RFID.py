from machine import Pin, SPI, PWM
import network
from umqtt.simple import MQTTClient
from mfrc522 import MFRC522
import utime

# Configuración del SPI para el lector RFID
sck = Pin(18, Pin.OUT)
mosi = Pin(23, Pin.OUT)
miso = Pin(19, Pin.IN)
spi = SPI(1, baudrate=1000000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso)

# Configuración del lector RFID
rst_pin = Pin(13, Pin.OUT)
cs_pin = Pin(15, Pin.OUT)
rfid = MFRC522(spi, rst_pin, cs_pin)

SSID = "Angel"
PASSWORD = "12345678"

# Configuración del broker MQTT
BROKER = "192.168.43.27"
TOPIC_RFID_STATUS = "rfid/status"
TOPIC_RFID_CONTROL = "rfid/control"

# Configuración del buzzer
buzzer_pin = Pin(14, Pin.OUT)
buzzer_pwm = PWM(buzzer_pin)
buzzer_pwm.freq(440)  # Frecuencia de resonancia del buzzer

# Variable para controlar el estado del dispositivo
device_enabled = True

# Función para conectar a la red WiFi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        print("Conectando a WiFi...")
        wlan.active(True)
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            pass
    print("Conexión WiFi exitosa")

# Función para conectar al broker MQTT
def connect_mqtt():
    client = MQTTClient("esp32", BROKER)
    client.connect()
    print("Conexión MQTT exitosa")
    return client

# Función para manejar los mensajes recibidos en el topic de control
def control_callback(topic, msg):
    global device_enabled
    if msg == b"on":
        device_enabled = True
        print("Dispositivo habilitado")
    elif msg == b"off":
        device_enabled = False
        # Apagar el buzzer si se desactiva el dispositivo
        buzzer_pwm.duty(0)
        print("Dispositivo deshabilitado")

# Función principal para leer el UID de la tarjeta RFID y publicarlo en MQTT
def main():
    connect_wifi()
    mqtt_client = connect_mqtt()
    mqtt_client.set_callback(control_callback)
    mqtt_client.subscribe(TOPIC_RFID_CONTROL)

    while True:
        mqtt_client.check_msg()  # Revisar si hay mensajes nuevos
        if device_enabled:
            stat, tag_type = rfid.request(rfid.REQIDL)
            if stat == rfid.OK:
                print("Dispositivo detectado...")
                stat, raw_uid = rfid.anticoll()
                if stat == rfid.OK:
                    uid_actual = ":".join([hex(i) for i in raw_uid])
                    print("UID de la tarjeta:", uid_actual)
                    mqtt_client.publish(TOPIC_RFID_STATUS, uid_actual)
                    # Hacer sonar el buzzer como confirmación
                    buzzer_pwm.duty(102)  # Encender el buzzer al máximo de su capacidad
                    utime.sleep(0.2)  # Mantenerlo encendido durante 0.2 segundos
                    buzzer_pwm.duty(0)  # Apagar el buzzer
                    utime.sleep(0.5)  # Pequeña pausa para evitar repeticiones rápidas
            else:
                # No se detectó ninguna tarjeta, apagar el buzzer
                buzzer_pwm.duty(0)
        utime.sleep(3)  # Esperar 3 segundos antes de la próxima detección

if __name__ == "__main__":
    main()


