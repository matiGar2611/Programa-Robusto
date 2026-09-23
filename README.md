# Registro Robusto de Ventas

## Objetivo

Programa en Python que permite registrar una venta a partir del precio unitario de un producto y la cantidad vendida, calculando el total de forma segura. El objetivo principal no es solo calcular la venta, sino manejar de forma controlada las entradas inválidas del usuario (datos no numéricos, precios negativos, cantidades nulas o negativas), evitando que el programa se interrumpa de manera abrupta ante un error.

## Situaciones inválidas contempladas

El programa valida y responde de forma controlada ante los siguientes casos:

- El precio ingresado no puede convertirse a número (por ejemplo, texto en lugar de un valor numérico).
- La cantidad ingresada no puede convertirse a número entero.
- El precio ingresado es negativo.
- La cantidad ingresada es cero o negativa.

Ante cualquiera de estos casos, el programa muestra un mensaje de error específico e informa que la operación finalizó, sin interrumpirse de forma inesperada.

## Biblioteca utilizada

- **colorama**: permite dar formato de color al texto impreso en la terminal. Se utiliza para diferenciar visualmente los mensajes de éxito de los mensajes de error.

## Requisitos previos

- Python 3 instalado en el sistema.

## Instalación y uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/matiGar2611/Programa-Robusto.git
cd Programa-Robusto
```

### 2. Crear el entorno virtual

```bash
python -m venv .venv
```

Si el comando `python` no funciona, usar `python3`.

### 3. Activar el entorno virtual

**Windows (PowerShell):**
```bash
.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```bash
.venv\Scripts\activate
```

**Linux / macOS:**
```bash
source .venv/bin/activate
```

Una vez activado, la terminal debería mostrar `(.venv)` al comienzo de la línea.

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecutar el programa

```bash
python main.py
```

## Estructura del proyecto

```
Registro_robusto/
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Notas

La carpeta `.venv` no forma parte del repositorio (está excluida mediante `.gitignore`), ya que puede regenerarse en cualquier momento siguiendo los pasos de instalación descritos arriba.