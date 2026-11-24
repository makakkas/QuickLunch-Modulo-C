# QuickLunch – Módulo C: Cocina

Sistema de gestión y seguimiento de pedidos para el área de Cocina de QuickLunch, desarrollado como parte del proyecto QuickLunch EV3.

## Descripción del proyecto

El Módulo C de QuickLunch está orientado a la gestión de pedidos que deben ser preparados por el personal de Cocina. Su propósito es facilitar la visualización, organización y seguimiento de los pedidos confirmados, permitiendo conocer su estado de preparación y consultar las cantidades totales de productos que deben elaborarse durante una jornada.

El módulo permite consultar pedidos según su fecha de servicio, filtrar por estado de preparación, actualizar el progreso de los pedidos y generar un consolidado de productos. También contempla un sistema de permisos para restringir el acceso a las funcionalidades del área de Cocina.

Este desarrollo busca mantener una estructura organizada, separando la lógica del sistema, la interacción con la base de datos y la interfaz utilizada por los trabajadores.

---

## ¿Por qué elegimos Python y Django?

### Python

Python fue seleccionado como lenguaje de programación debido a su sintaxis clara, facilidad de lectura y flexibilidad para desarrollar aplicaciones. Estas características permiten trabajar con la lógica del sistema de manera más ordenada, facilitando tanto el desarrollo como el mantenimiento del código.

Además, Python dispone de una amplia comunidad, documentación y herramientas que permiten resolver problemas durante el desarrollo y ampliar las funcionalidades del proyecto.

En QuickLunch, Python se utiliza principalmente para implementar la lógica del sistema, validar las operaciones realizadas sobre los pedidos, gestionar los estados de preparación y procesar la información obtenida desde la base de datos.

### Django

Para el desarrollo del backend se eligió Django, un framework web basado en Python que proporciona una estructura de desarrollo y herramientas integradas para construir aplicaciones web.

La elección de Django se debe principalmente a que permite trabajar de forma organizada con diferentes componentes del sistema, como modelos, vistas, rutas, autenticación, permisos, plantillas y conexión con bases de datos.

En lugar de implementar desde cero funcionalidades comunes de una aplicación web, Django permite aprovechar componentes existentes, facilitando el desarrollo y reduciendo la cantidad de código necesario para implementar funcionalidades básicas.

Dentro del Módulo C aprovechamos principalmente:

- **ORM de Django:** permite interactuar con la base de datos mediante modelos y consultas desde Python.
- **Sistema de autenticación:** permite trabajar con usuarios registrados.
- **Grupos y permisos:** permiten controlar el acceso a las funcionalidades según el rol del usuario.
- **Sistema de vistas:** permite procesar solicitudes y entregar información al usuario.
- **Sistema de plantillas:** permite integrar la información del backend con páginas HTML.
- **Migraciones:** permiten gestionar los cambios realizados en la estructura de la base de datos.

---

## Tecnologías utilizadas

| Tecnología | Uso dentro del proyecto |
|---|---|
| Python | Lenguaje utilizado para desarrollar la lógica del sistema. |
| Django | Framework utilizado para desarrollar el backend y organizar la aplicación web. |
| MySQL | Base de datos relacional utilizada para almacenar la información del módulo. |
| XAMPP | Entorno utilizado para administrar y ejecutar el servidor MySQL localmente. |
| phpMyAdmin | Herramienta utilizada para administrar la base de datos mediante una interfaz web. |
| HTML | Utilizado para estructurar las páginas del módulo. |
| CSS | Utilizado para diseñar y dar formato a la interfaz de Cocina. |
| Git | Sistema de control de versiones utilizado para registrar los cambios del proyecto. |
| GitHub | Plataforma utilizada para almacenar y compartir el repositorio del proyecto. |

---

## Base de datos

### MySQL

Se utiliza MySQL como sistema de gestión de bases de datos relacionales, debido a que la información del módulo mantiene relaciones entre distintas entidades.

Por ejemplo, un pedido puede contener múltiples detalles, cada detalle está asociado a un producto y los pedidos también mantienen información relacionada con el usuario que los registra.

El uso de una base de datos relacional permite organizar esta información, mantener relaciones entre registros y realizar consultas para obtener los pedidos y las cantidades de productos necesarias para la preparación.

### XAMPP y phpMyAdmin

XAMPP se utiliza como entorno local para ejecutar MySQL, mientras que phpMyAdmin permite administrar la base de datos de forma gráfica.

Estas herramientas facilitan la creación, consulta y revisión de los registros utilizados durante el desarrollo y las pruebas del módulo.

### Base de datos utilizada

- **Motor:** MySQL
- **Entorno local:** XAMPP
- **Administración:** phpMyAdmin

---

## Arquitectura del sistema

El módulo se desarrolló utilizando una estructura basada en Django, separando los componentes encargados de gestionar los datos, procesar las solicitudes, ejecutar la lógica de negocio y presentar la información.

Se utiliza una organización basada en el patrón MTV de Django (Model - Template - View), incorporando además una capa de servicios para centralizar la lógica de negocio.

### Modelo – Model

Los modelos representan las entidades que se almacenan en la base de datos y permiten establecer relaciones entre ellas.

Los modelos principales desarrollados para el módulo son:

- **Producto:** almacena la información de los productos.
- **Pedido:** contiene información general del pedido, usuario asociado, fecha de servicio y estados.
- **DetallePedido:** relaciona los pedidos con sus productos y cantidades.
- **EstadoPreparacion:** registra los cambios realizados en el estado de preparación de los pedidos.
- **Historial:** permite registrar acciones realizadas dentro del sistema.

Los modelos permiten trabajar con la información mediante el ORM de Django, facilitando la consulta, creación y modificación de registros.

### View – Vistas

Las vistas son responsables de recibir las solicitudes del usuario, procesar la información necesaria y entregar las respuestas correspondientes.

En el módulo se desarrollan vistas para:

- Visualizar pedidos del área de Cocina.
- Consultar pedidos según la fecha de servicio.
- Filtrar pedidos por estado de preparación.
- Consultar el consolidado de productos.
- Actualizar el estado de preparación de los pedidos.

Las vistas también permiten integrar la lógica de los servicios con las plantillas HTML.

### Template – Plantillas

Las plantillas HTML se utilizan para presentar la información obtenida desde las vistas.

Dentro del módulo se desarrollaron interfaces para la visualización y gestión de pedidos, junto con una página dedicada al consolidado de productos.

Las plantillas permiten mostrar los datos de manera organizada, facilitando la interacción del personal de Cocina con el sistema.

### Capa de servicios

Además de la estructura tradicional de Django, se incorporó una capa de servicios para centralizar las operaciones y reglas de negocio.

Esta separación permite evitar que toda la lógica se encuentre directamente dentro de las vistas.

La capa de servicios se utiliza para:

- Verificar permisos antes de ejecutar operaciones.
- Obtener el consolidado de productos.
- Gestionar los cambios de estado de los pedidos.
- Validar las transiciones permitidas.
- Controlar las operaciones que requieren justificación.
- Registrar los cambios realizados sobre los pedidos.

Esta organización permite que las vistas se concentren principalmente en gestionar las solicitudes y respuestas, mientras que los servicios se encargan de ejecutar las operaciones correspondientes.

---

## Estructura del proyecto

La organización actual del proyecto se basa en la separación de archivos y componentes de Django.

```text
modulo_cocina/
│
├── Cocinaapp/
│   ├── migrations/
│   ├── static/
│   │   └── Cocinaapp/
│   │       └── cocina.css
│   │
│   ├── templates/
│   │   └── Cocinaapp/
│   │       ├── pedidos.html
│   │       └── consolidado.html
│   │
│   ├── admin.py
│   ├── decorators.py
│   ├── models.py
│   ├── services.py
│   ├── views.py
│   └── urls.py
│
├── modulo_cocina/
│   ├── settings.py
│   └── urls.py
│
└── manage.py
```

### Descripción de los archivos principales

| Archivo | Responsabilidad |
|---|---|
| `models.py` | Define las entidades y relaciones de la base de datos. |
| `views.py` | Gestiona las solicitudes, consultas y respuestas de las páginas. |
| `services.py` | Centraliza la lógica de negocio y las operaciones del módulo. |
| `decorators.py` | Contiene mecanismos de restricción de acceso por rol. |
| `urls.py` | Define las rutas disponibles dentro de la aplicación. |
| `admin.py` | Permite administrar los modelos desde Django Admin. |
| `pedidos.html` | Interfaz para visualizar y gestionar los pedidos. |
| `consolidado.html` | Interfaz para visualizar el consolidado de productos. |
| `cocina.css` | Contiene los estilos visuales del módulo. |
| `settings.py` | Contiene la configuración general del proyecto Django. |
| `manage.py` | Herramienta de administración del proyecto Django. |

---

## Funcionalidades desarrolladas

### Gestión y visualización de pedidos

El módulo permite visualizar los pedidos confirmados que corresponden a una fecha de servicio determinada.

La consulta permite organizar los pedidos para que el personal de Cocina pueda revisar la información necesaria para su preparación.

Se contempla:

- Consulta de pedidos según fecha de servicio.
- Visualización de información asociada al pedido.
- Visualización de productos y cantidades.
- Filtrado por estado de preparación.
- Exclusión de pedidos cancelados de la vista de preparación.

### Gestión de estados de preparación

Se implementa un flujo de preparación que permite realizar seguimiento al progreso de los pedidos.

Los estados considerados son:

- `pendiente`
- `en_preparacion`
- `preparado`

El sistema contempla validaciones para evitar saltos de estados y cambios repetidos innecesarios.

También se contempla la posibilidad de retroceder un estado mediante una justificación, de acuerdo con las reglas implementadas en la lógica de negocio.

### Consolidado de productos

El módulo cuenta con una funcionalidad para agrupar las cantidades de productos correspondientes a los pedidos confirmados de una fecha determinada.

El consolidado permite conocer la cantidad total de cada producto que debe prepararse, evitando revisar individualmente todos los pedidos para realizar el cálculo.

La información se obtiene mediante consultas al ORM de Django y agrupaciones de datos en la base de datos.

Los pedidos cancelados son excluidos del consolidado.

### Control de acceso por roles

El módulo utiliza el sistema de grupos de Django para controlar el acceso a las funcionalidades.

Se consideran los siguientes grupos:

- **Cocina:** permite acceder a las funcionalidades de gestión de pedidos y preparación.
- **Trabajador:** corresponde a un rol que no debe acceder a las funcionalidades restringidas del módulo Cocina.

Se implementan verificaciones de permisos para evitar que usuarios sin autorización accedan a las vistas protegidas.

### Registro de cambios

Se contempla el registro de las modificaciones realizadas sobre los estados de preparación.

Estos registros permiten mantener información relacionada con los cambios efectuados, incluyendo el estado anterior, el estado nuevo, el usuario responsable, la fecha y hora del cambio y, cuando corresponde, la justificación.

---

## Diseño de interfaz

La interfaz del módulo fue desarrollada utilizando HTML y CSS, buscando mantener una presentación ordenada y facilitar el trabajo del personal de Cocina.

Se implementó una estructura visual que incluye:

- Panel lateral de navegación.
- Encabezado de la página.
- Tarjetas informativas.
- Filtros de fecha y estado.
- Tabla de pedidos.
- Indicadores visuales de estados.
- Botones de acciones.
- Tabla de consolidado de productos.
- Mensajes de confirmación y error.
- Adaptaciones para diferentes tamaños de pantalla.

La interfaz busca facilitar la visualización de la información y permitir que las acciones principales puedan realizarse de manera sencilla.

---

## Seguridad y validaciones

Durante el desarrollo se consideran distintos mecanismos de validación para proteger las operaciones del módulo.

Entre ellos:

- Restricción de acceso mediante grupos de Django.
- Validación de roles antes de ejecutar operaciones de negocio.
- Protección de operaciones mediante solicitudes POST.
- Validación de los estados permitidos.
- Control de transiciones entre estados.
- Exigencia de justificación en retrocesos.
- Control de operaciones sobre pedidos cancelados.
- Uso de transacciones para operaciones que modifican información relacionada.
- Uso de consultas ORM para interactuar con la base de datos.

Estas medidas contribuyen a mantener un comportamiento consistente y a evitar modificaciones no autorizadas o inválidas.

---

## Flujo general de funcionamiento

El funcionamiento general del módulo puede representarse de la siguiente manera:

1. El usuario accede al módulo Cocina.
2. Django verifica que el usuario tenga los permisos correspondientes.
3. La vista consulta los pedidos de la fecha seleccionada.
4. Los datos se obtienen desde MySQL mediante el ORM.
5. La información es enviada a la plantilla HTML.
6. El usuario visualiza los pedidos y sus estados.
7. Cuando se realiza una acción, la vista recibe la solicitud.
8. La capa de servicios valida los permisos y las reglas de negocio.
9. Se actualizan los registros correspondientes en la base de datos.
10. Se registra la información del cambio.
11. La interfaz muestra el resultado de la operación.

---

## Control de versiones

El proyecto utiliza Git como sistema de control de versiones y GitHub como plataforma de almacenamiento del repositorio.

Esto permite mantener un registro de los cambios realizados durante el desarrollo, facilitar el respaldo del código y compartir los avances del módulo.

Repositorio:

[QuickLunch – Módulo C](https://github.com/makakkas/QuickLunch-Modulo-C)

---

## Objetivo del módulo

El objetivo del Módulo C es proporcionar una herramienta que permita al área de Cocina gestionar y visualizar los pedidos confirmados, realizar seguimiento a su preparación y obtener un consolidado de productos según la fecha de servicio.

El desarrollo busca mantener una estructura organizada, aplicar separación de responsabilidades, implementar control de acceso y facilitar la administración de las operaciones relacionadas con la preparación de pedidos.

---

## Estado del desarrollo

El módulo se encuentra en desarrollo incremental. Se han implementado la estructura principal, los modelos, la conexión con la base de datos, la gestión de roles, las vistas, la capa de servicios y las interfaces de visualización y consolidado.

Las pruebas funcionales, la validación integral de permisos, el historial consultable y las verificaciones finales se continuarán desarrollando conforme avance el proyecto.

---

**Proyecto:** QuickLunch  
**Módulo:** C – Cocina  
**Tecnologías principales:** Python, Django, MySQL, HTML y CSS  
**Repositorio:** GitHub
