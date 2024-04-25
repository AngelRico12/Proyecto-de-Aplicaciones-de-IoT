import machine
import time
import network
import ujson
from umqtt.simple import MQTTClient
from hcsr04 import HCSR04

# Configuración de los pines para el sensor ultrasónico y el servo motor
TRIGGER_PIN = 14
ECHO_PIN = 12
SERVO_PIN = 13
MOTION_PIN = 15  # Pin para el sensor de movimiento

# Configuración de la frecuencia del servo
SERVO_FREQ = 50

# Configuración de los detalles de conexión Wi-Fi
WIFI_SSID = "Angel"
WIFI_PASSWORD = "12345678"

# Configuración de los detalles del servidor MQTT
MQTT_SERVER = "192.168.43.27"
MQTT_TOPIC_SERVO_CONTROL = "servo/control"
MQTT_TOPIC_SERVO_STATUS = "servo/status"

# Configuración de las credenciales MQTT
MQTT_CLIENT_ID = "servo"
MQTT_USER = "servo_mqtt"
MQTT_PASSWORD = "123"

MIN_DISTANCE = 10  # cm

# Inicialización del sensor ultrasónico
ultrasonic = HCSR04(trigger_pin=TRIGGER_PIN, echo_pin=ECHO_PIN)

# Inicialización del servo motor
servo = machine.PWM(machine.Pin(SERVO_PIN), freq=SERVO_FREQ)
servo.duty(0)  # Establecer el servo en su posición inicial

# Inicialización del sensor de movimiento
motion_sensor = machine.Pin(MOTION_PIN, machine.Pin.IN)

# Inicialización de la conexión Wi-Fi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASSWORD)

# Esperar a que se establezca la conexión Wi-Fi
while not wifi.isconnected():
    pass

print("Conexión Wi-Fi establecida:", wifi.ifconfig())

# Inicialización del cliente MQTT
mqtt_client = MQTTClient(MQTT_CLIENT_ID, MQTT_SERVER, user=MQTT_USER, password=MQTT_PASSWORD)

try:
    mqtt_client.connect()
    print("Conexión MQTT establecida")
except Exception as e:
    print("Error al conectar MQTT:", e)

# Variable de control para el estado del servo
servo_on = False

def on_message(topic, msg):
    global servo_on
    payload = msg.decode('utf-8')  # Convertir bytes a string
    if topic.decode('utf-8') == MQTT_TOPIC_SERVO_CONTROL:  # Convertir topic a string para comparar
        if payload == "on":
            servo_on = True
        elif payload == "off":
            servo_on = False

mqtt_client.set_callback(on_message)
mqtt_client.subscribe(MQTT_TOPIC_SERVO_CONTROL)

try:
    while True:
        mqtt_client.check_msg()  # Verificar mensajes MQTT
        if servo_on:
            for angle in range(0, 181, 10):  # Hacer un barrido desde 0 a 180 grados
                servo.duty(angle)  # Mover el servo a un ángulo específico
                time.sleep(0.5)  # Pequeño retardo antes de medir la distancia
                distance = ultrasonic.distance_cm()  # Medir la distancia
                if distance <= MIN_DISTANCE:
                    # Enviar distancia y ángulo a través de MQTT si la distancia es menor o igual a MIN_DISTANCE
                    mqtt_client.publish(MQTT_TOPIC_SERVO_STATUS, ujson.dumps({"angle": angle, "distance": distance}))
        else:
            servo.duty(0)  # Mover el servo a 0 grados (apagado)
            time.sleep(0.1)  # Pequeño retardo para liberar el procesador

except KeyboardInterrupt:
    pass

# Desconectar el cliente MQTT y desactivar la conexión Wi-Fi al finalizar
mqtt_client.disconnect()
wifi.disconnect()
wifi.active(False)
print("Desconectado de MQTT y Wi-Fi")


