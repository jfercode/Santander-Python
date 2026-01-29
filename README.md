# Curso de Python Santander

## Descripción General

Este repositorio contiene una colección completa y estructurada de scripts de Python creados como parte del **Curso de Python de Santander Open Academy**. El proyecto sirve como un recurso educativo profesional con ejemplos prácticos, bien documentados y listos para ejecutar.

## Propósito

El objetivo principal de este proyecto es:
- **Aprender Fundamentales**: Consolidar el conocimiento de los conceptos básicos de Python
- **Documentar Conceptos**: Proporcionar ejemplos claros, ejecutables y bien comentados
- **Construir Bases Sólidas**: Crear una base sólida en programación Python
- **Material de Referencia**: Servir como guía de referencia para futuros proyectos
- **Código Profesional**: Seguir estándares de código limpio y organizado

## Estructura del Proyecto

```
Santander-Python/
├── README.md                      # Este archivo
├── LICENSE                        # Licencia MIT del proyecto
│
├── 01/ - Fundamentos de Python (12 archivos)
│   ├── Introduction.py            # Conceptos básicos y sintaxis
│   ├── Fundaments.py              # Tipos de datos (int, float, str, bool)
│   ├── Variables.py               # Declaración y reglas de nombres
│   ├── Operators.py               # Operadores aritméticos, comparación y lógicos
│   ├── ControlStructures.py       # Condicionales (if, elif, else)
│   ├── Loops.py                   # Bucles (for, while, break, continue)
│   ├── DataStructures.py          # Listas y Tuplas
│   ├── Dictionaries.py            # Diccionarios y operaciones clave-valor
│   ├── Tuples.py                  # Tuplas en detalle
│   ├── List.py                    # Listas en detalle
│   └── Sets.py                    # Conjuntos y operaciones
│
├── 02/ - Tópicos Avanzados (9 archivos)
    ├── Functions.py               # Definición, parámetros, retornos
    ├── ErrorHandling.py           # Try-except-finally fundamentals
    ├── Exceptions.py              # Mecanismos de excepciones
    ├── CustomExceptions.py        # Crear excepciones personalizadas
    ├── InputOutput.py             # Entrada/salida del usuario
    ├── FileOperations.py          # Leer y escribir archivos
    ├── Modules.py                 # Módulos y la librería estándar
    ├── CustomModules.py           # Crear módulos personalizados
    └── Packages.py                # Organización en paquetes

```

## Contenido del Curso

### 📚 Carpeta 01 - Fundamentos de Python

#### Introduction.py
- Ejecución de scripts Python
- Conceptos básicos del lenguaje
- Comentarios (una línea y multi-línea)
- Variables y tipos de datos básicos
- Case sensitivity (sensibilidad a mayúsculas)
- Precedencia de operadores
- Condicionales básicos (if-else)
- Entrada/salida de datos

#### Fundaments.py
- **Números Enteros (int)**: Números enteros, positivos y negativos
- **Números Decimales (float)**: Números con punto decimal
- **Cadenas de Texto (str)**: Texto, caracteres especiales, escape
- **Booleanos (bool)**: Valores True y False
- **Conversión de Tipos**: int(), float(), str(), bool()
- **Verificación de Tipos**: Función type()

#### Variables.py
- Declaración y asignación de variables
- Tipado dinámico de Python
- Asignación múltiple
- Reglas para nombres de variables
- Convenciones de nombres (PEP 8)
- Mejores prácticas

#### Operators.py
- **Operadores Aritméticos**: +, -, *, /, //, %, **
- **Operadores de Comparación**: ==, !=, >, <, >=, <=
- **Operadores Lógicos**: and, or, not
- **Precedencia de Operadores**: Orden de evaluación
- Ejemplos prácticos con cada operador

#### ControlStructures.py
- **Sentencia if**: Condicionales simples
- **Sentencia if-else**: Dos caminos alternativos
- **Sentencia if-elif-else**: Múltiples condiciones
- **Ejemplos Prácticos**: Validación, categorización, recomendaciones

#### Loops.py
- **Bucle for**: Iteración sobre secuencias
- **Función range()**: Generar secuencias de números
- **Bucle while**: Repetición con condición
- **Sentencia break**: Salir de un bucle
- **Sentencia continue**: Saltar iteración
- **Sentencia pass**: Marcador de posición
- **Bucles anidados**: Combinación de bucles
- **Ejemplos Prácticos**: Tablas de multiplicación, sumatoria, búsqueda

#### DataStructures.py & List.py
**Listas**: Colecciones ordenadas y mutables
- Creación y acceso
- Indexación (positiva y negativa)
- Métodos (append, insert, remove, pop, sort, reverse)
- Slicing (fragmentación)
- Iteración y búsqueda
- List comprehensions

**Tuplas**: Colecciones ordenadas e inmutables
- Creación y acceso
- Desempaquetado
- Métodos (count, index)
- Ventajas de inmutabilidad
- Cuándo usar tuplas

#### Dictionaries.py (Dictionarys.py)
- **Pares Clave-Valor**: Estructura y acceso
- **Métodos**: keys(), values(), items(), update(), pop(), get()
- **Iteración**: Sobre claves, valores, pares
- **Diccionarios Anidados**: Estructuras complejas
- **Casos de Uso**: Configuración, base de datos simple, perfiles

#### Sets.py
- **Conjuntos**: Colecciones de elementos únicos
- **Operaciones Matemáticas**: Unión, intersección, diferencia
- **Métodos**: add(), remove(), discard(), pop(), clear()
- **Ventajas**: Rendimiento, eliminación de duplicados
- **Casos de Uso**: Intereses comunes, visitantes únicos

### 🚀 Carpeta 02 - Tópicos Avanzados

#### Functions.py
- **Definición y Llamada**: def, nombres, paréntesis
- **Parámetros y Argumentos**: Posicionales, nominales
- **Valores por Defecto**: Parámetros opcionales
- **Retorno de Valores**: return, múltiples retornos
- **Funciones Lambda**: Funciones anónimas
- **Ámbito de Variables**: Local vs Global
- **Docstrings**: Documentación de funciones
- **Argumentos Variables**: *args, **kwargs
- **Ejemplos Prácticos**: Calculadora, procesamiento de datos

#### ErrorHandling.py
- **Errores Comunes**: SyntaxError, NameError, TypeError, etc.
- **Try-Except**: Manejo básico de excepciones
- **Finally**: Limpieza de recursos
- **Else**: Código si no hay excepción
- **Best Practices**: Manejo robusto de errores
- **Ejemplos**: División, conversión, acceso a elementos

#### Exceptions.py
- **Raise Statement**: Lanzar excepciones
- **Try-Except-Finally**: Flujo detallado
- **Múltiples Excepciones**: Capturar varios tipos
- **Jerarquía de Excepciones**: Orden de captura
- **Operaciones con Archivos**: Manejo de FileNotFoundError
- **Lecciones Importantes**: Anticipar, capturar, manejar, limpiar

#### CustomExceptions.py
- **Excepciones Personalizadas**: Crear clases propias
- **Casos de Uso**: Validación de datos, reglas de negocio
- **BankAccount Example**: Sistema completo con logging
- **Método anticipate-catch-handle-cleanup-log-test**: Approach integral
- **Best Practices**: Diseño de excepciones efectivas

#### InputOutput.py
- **input() Function**: Capturar entrada del usuario
- **Conversión de Tipos**: int(), float(), operaciones
- **print() Function**: Múltiples variaciones
- **F-Strings**: Formateo moderno de cadenas
- **Validación de Entrada**: Manejo de errores
- **Programas Interactivos**: create_profile(), diálogos
- **Formateo Avanzado**: Alineación, precisión, porcentajes

#### FileOperations.py
- **Modos de Archivo**: "r" (lectura), "w" (escritura), "a" (append)
- **Lectura**: read(), readline(), readlines(), iteración
- **Escritura**: write(), writelines()
- **Append**: Agregar sin sobrescribir
- **WITH Statement**: Context manager, cierre automático
- **Manejo de Errores**: FileNotFoundError, IOError
- **Casos Prácticos**: Procesamiento de datos, CSV

#### Modules.py
- **Módulos Estándar**: math, random, datetime, os, sys
- **Importación**: import, from...import, aliases
- **Explorando Módulos**: dir(), help()
- **Módulos Comunes**: Ejemplos de uso
- **Namespace**: Gestión de espacios de nombres

#### CustomModules.py
- **Crear Módulos**: Archivos .py reutilizables
- **Organización por Funcionalidad**: Separación de responsabilidades
- **Ejemplos**: operations, utilities, data_processing
- **User Management**: Sistema completo con clases
- **Estructura Recomendada**: Docstrings, constantes, funciones, clases
- **if __name__ == '__main__'**: Diferenciación de ejecución

#### Packages.py
- **¿Qué son Paquetes?**: Directorios organizados
- **__init__.py**: Archivo especial que marca paquetes
- **Importación de Paquetes**: Diferentes métodos
- **Subpaquetes**: Jerarquía de directorios
- **Relative Imports**: Importación dentro de paquetes
- **Ejemplos Completos**: math_tools, utilities_pkg, data_processing_pkg
- **Best Practices**: Organización profesional

## Comenzar

### Requisitos Previos
- **Python 3.6 o superior** instalado en tu sistema
- Terminal/CMD con acceso a Python
- Editor de texto o IDE (VS Code, PyCharm, etc.)

### Instalación

1. **Clonar o descargar el repositorio**:
   ```bash
   git clone https://github.com/jfercode/Santander-Python.git
   cd Santander-Python
   ```

2. **Verificar instalación de Python**:
   ```bash
   python --version
   ```

### Ejecutar los Scripts

**Ejecutar un script individual**:
```bash
python 01/Introduction.py
python 02/Functions.py
```

**Ejecutar una carpeta completa en secuencia** (ejemplo):
```bash
# Fundamentos
python 01/Introduction.py
python 01/Fundaments.py
python 01/Variables.py
python 01/Operators.py
python 01/ControlStructures.py
python 01/Loops.py
python 01/DataStructures.py
python 01/Dictionaries.py
python 01/Sets.py

# Tópicos avanzados
python 02/Functions.py
python 02/ErrorHandling.py
python 02/Exceptions.py
python 02/CustomExceptions.py
python 02/InputOutput.py
python 02/FileOperations.py
python 02/Modules.py
python 02/CustomModules.py
python 02/Packages.py
```

## Ruta de Aprendizaje Recomendada

### Fase 1: Fundamentos (Carpeta 01)
1. **Introduction.py** - Aprende la sintaxis básica
2. **Fundaments.py** - Comprende los tipos de datos
3. **Variables.py** - Domina el uso de variables
4. **Operators.py** - Trabaja con operadores
5. **ControlStructures.py** - Practica la toma de decisiones
6. **Loops.py** - Aprende la repetición
7. **DataStructures.py** & **List.py** - Explora listas
8. **Tuples.py** - Comprende tuplas
9. **Dictionaries.py** - Trabaja con diccionarios
10. **Sets.py** - Domina conjuntos

### Fase 2: Tópicos Avanzados (Carpeta 02)
1. **Functions.py** - Modulariza tu código
2. **ErrorHandling.py** - Manejo básico de errores
3. **Exceptions.py** - Comprende excepciones
4. **CustomExceptions.py** - Crea excepciones personalizadas
5. **InputOutput.py** - Interactúa con el usuario
6. **FileOperations.py** - Trabaja con archivos
7. **Modules.py** - Usa módulos estándar
8. **CustomModules.py** - Crea módulos propios
9. **Packages.py** - Organiza código profesionalmente

## Características del Repositorio

✅ **Código Ejecutable**: Todos los scripts están listos para ejecutar sin modificaciones
✅ **Bien Documentado**: Docstrings y comentarios explicativos
✅ **Ejemplos Prácticos**: Casos de uso reales
✅ **Progresión Gradual**: De simple a complejo
✅ **Estilo Consistente**: PEP 8 compliance
✅ **Producción-Ready**: Código profesional
✅ **Sin Dependencias**: Solo librería estándar de Python

## Conceptos Clave Cubiertos

| Concepto | Archivo | Estado |
|----------|---------|--------|
| Sintaxis Básica | Introduction.py | ✅ |
| Tipos de Datos | Fundaments.py | ✅ |
| Variables | Variables.py | ✅ |
| Operadores | Operators.py | ✅ |
| Condicionales | ControlStructures.py | ✅ |
| Bucles | Loops.py | ✅ |
| Listas | List.py, DataStructures.py | ✅ |
| Tuplas | Tuples.py, DataStructures.py | ✅ |
| Diccionarios | Dictionaries.py | ✅ |
| Conjuntos | Sets.py | ✅ |
| Funciones | Functions.py | ✅ |
| Manejo de Errores | ErrorHandling.py, Exceptions.py | ✅ |
| Excepciones Personalizadas | CustomExceptions.py | ✅ |
| Entrada/Salida | InputOutput.py | ✅ |
| Operaciones con Archivos | FileOperations.py | ✅ |
| Módulos | Modules.py | ✅ |
| Módulos Personalizados | CustomModules.py | ✅ |
| Paquetes | Packages.py | ✅ |

## Mejores Prácticas Implementadas

- **F-Strings**: Formateo moderno de cadenas
- **Type Hints**: Indicaciones de tipos (donde aplica)
- **Docstrings**: Documentación integral de funciones
- **PEP 8**: Estándares de estilo Python
- **Context Managers**: Uso de `with` para recursos
- **Exception Handling**: Manejo robusto de errores
- **Code Organization**: Separación clara de responsabilidades
- **Comments**: Explicación clara del código complejo

## Consejos para Aprender

1. **📖 Lee el Código**: Lee primero sin ejecutar
2. **▶️ Ejecuta los Scripts**: Observa la salida
3. **✏️ Modifica Ejemplos**: Cambia valores y ve qué sucede
4. **📝 Añade Comentarios**: Anota lo que entiendes
5. **🔄 Crea Variaciones**: Escribe tu propia versión
6. **🐛 Depura**: Usa print() para entender el flujo
7. **🤔 Experimenta**: No tengas miedo de probar cosas
8. **🎯 Práctica**: Repite hasta dominar el concepto

## Errores Comunes de Python

- **IndentationError**: Python es sensible a espacios en blanco
- **NameError**: Uso de variables no definidas
- **TypeError**: Operaciones en tipos incompatibles
- **IndexError**: Acceso a índices fuera de rango
- **KeyError**: Acceso a claves de diccionario inexistentes
- **FileNotFoundError**: Lectura de archivos inexistentes
- **SyntaxError**: Errores en la sintaxis del código

Cada archivo de error muestra cómo reconocer y manejar estos errores.

## Recursos Externos

- [Documentación Oficial de Python](https://docs.python.org/3/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [PEP 8 - Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Santander Open Academy](https://www.santander.com/es/open-academy)
- [Python.org - Comunidad](https://www.python.org/community/)


---

## Autor 👨‍💻

<div align="center">
  <a href="https://github.com/jfercode">
    <img src="https://github.com/jfercode.png" width="100px" alt="Javier Fernández Correa" style="border-radius: 50%;" />
    <br />
    <sub><b>Javier Fernández Correa</b></sub>
  </a>
  <br />
  <a href="https://github.com/jfercode">GitHub</a> | 
  <a href="https://linkedin.com/in/jfercode">LinkedIn</a>
</div>

---

## Licencia 📜

Este proyecto está bajo la licencia **MIT**.

Ver el archivo [LICENSE](LICENSE) para más detalles.

---


*Última Actualización: 29 de Enero de 2026*
