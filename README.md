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
| Placa ESP-32            | $250         | 1        | [Imagen] |
| ESP-32 Cam              | $250         | 1        | [Imagen] |
| Controlador ESP32-Cam   | $100         | 1        | [Imagen] |
| Protoboard              | $50          | 1        | [Imagen] |
| Motor servo             | $70          | 1        | [Imagen] |
| Cables                  | $100         | Varios   | [Imagen] |

## Boceto

[https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/blob/main/imagenes/Boceto%201.jpeg]

### Sistema de Alerta para Entrada de Clientes
Desarrollaremos un detector de entrada con sensores ultrasónicos y un buzzer activo que alertará al personal del estudio cuando un cliente entre al local. Este sistema mejorará la atención al cliente al permitirnos recibirlos de manera inmediata y personalizada, maximizando así las oportunidades de venta.

**Materiales**
| Material                | Precio (MXN) | Cantidad | Imagen |
|-------------------------|--------------|----------|--------|
| Placa ESP-32            | $250         | 1        | [Imagen] |
| Sensores ultrasónicos   | $80          | 2        | [Imagen] |
| Buzzer activo           | $30          | 1        | [Imagen] |
| Protoboard              | $100         | 1        | [Imagen] |
| Cables                  | $100         | Varios   | [Imagen] |

## Boceto

https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/blob/main/imagenes/Boceto%202.jpeg


### Control de Inventario con RFID
Implementaremos un sistema de control de inventario mediante RFID (Identificación por Radiofrecuencia). Colocaremos etiquetas RFID en los objetos del inventario y utilizaremos un sensor RFID para escanear estas etiquetas y mantener un registro en tiempo real de los objetos que entran o salen del local. Esto nos permitirá tener un control de inventario más preciso y reducir el riesgo de pérdidas.

**Materiales**
| Material                | Precio (MXN) | Cantidad | Imagen |
|-------------------------|--------------|----------|--------|
| Placa ESP-32            | $350         | 1        | [Imagen] |
| Sensor RFID             | $150         | 1        | [Imagen] |
| Etiquetas RFID          | $20          | Varios   | [Imagen] |
| Buzzer activo KY        | $30          | 1        | [Imagen] |
| Protoboard              | $100         | 1        | [Imagen] |
| Cables                  | $100         | Varios   | [Imagen] |

## Boceto

https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/blob/main/imagenes/Boceto%203.jpeg


### Mostrador Fotográfico Interactivo
Crearemos un mostrador fotográfico interactivo con un sensor PIR y un motor stepper. Cuando alguien se acerque al mostrador, el sensor PIR activará el motor stepper, poniendo en movimiento una base giratoria que exhibirá muestras fotográficas de los trabajos realizados. Este sistema ofrecerá una presentación dinámica y atractiva del portafolio del estudio, captando la atención de los clientes y promocionando de manera efectiva nuestros servicios fotográficos.

**Materiales**
| Material                | Precio (MXN) | Cantidad | Imagen |
|-------------------------|--------------|----------|--------|
| Placa ESP-32            | $350         | 1        | [Imagen] |
| Sensor PIR              | $100         | 1        | [Imagen] |
| Motor stepper           | $300         | 4        | [Imagen] |
| Protoboard              | $100         | 2        | [Imagen] |
| Cables                  | $50          | Varios   | [Imagen] |

## Boceto

https://github.com/AngelRico12/Proyecto-de-Aplicaciones-de-IoT/blob/main/imagenes/Boceto%204.jpeg


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
| 1   | Conexiones del circuito utilizando Fritzzing    | Alta      | 2 horas    | Verificar las conexiones visuales en el software y confirmar que coinciden con el diseño del circuito. | [Nombre del Responsable] |
| 2   | Configuración de la Raspberry Pi y ESP32 para la comunicación inalámbrica | Alta | 3 horas | Verificar la conexión entre la Raspberry Pi y el ESP32 a través de la comunicación inalámbrica. | [Nombre del Responsable] |
| 3   | Implementación de funcionalidades específicas en Raspberry Pi y ESP32 | Media | 5 horas | Verificar que las funcionalidades diseñadas se ejecuten correctamente en ambas plataformas. | [Nombre del Responsable] |
