# Fotografía Inteligente: Innovación Domótica en Estudio Familiar

### Integrantes
- Claudio Angel Huerta Ducoing   1222100432
- Jose Angel Rangel Rico         1222100483

## Introducción
El proyecto "Fotografía Inteligente: Innovación Domótica en Estudio Familiar" busca transformar un estudio fotográfico familiar tradicional en un espacio moderno y eficiente mediante la implementación de sistemas de domótica avanzados. La combinación de tecnologías como sensores ultrasónicos, cámaras, RFID y controladores permite automatizar diversas tareas, mejorar la experiencia del cliente y optimizar la gestión del negocio.

## Objetivos
- Implementar sistemas de domótica que mejoren la eficiencia y la experiencia del cliente.
- Desarrollar un sistema de detección de objetos mediante ultrasonido y cámara.
- Crear un sistema de detección de entrada para avisar cuando un cliente entre al local.
- Implementar un sistema de control de inventario mediante RFID.
- Crear un mostrador fotográfico interactivo para mostrar el trabajo del estudio de manera llamativa.

## Problemática
En el estudio fotográfico familiar nos encontramos con varios desafíos que impactan directamente en nuestra operación diaria y en la experiencia que ofrecemos a nuestros clientes. Uno de los principales problemas es la gestión manual del inventario, que conlleva a errores, pérdidas de tiempo y dificultades para mantener un registro preciso de los objetos y equipos disponibles. Esta falta de precisión en el inventario puede llevar a pérdidas económicas y a una gestión ineficiente de los recursos.

Además, la falta de un sistema de alerta eficiente para la entrada de clientes representa otro desafío. Sin un sistema que nos notifique de manera inmediata cuando un cliente entra al local, corremos el riesgo de perder oportunidades de venta al no poder atender a los clientes de manera oportuna y personalizada.

Por último, la presentación estática y poco atractiva de los trabajos fotográficos en el estudio no logra captar suficientemente la atención de los clientes. Esto puede limitar nuestras oportunidades de promocionar y vender nuestros servicios, ya que no estamos mostrando de manera efectiva la calidad y diversidad de los trabajos realizados.

## Visión del Proyecto:

- Transformación Digital: El proyecto representa una evolución significativa en la industria de la fotografía, incorporando tecnología de vanguardia para adaptarse a las demandas cambiantes del mercado. La integración de sistemas domóticos permite al estudio familiar posicionarse como un referente en innovación y eficiencia.

- Experiencia del Cliente Mejorada: Con la implementación de sistemas de detección de entrada y un mostrador fotográfico interactivo, el estudio ofrece una experiencia más personalizada y atractiva para los clientes. La atención inmediata al cliente al entrar al local y la presentación dinámica de los trabajos fotográficos aumentan el compromiso y la satisfacción del cliente.

- Eficiencia Operativa: La automatización de tareas como el control de inventario mediante RFID y la detección de objetos con sensores ultrasónicos optimiza los procesos operativos del estudio. Se reducen los errores, se minimizan las pérdidas de tiempo y se mejora la precisión en la gestión del inventario, lo que conlleva a una mayor eficiencia y rentabilidad del negocio.

- Diferenciación Competitiva: La adopción de tecnologías avanzadas posiciona al estudio fotográfico familiar como un pionero en su sector. La capacidad de ofrecer servicios innovadores y una experiencia única para los clientes se convierte en un factor clave para destacar frente a la competencia y captar nuevos clientes.

- Escalabilidad y Adaptabilidad: La modularidad de los sistemas implementados permite al estudio adaptarse fácilmente a futuras necesidades y expansiones. Además, la integración de software como Thonny, Grafana y Node-Red proporciona herramientas flexibles para monitorear y gestionar los sistemas de manera eficiente.

## Propuesta de Solución
Para abordar los desafíos identificados en nuestro estudio fotográfico familiar, proponemos una solución integral basada en la implementación de sistemas de domótica avanzados. Estos sistemas permitirán automatizar diversas tareas operativas, mejorar la eficiencia en la gestión del inventario, optimizar la atención al cliente y presentar de manera atractiva los trabajos fotográficos realizados.

### Sistema de seguridad y detección
Implementaremos un sistema de detección y visualización de objetos mediante el circuito ESP-CAM. Este sistema utilizará sensores ultrasónicos y cámaras ESP-32 Cam para realizar un inventario visual rápido y preciso, eliminando así los errores y pérdidas de tiempo asociados con la gestión manual del inventario.

**Materiales**
| Material                | Precio (MXN) | Cantidad | Imagen |
|-------------------------|--------------|----------|--------|
| Placa ESP-32            | $250         | 1        | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/8ebe7e59-6268-4eae-b684-dd0d2acd6e15)|
| ESP-32 Cam              | $250         | 1        | ![espcam](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/8d904e35-9f18-4bfb-8c6c-6fd260f72d0b)|
| Controlador ESP32-Cam   | $100         | 1        | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/8527399e-e620-4480-aa8e-9f430a7d1281)|
| Protoboard              | $50          | 1        | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/8f81780f-abb6-4323-a1e3-15c5300124a7)|
| Motor servo             | $70          | 1        | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/8489d51e-cc61-467f-876e-7fa0e0ceed10)|
| Cables                  | $100         | Varios   | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/dbef21da-1408-4371-a0a7-a4664cba8312)|

## Boceto

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/ba4667d5-4543-46c4-8259-1a9011765fe9)

## Conexión fritzing

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/94b591ef-cefa-4812-b947-dd8efc48f10b)

## Proceso construcción

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/d531f2d8-c99e-435e-92f6-0ad39b77bea8)

## Nodos node-red

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/eef0dae9-e5cc-4538-b704-9ba4ee0663b3)

|[
    {
        "id": "968c565030a8bbdf",
        "type": "mqtt in",
        "z": "b05da65af15284d8",
        "name": "Recibir MQTT",
        "topic": "servo/status",
        "qos": "2",
        "datatype": "json",
        "broker": "b43cb77a.8ffbd8",
        "nl": false,
        "rap": false,
        "inputs": 0,
        "x": 150,
        "y": 280,
        "wires": [
            [
                "7bc9741be93b7c73",
                "41a6525616924c2e"
            ]
        ]
    },
    {
        "id": "7bc9741be93b7c73",
        "type": "debug",
        "z": "b05da65af15284d8",
        "name": "debug 2",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "statusVal": "",
        "statusType": "auto",
        "x": 440,
        "y": 100,
        "wires": []
    },
    {
        "id": "8b23bb910ea3af5f",
        "type": "postgresql",
        "z": "b05da65af15284d8",
        "name": "",
        "query": "INSERT INTO servo_data (timestamp, angle, distance) VALUES (NOW(), $1, $2);\n",
        "postgreSQLConfig": "49c448cf338bd2d2",
        "split": false,
        "rowsPerMsg": 1,
        "outputs": 1,
        "x": 610,
        "y": 260,
        "wires": [
            [
                "aaa34973f64e5579"
            ]
        ]
    },
    {
        "id": "41a6525616924c2e",
        "type": "function",
        "z": "b05da65af15284d8",
        "name": "function 3",
        "func": "// Lee el payload del mensaje MQTT\nvar payload = msg.payload;\n\n// Construye la consulta SQL con los valores del mensaje\nvar query = \"INSERT INTO servo_data (timestamp, angle, distance) VALUES (NOW(), \" + payload.angle + \", \" + payload.distance + \");\";\n\n// Guarda la consulta SQL en el objeto de mensaje para ser enviado al siguiente nodo\nmsg.query = query;\n\n// Retorna el mensaje modificado\nreturn msg;\n",
        "outputs": 1,
        "timeout": 0,
        "noerr": 0,
        "initialize": "",
        "finalize": "",
        "libs": [],
        "x": 340,
        "y": 340,
        "wires": [
            [
                "8b23bb910ea3af5f"
            ]
        ]
    },
    {
        "id": "aaa34973f64e5579",
        "type": "debug",
        "z": "b05da65af15284d8",
        "name": "debug 3",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "statusVal": "",
        "statusType": "auto",
        "x": 780,
        "y": 180,
        "wires": []
    },
    {
        "id": "b43cb77a.8ffbd8",
        "type": "mqtt-broker",
        "name": "Broker MQTT",
        "broker": "localhost",
        "port": "1883",
        "clientid": "",
        "autoConnect": true,
        "usetls": false,
        "protocolVersion": "4",
        "keepalive": "60",
        "cleansession": true,
        "autoUnsubscribe": true,
        "birthTopic": "",
        "birthQos": "0",
        "birthPayload": "",
        "birthMsg": {},
        "closeTopic": "",
        "closePayload": "",
        "closeMsg": {},
        "willTopic": "",
        "willQos": "0",
        "willPayload": "",
        "willMsg": {},
        "userProps": "",
        "sessionExpiry": ""
    },
    {
        "id": "49c448cf338bd2d2",
        "type": "postgreSQLConfig",
        "name": "aiot_connection",
        "host": "127.0.0.1",
        "hostFieldType": "str",
        "port": "5432",
        "portFieldType": "num",
        "database": "aiot",
        "databaseFieldType": "str",
        "ssl": "false",
        "sslFieldType": "bool",
        "applicationName": "",
        "applicationNameType": "str",
        "max": "10",
        "maxFieldType": "num",
        "idle": "1000",
        "idleFieldType": "num",
        "connectionTimeout": "10000",
        "connectionTimeoutFieldType": "num",
        "user": "postgres",
        "userFieldType": "str",
        "password": "123456",
        "passwordFieldType": "str"
    }
]|



### Sistema de Alerta para Entrada de Clientes
Desarrollaremos un detector de entrada con sensores ultrasónicos y un buzzer activo que alertará al personal del estudio cuando un cliente entre al local. Este sistema mejorará la atención al cliente al permitirnos recibirlos de manera inmediata y personalizada, maximizando así las oportunidades de venta.

**Materiales**
| Material                | Precio (MXN) | Cantidad | Imagen |
|-------------------------|--------------|----------|--------|
| Placa ESP-32            | $250         | 1        | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/8ebe7e59-6268-4eae-b684-dd0d2acd6e15) |
| Sensores ultrasónicos   | $80          | 1        | ![ultrasonico](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/b20bad43-c1d6-4a52-987a-1e52206c94f2)|
| Buzzer activo           | $30          | 1        | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/de9b1723-fa49-4aa6-b563-6baa67a16618)|
| Protoboard              | $100         | 1        | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/8f81780f-abb6-4323-a1e3-15c5300124a7) |
| Cables                  | $100         | Varios   | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/dbef21da-1408-4371-a0a7-a4664cba8312) |

## Boceto

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/a3c3b2e6-9232-4335-b2b4-72fffbb46e6f)

## Conexión fritzing

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/d8c15a3e-a9de-4bb7-a349-05c51dc97cf0)

## Proceso construcción

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/09e13a82-9b8a-49ed-abf5-7ed780b73b2d)


### Control de Inventario con RFID
Implementaremos un sistema de control de inventario mediante RFID (Identificación por Radiofrecuencia). Colocaremos etiquetas RFID en los objetos del inventario y utilizaremos un sensor RFID para escanear estas etiquetas y mantener un registro en tiempo real de los objetos que entran o salen del local. Esto nos permitirá tener un control de inventario más preciso y reducir el riesgo de pérdidas.

**Materiales**
| Material                | Precio (MXN) | Cantidad | Imagen |
|-------------------------|--------------|----------|--------|
| Placa ESP-32            | $350         | 1        | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/8ebe7e59-6268-4eae-b684-dd0d2acd6e15) |
| Sensor RFID             | $150         | 1        | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/c56e9a4d-c73c-490c-a532-7d67760dcec7)|
| Etiquetas RFID          | $20          | 5        | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/5393b80b-5f70-4dfc-8b7f-214d6d4c3294)|
| Buzzer activo KY        | $30          | 1        | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/de9b1723-fa49-4aa6-b563-6baa67a16618) |
| Protoboard              | $100         | 1        | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/8f81780f-abb6-4323-a1e3-15c5300124a7) |
| Cables                  | $100         | Varios   | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/dbef21da-1408-4371-a0a7-a4664cba8312) |

## Boceto

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/3a58646c-79ca-4f23-b560-e5588fd511a8)

## Conexión fritzing

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/41b62a24-47db-469e-a06b-e332ed416e61)

## Proceso construcción

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/6952a0bf-3fac-4576-bed3-6be937968e7f)


### Mostrador Fotográfico Interactivo
Crearemos un mostrador fotográfico interactivo con un sensor PIR y un motor stepper. Cuando alguien se acerque al mostrador, el sensor PIR activará el motor stepper, poniendo en movimiento una base giratoria que exhibirá muestras fotográficas de los trabajos realizados. Este sistema ofrecerá una presentación dinámica y atractiva del portafolio del estudio, captando la atención de los clientes y promocionando de manera efectiva nuestros servicios fotográficos.

**Materiales**
| Material                | Precio (MXN) | Cantidad | Imagen |
|-------------------------|--------------|----------|--------|
| Placa ESP-32            | $350         | 1        | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/8ebe7e59-6268-4eae-b684-dd0d2acd6e15) |
| Sensor PIR              | $100         | 1        | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/941043c5-ed4a-4c24-aea6-b73fb3e73ba7)|
| Motor stepper           | $300         | 1        | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/398f7a7d-255c-4c30-9202-4006ed713986)|
| Protoboard              | $100         | 1        | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/8f81780f-abb6-4323-a1e3-15c5300124a7) |
| Cables                  | $50          | Varios   | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/dbef21da-1408-4371-a0a7-a4664cba8312) |

## Boceto

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/e6c000fd-43c2-4ce3-b355-ae34713cf552)


## Conexión fritzing

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/b7803074-29fe-4cad-93e9-b88968e4002e)

## Proceso construcción

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/f4c27265-d66f-42c5-9122-8a96f74443e2)


## Software
- Thonny
- Grafana
- Tinkercad
- Node-Red
- Fritzing
- Aplicación de la ESP-32 Cam
- 
## Conexión y Funcionalidad 
| ID  | Historia de Usuario                            | Prioridad | Estimación | Como Probarlo   | Responsable |
|-----|-----------------------------------------------|-----------|------------|-----------------|-------------|
| 1   | Conexiones del circuito utilizando Fritzzing    | Alta      | 2 horas    | Verificar las conexiones visuales en el software y confirmar que coinciden con el diseño del circuito. | Angel Huerta |
| 2   | Configuración de la Raspberry Pi y ESP32 para la comunicación inalámbrica | Alta | 3 horas | Verificar la conexión entre la Raspberry Pi y el ESP32 a través de la comunicación inalámbrica. | Jose Angel |
| 3   | Implementación de funcionalidades específicas en Raspberry Pi y ESP32 | Media | 5 horas | Verificar que las funcionalidades diseñadas se ejecuten correctamente en ambas plataformas. | Jose Angel y Angel Huerta |
