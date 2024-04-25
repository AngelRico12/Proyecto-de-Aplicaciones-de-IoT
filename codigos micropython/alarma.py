from hcsr04 import HCSR04
from machine import Pin, PWM
import time
import network
from umqtt.simple import MQTTClient

# Configurar los pines Trigger y Echo para ambos sensores ultrasónicos
sensor1 = HCSR04(trigger_pin=12, echo_pin=14)
sensor2 = HCSR04(trigger_pin=26, echo_pin=27)

# Configurar el pin del buzzer con PWM
buzzer_pin = Pin(33, Pin.OUT)
buzzer_pwm = PWM(buzzer_pin)
buzzer_pwm.freq(1000)  # Frecuencia de resonancia del buzzer

# Configurar la red WiFi
SSID = "Angel"
PASSWORD = "12345678"

# Configurar el cliente MQTT
MQTT_BROKER = "192.168.43.27"
TOPIC_ALARMA = "alarma"
TOPIC_CONTROL = "alarma/control"

# Variable para controlar el estado de la alarma
alarma_activada = False  # Inicialmente la alarma está desactivada

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
    global alarma_activada
    if msg == b"on":
        alarma_activada = True
        print("Alarma activada")
    elif msg == b"off":
        alarma_activada = False
        # Apagar el buzzer si se desactiva la alarma
        buzzer_pwm.duty(0)
        print("Alarma desactivada")

# Función para hacer sonar el buzzer
def hacer_sonar_buzzer():
    # Hacer sonar el buzzer con PWM
    buzzer_pwm.duty(1000)  # Encender el buzzer al máximo de su capacidad
    time.sleep(0.2)  # Mantenerlo encendido durante 0.2 segundos
    buzzer_pwm.duty(0)  # Apagar el buzzer

# Configurar el cliente MQTT y suscribirse al topic de control
conectar_wifi()
client = MQTTClient("esp32", MQTT_BROKER)
client.set_callback(control_callback)
client.connect()
client.subscribe(TOPIC_CONTROL)

while True:
    # Revisar si hay mensajes nuevos
    client.check_msg()
    
    # Si la alarma está activada, medir la distancia con los sensores y activar la alarma si es necesario
    if alarma_activada:
        distancia_sensor1 = sensor1.distance_cm()
        distancia_sensor2 = sensor2.distance_cm()
        
        # Determinar si se activa la alarma
        if distancia_sensor1 < 20 or distancia_sensor2 < 20:
            hacer_sonar_buzzer()
            client.publish(TOPIC_ALARMA, b"Alarma activada")
    
    # Esperar un breve tiempo antes de la próxima medición
    time.sleep(0.1)


