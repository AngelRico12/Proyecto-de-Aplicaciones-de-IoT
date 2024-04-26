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

## Sistema de seguridad y detección
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

### Boceto

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/ba4667d5-4543-46c4-8259-1a9011765fe9)

### Conexión fritzing

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/94b591ef-cefa-4812-b947-dd8efc48f10b)

### Proceso construcción

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/d531f2d8-c99e-435e-92f6-0ad39b77bea8)

### Nodos node-red

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/eef0dae9-e5cc-4538-b704-9ba4ee0663b3)

|![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/beb0e991-6ea7-41c2-9abf-e6627f99ff8a)|![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/a34024c7-7c4f-423d-96fd-a17bfdac9263)|![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/12bfbb4f-6d9e-45ad-a4f3-5af27a52cde3)
|

### Base de datos

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/a174c9fc-1f64-4887-81c1-490f2dcc5344)

### Video funcionamiento

https://drive.google.com/file/d/13jRXSBxbHsxH7EKlff8PnEvUKCuB4JGd/view?usp=drive_link

## Sistema de Alerta para Entrada de Clientes
Desarrollaremos un detector de entrada con sensores ultrasónicos y un buzzer activo que alertará al personal del estudio cuando un cliente entre al local. Este sistema mejorará la atención al cliente al permitirnos recibirlos de manera inmediata y personalizada, maximizando así las oportunidades de venta.

**Materiales**
| Material                | Precio (MXN) | Cantidad | Imagen |
|-------------------------|--------------|----------|--------|
| Placa ESP-32            | $250         | 1        | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/8ebe7e59-6268-4eae-b684-dd0d2acd6e15) |
| Sensores ultrasónicos   | $80          | 2        | ![ultrasonico](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/b20bad43-c1d6-4a52-987a-1e52206c94f2)|
| Buzzer activo           | $30          | 1        | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/de9b1723-fa49-4aa6-b563-6baa67a16618)|
| Protoboard              | $100         | 1        | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/8f81780f-abb6-4323-a1e3-15c5300124a7) |
| Cables                  | $100         | Varios   | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/dbef21da-1408-4371-a0a7-a4664cba8312) |

### Boceto

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/a3c3b2e6-9232-4335-b2b4-72fffbb46e6f)

### Conexión fritzing

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/d8c15a3e-a9de-4bb7-a349-05c51dc97cf0)

### Proceso construcción

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/09e13a82-9b8a-49ed-abf5-7ed780b73b2d)

### Nodos node-red

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/b2859deb-3986-4dc0-b1f8-792a4400b55a)

|![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/22888a1b-4abb-4f8a-ab16-fd4a3199161e)|![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/6ae970f1-37e1-4c60-ae13-1ad8b595ae67)
|![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/de2f324e-0ea6-42e9-8928-3b2077012fcc)|

### Base de datos

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/78eed271-e84c-48c4-8106-99f2fc6a8639)

### Video funcionamiento

https://drive.google.com/file/d/1kFupxTBYBXSfS1tc85ff3FBNZrJpzS2b/view?usp=drive_link

## Control de Inventario con RFID
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

### Boceto

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/3a58646c-79ca-4f23-b560-e5588fd511a8)

### Conexión fritzing

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/41b62a24-47db-469e-a06b-e332ed416e61)

### Proceso construcción

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/6952a0bf-3fac-4576-bed3-6be937968e7f)

### Nodos node-red

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/5a682811-8452-450b-a997-b563feb306da)

|![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/ebaad735-7525-4af8-86f0-ab6f22675ecc)|![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/21591f42-afd1-4b38-9b60-0e6e341a651b)
|![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/82352eb0-fd75-44d3-9d51-552ef05cef10)
|

### Base de datos

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/b5e76e26-705d-4c8f-940c-560f3045584f)

### Video de funcionamiento

https://drive.google.com/file/d/1w9sB0GDTlvqu20N9vn3VAbqZQgY9aVF2/view?usp=drive_link

## Mostrador Fotográfico Interactivo
Crearemos un mostrador fotográfico interactivo con un sensor PIR y un motor stepper. Cuando alguien se acerque al mostrador, el sensor PIR activará el motor stepper, poniendo en movimiento una base giratoria que exhibirá muestras fotográficas de los trabajos realizados. Este sistema ofrecerá una presentación dinámica y atractiva del portafolio del estudio, captando la atención de los clientes y promocionando de manera efectiva nuestros servicios fotográficos.

**Materiales**
| Material                | Precio (MXN) | Cantidad | Imagen |
|-------------------------|--------------|----------|--------|
| Placa ESP-32            | $350         | 1        | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/8ebe7e59-6268-4eae-b684-dd0d2acd6e15) |
| Sensor PIR              | $100         | 1        | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/941043c5-ed4a-4c24-aea6-b73fb3e73ba7)|
| Motor stepper           | $300         | 1        | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/398f7a7d-255c-4c30-9202-4006ed713986)|
| Protoboard              | $100         | 1        | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/8f81780f-abb6-4323-a1e3-15c5300124a7) |
| Cables                  | $50          | Varios   | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/dbef21da-1408-4371-a0a7-a4664cba8312) |
| Display                 | $60          | 1        | ![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/82f96719-8c6f-4ac5-a2a1-630fb65fbb6b)|

### Boceto

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/e6c000fd-43c2-4ce3-b355-ae34713cf552)


### Conexión fritzing

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/b7803074-29fe-4cad-93e9-b88968e4002e)

### Proceso construcción

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/f4c27265-d66f-42c5-9122-8a96f74443e2)

### Nodos node-red

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/939644c4-8d7a-4065-87d2-f8692c674f18)

|![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/4f6b4796-8924-437c-8f29-8c0a150135c1)|![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/6407648f-35f6-4eff-b17e-1209f13d4b0c)
|![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/4624546d-2133-47aa-8bcc-9628a8f32402)
|

### Base de datos

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/101e6f60-a8b0-4a99-be88-b67134115aee)

### Video funcionamiento

https://drive.google.com/file/d/1X5rBK6hsIS6Cf4ui32ePP9qBTa1jJbnJ/view?usp=drive_link

## Software Utilizado
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
| 2   | Configuración de la Raspberry Pi y ESP32 para la comunicación inalámbrica | Media | 3 horas | Verificar la conexión entre la Raspberry Pi y el ESP32 a través de la comunicación inalámbrica. | Jose Angel |
| 3   | Implementación de funcionalidades específicas en Raspberry Pi y ESP32 | Alta | 5 horas | Verificar que las funcionalidades diseñadas se ejecuten correctamente en ambas plataformas. | Jose Angel y Angel Huerta |
| 4   | Integración de sensores ultrasónicos en el circuito ESP32-CAM  | Alta      | 4 horas    | Verificar que los sensores ultrasónicos estén correctamente conectados al circuito ESP32-CAM y que proporcionen lecturas precisas de la distancia. | Jose Angel |
| 5   | Configuración del sistema de detección de entrada con sensores ultrasónicos y buzzer activo   | Alta | 4 horas | Probar la detección de entrada al local mediante los sensores ultrasónicos y verificar que el buzzer activo emita una alerta adecuada al detectar la presencia de un cliente. | Jose Angel |
| 6   | Implementación del sistema de control de inventario mediante RFID  | Alta | 6 horas | Verificar que el sistema de control de inventario con RFID esté correctamente configurado y que registre con precisión la entrada y salida de objetos del local. | Jose Angel |
| 7   | Desarrollo del mostrador fotográfico interactivo con sensor PIR y motor stepper | Alta | 8 horas | Probar la interacción del sensor PIR con el motor stepper para asegurarse de que el mostrador fotográfico se active de manera adecuada cuando un cliente se acerque y exhiba las muestras fotográficas de forma dinámica. | Jose Angel y Angel Huerta |
| 8   | Implementación de software de monitoreo y control (Thonny, Grafana, Node-Red) | Media | 6 horas | Verificar que el software de monitoreo y control esté instalado y configurado correctamente en las plataformas pertinentes (Raspberry Pi, ESP32) y que proporcione una interfaz fácil de usar para gestionar los sistemas domóticos. | Angel Huerta |

### Video agradecimiento

https://drive.google.com/file/d/147XoIXfEQK7N2dSqAHOD07JSAA2tIm6a/view?usp=drive_link

### Carta de satisfacción firmada

![image](https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/assets/137667970/b3669434-d5c4-4f0e-b430-a7a99382340c)
