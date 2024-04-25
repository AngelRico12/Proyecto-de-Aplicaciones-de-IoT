from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep
import network
from umqtt.simple import MQTTClient

# Configura los pines para el motor paso a paso
IN1_PIN = 2
IN2_PIN = 4
IN3_PIN = 5
IN4_PIN = 18

motor_pins = [Pin(pin, Pin.OUT) for pin in (IN1_PIN, IN2_PIN, IN3_PIN, IN4_PIN)]

# Secuencia de pasos para el motor paso a paso (un ciclo completo)
STEPPER_SEQUENCE = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

# Inicializa el objeto PIR
pir_pin = Pin(14, Pin.IN)

# Configurar la red WiFi
SSID = "Angel"
PASSWORD = "12345678"

# Configurar el cliente MQTT
MQTT_BROKER = "192.168.43.27"  # Cambia por la dirección IP de tu broker MQTT
TOPIC_MOTOR = "motor"
TOPIC_CONTROL = "motor/control"

# Variable para controlar el estado del motor
motor_activado = False

# Configuración de la pantalla OLED
WIDTH = 128
HEIGHT = 64
i2c = I2C(0, scl=Pin(22), sda=Pin(21))  # Configura el bus I2C
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Función para mostrar "Bienvenido" en la pantalla OLED
def mostrar_bienvenido():
    oled.fill(0)  # Borra la pantalla
    oled.text("Bienvenido", 20, 20)
    oled.show()

# Conectar a la red WiFi
def conectar_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Conectando a la red WiFi...")
        sta_if.active(True)
        sta_if.connect(SSID, PASSWORD)
        while not sta_if.isconnected():
            pass
    print("Conexión WiFi establecida")

# Callback para manejar los mensajes recibidos en el topic de control
def control_callback(topic, msg):
    global motor_activado
    if msg == b"on":
        motor_activado = True
        print("Motor activado")
        client.publish(TOPIC_MOTOR, b"Motor activado")  # Enviar mensaje de activación al topic del motor
    elif msg == b"off":
        motor_activado = False
        print("Motor desactivado")

# Función para hacer girar el motor paso a paso en sentido horario
def forward_step(delay):
    for step in STEPPER_SEQUENCE:
        for pin, state in zip(motor_pins, step):
            pin.value(state)
        sleep(delay)

# Función para hacer girar el motor una vuelta completa en sentido horario
def rotate_stepper_motor(steps=200, delay=0.01):
    for _ in range(steps):
        forward_step(delay)

# Configurar el cliente MQTT y suscribirse al topic de control
conectar_wifi()
client = MQTTClient("esp32", MQTT_BROKER)
client.set_callback(control_callback)
client.connect()
client.subscribe(TOPIC_CONTROL)

# Mostrar "Bienvenido" en la pantalla OLED al iniciar
mostrar_bienvenido()

while True:
    # Revisar si hay mensajes nuevos
    client.check_msg()

    # Lee el valor del sensor PIR si el motor está activado
    if motor_activado:
        pir_value = pir_pin.value()

        # Si se detecta movimiento, gira el motor paso a paso
        if pir_value == 1:
            print("¡Movimiento detectado!")
            rotate_stepper_motor()  # Gira una vuelta completa
            sleep(1)  # Espera 1 segundo para evitar activaciones rápidas

    # Esperar un breve tiempo antes de revisar nuevamente
    sleep(0.1)
