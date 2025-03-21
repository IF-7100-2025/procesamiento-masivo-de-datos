# Proyecto de Investigación

## Part 1: ¿Qué son Katas de Ingeniería de Software?

Kata es una palabra japonesa que significa "forma" o "modelo". Se refiere a un patrón de coreografía detallado de movimientos de artes marciales que se hacen para practicar solo. [[Wikipedia, 2024]](https://es.wikipedia.org/wiki/Kata). [Dave Thomas](https://pragdave.me/) incorporó este concepto a la programación mientras veía a su hijo practicar Karate, llamándolo ["Code Kata"](http://codekata.com/). La idea es que los programadores practiquen ejercicios de programación para mejorar sus habilidades. Eventualmente, [Ted Neward](https://www.linkedin.com/in/tedneward/) propuso el término ["Architectural Kata"](https://www.architecturalkatas.com/)[Richard,Ford, 2020], en este caso la idea es que los arquitectos practiquen elaborar una arquitectura. Ambos conceptos consisten en atacar un determinado problema en un ambiente controlado, con el fin de mejorar habilidades y conocimientos en un área específica con un límite de tiempo, generalmente media hora o una hora.

Ambos conceptos son bastante útiles para practicar sus respectivos campos, uno es meramente para resolver tareas específicas como un problema de modelaje de datos o un algoritmo(Code Kata) y el otro resuelve problemas de arquitectura de software(Architectural Kata). Hay un segmento que queda sin cubrir que es separado por la difusa línea que existe entre un Arquitecto de Software y un Desarrollador de Software. Tal vez más difusa está entre este último y un Programador. Al final de cuentas esto ha sido tema de discusiones interminables en la comunidad de desarrollo de software. Dada la necesidad de fortalecer las habilidades tanto en diseño como en la estructuración de código y resolución de algoritmos, se propone la realización de realizar "Engineering Kata".

Una "Engineering Kata" tendría el mismo fundamento de una "Code Kata" pero con un enfoque más amplio. En lugar de resolver un problema específico, se resolverá un problema común en el desarrollo de software, que abarque una solución más extendida en términos de funcionalidad. La idea es que el estudiante pueda practicar la resolución de problemas comunes en el desarrollo de software, pero con un enfoque más amplio que el de un "Code Kata". Pero con un enfoque más específico que el de un "Architectural Kata". Aplicando conceptos de programación, diseño de software y arquitectura de software. Dado esto se propone ampliar el tiempo empleado en la realización de esta más tiempo que las katas propuestas por Thomas y Neward. Se sugiere asignar el tiempo dependiendo del problema.

### Kata

Cada kata representa un caso a resolver:

- Primera sección: indica las características arquitectónicas que se deben priorizar en la solución propuesta.
- Segunda sección: introduce el contexto del problema.
- Tercera sección: presenta el problema a resolver.
- Cuarta sección: presenta las condiciones necesarias para resolver el problema. Aquí se indican algunas limitantes e indicaciones a seguir tanto para el planteamiento como la solución del problema. En algunos casos hay que generar algunos artefactos que están fuera del alcance del problema con el fin de obtener su planteamiento.
- Quinta sección: presenta los parámetros de evaluación de la solución.
- Sexta sección: presenta notas adicionales que se deben considerar al momento de resolver el problema.

### Listado de Katas

- [Cobro de Pasajes](cobro-de-pasajes.md)
- [Envío de mensajes servidor cliente](envío-de-mensajes-servidor-cliente.md)
- [Información compartida entre servicios](información-compartida-entre-servicios.md)
- [Interacción de transacciones](interacción-de-transacciones.md)
- [Optimización de imágenes](optimización-de-imágenes.md)
- [Paginación](paginación.md)
- [Procesamiento masivo de datos](procesamiento-masivo-de-datos.md)
- [Seguridad en repositorio de archivos en la nube](seguridad-en-repositorio-de-archivos-en-la-nube.md)

### Características arquitectónicas

Siendo muy ambigüo el realizar una valoración cuantitativa de las características arquitectónicas en cada Kata se ha definido métricas a modo de referencia, el objetivo es lograr cumplir las métricas establecidas, sin embargo, puede darse el caso de que alguna métrica no se cumpla, pero la solución obtenida sea satisfactoria. De igual manera todo se debe justificar en las conclusiones del proyecto.

- Performance: Se refiere a la eficiencia del sistema en términos de velocidad de respuesta, uso de recursos y capacidad de manejar cargas de trabajo
- Maintainability: Se refiere a la facilidad con la que se puede mantener y actualizar el sistema. Esto incluye la facilidad para identificar y corregir defectos, adaptar el sistema a nuevos requisitos y hacer que el mantenimiento futuro sea más fácil.
- Testability: Se refiere a la facilidad con la que se pueden probar las funcionalidades del sistema para asegurar que funcionan como se espera.
- Usability: Se refiere a la facilidad de uso del sistema por parte de los usuarios.
- Scalability: Se refiere a la capacidad del sistema para manejar un creciente volumen de trabajo añadiendo recursos al sistema.
- Reliability: Se refiere a la capacidad del sistema para realizar su función requerida, bajo condiciones dadas, durante un período de tiempo específico.
- Security: Se refiere a la capacidad del sistema para proteger la información y los datos contra el acceso no autorizado y otras amenazas.
- Performance: Se refiere a la necesidad de asegurar que los datos sean precisos y consistentes a lo largo de todo el sistema.
- Data Consistency: Se refiere a la necesidad de asegurar que los datos sean precisos y consistentes a lo largo de todo el sistema.

## Proyecto de Investigación

### Introducción

Este proyecto de investigación explorará diversos temas relacionados con la ingeniería de software. Enfocados en realizar problemas comunes que pueden presentarse en un proyecto tradicional de software propuestos en las "Engineering Katas". La motivación de este proyecto es enfatizar en la solución de problemas comunes que se presentan durante el desarrollo. Estos problemas no están relacionados con objetivos de negocio, sino más bien con problemas técnicos que se presentan al momento de diseñar y desarrollar una funcionalidad. Sin embargo, se deben considerar las limitaciones impuestas en cada uno de ellos que pueden ser impuestas por alguna restricción de negocio o fuera del alcance de la aplicación en cuestión.

### Objetivos

- Identificar una solución a un problema común en el desarrollo de software.
- Realizar un análisis de la solución propuesta en función de características arquitectónicas.
- Implementar una solución utilizando una o varias tecnologías específicas.
- Analizar los resultados obtenidos desde el punto de vista arquitectónico.
- Implementar un plan de pruebas enfocado en las características arquitectónicas.

### Metodología

Se debe seleccionar una de las katas propuestas en la sección siguiente. Se deberá desarrollar el problema de acuerdo a los puntos solicitados. Para este desarrollo deberá identificar dos tecnologías. Estas dos tecnologías deberán complementarse para generar una solución al problema dado. La elección de las tecnologías como de los problemas quedará a convenio entre el profesor y los y las estudiantes.

### Procedimiento

El proyecto se debe realizar en grupos de tres personas(No se aceptarán grupos de dos a no ser que exista algún motivo de fuerza mayor).
Para elaborar el proyecto de investigación, se deberá seguir el siguiente procedimiento:

- Registre el grupo [aquí](https://forms.gle/NPMdh8pjxnuuniiX6)
- El problema se le asignará en convenio con el profesor y colegas de clase.
- Identificar dos tecnologías que se puedan complementar para proponer una solución al problema. Podrán ser desde lenguajes de programación no vistos en el curso anterior hasta frameworks o librerías.
- Proponer las tecnologías a utilizar en la segunda semana de clases para ser **aprobadas** el jueves 21 de marzo.
- Fecha de Entrega: 23 de mayo 5 pm. Todos los documentos(incluyendo presentación) deben estar completos antes de la fecha indicada y llenar el [siguiente formulario](https://forms.gle/g941QshacaiaeFdz5).
- Presentar los resultados de la investigación: Se realizará entre la semana del 27 de mayo al 01 de junio(Día por definir a discreción por profesor y estudiantes).

### Artefactos a entregar

- Pull Request en el repositorio de documentación del curso bajo el directorio `investigación/grupo-##-{nombre-del-caso-sin-llaves-y-separado-por-guiones}`:
    - Documento formal sobre su investigación.
        - Explicación de las dos tecnologías implementadas, destacar características principales y aplicaciones.
        - Explicación del problema propuesto.
        - Explicación de la solución propuesta: Utilizar recursos visuales(UML) y escritos para explicar la solución.
        - Presentar un plan de pruebas para obtener métricas sobre la implementación.
        - Resultados de ejecución del plan de pruebas: Involucra métricas obtenidas, resultados de pruebas manuales y automáticas.
    - Realizar una presentación donde se expongan:
        - Las tecnologías seleccionadas. Puntos claves para entender la tecnología.
        - El problema propuesto.
        - La solución propuesta.
        - Los resultados obtenidos.
        - Conclusiones.
- Repositorio de código fuente(se creará el repositorio dentro de la organización del GitHub), donde contenga:
    - Todo el código fuente de la solución propuesta: Incluyendo la implementación de cada tecnología separada por directorios.
    - Este repositorio será solamente de código fuente, el aporte de cada ingeniero deberá ser equitativo. Debe tener una distribución equitativa de cantidad de código propuesto por cada ingeniero.

### Consideraciones adicionales

- La investigación deberá realizarse en grupos de tres personas.
- El trabajo de programación deberá ser equitativo entre los miembros del equipo(Lo ideal ~33% por cada estudiante). La idea es incentivar la práctica de la programación.
  **Se debe notificar al profesor con antelación cualquier circunstancia extraordinaria donde la distribución no sea
  equitativa con antelación, de lo contrario se procederá con una penalización del 50% de la nota final para los tres
  integrantes**.
- Se deben respetar las fechas de entrega.
- El plagio será sancionado según las normativas de la universidad, esto incluye el uso de inteligencia artificial generativa.

## Rubros de calificación

| Rubro                                    | Porcentaje |
|------------------------------------------|------------|
| Presentación del proyecto*               | **20%**    |
| - Manejo del tema                        | 10%        |
| - Manejo del tiempo                      | 5%         |
| - Coordinación grupal                    | 5%         |
| Implementación de la solución propuesta* | **45%**    |
| - Completitud de la solución**           | 25%        |
| - Ejecución/Codificación de pruebas      | 10%        |
| - Distribución de trabajo                | 5%         |
| - Limpieza de código***                  | 5%         |
| Informe*                                 | **30%**    |
| - Explicación de ambas tecnologías       | 10%        |
| - Explicación de solución propuesta      | 10%        |
| - Plan de pruebas                        | 5%         |
| - Ejecución de pruebas                   | 5%         |
| Validación de fuentes*                   | **5%**     |

### Puntos a considerar

- (\*) La ausencia de cualquier rubro será penalizada con la anulación total del trabajo.
- (**) Debe tener la participación similar en cuanto el aporte de código de cada estudiante.
- (***)Limpieza de código se refiere a aplicación de buenas prácticas de programación:
  - Nombres de variables y funciones descriptivos.
  - Uso de comentarios para explicar partes del código que no sean obvias.
  - Omitir código muerto(Comentado y/o que no se usa).
  - No usar comentarios para explicar código obvio.
  - Métodos/Funciones no deben tener más de 20 líneas de código.
- 

## Referencias Bibliográficas

- Wikipedia contributors. (2024, 19 enero). Kata. Wikipedia. https://en.wikipedia.org/wiki/Kata
- Thomas, D. (2024, 19 enero). Code Kata. Code Kata. http://codekata.com/
- Neward, T. (2024, 19 enero). Architectural Kata. Architectural Kata. https://www.architecturalkatas.com/
- Richards, M., & Ford, N. (2020). Fundamentals of Software Architecture: An Engineering Approach. https://openlibrary.org/books/OL28265072M/Fundamentals_of_Software_Architecture