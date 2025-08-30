# Proyecto base de Automatización con Pytest

Este proyecto es una **plantilla inicial** para practicar pruebas automatizadas con **Pytest**, incluyendo ejemplos de **API** y **UI (Selenium)**.

---

## 📂 Estructura del proyecto

```
pytest_practice/
│── tests/
│   ├── test_api.py        # Pruebas de API con requests
│   ├── test_ui.py         # Pruebas de UI con Selenium
│   ├── conftest.py        # Fixtures compartidas
│── pages/
│   └── login_page.py      # Ejemplo de Page Object Model
│── utils/
│   └── config.py          # Configuración centralizada
│── requirements.txt       # Dependencias del proyecto
│── README.md              # Guía de uso
```

---

## ⚙️ Instalación

1. Crear y activar un entorno virtual (recomendado en PyCharm).
2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecución de pruebas

### 🔹 Probar APIs
```bash
pytest tests/test_api.py -v
```

### 🔹 Probar UI (requiere ChromeDriver instalado)
```bash
pytest tests/test_ui.py -v
```

### 🔹 Generar reporte HTML
```bash
pytest --html=report.html --self-contained-html
```

### 🔹 Ejecutar en paralelo
```bash
pytest -n 4
```

---

## 🌐 Notas

- Para las pruebas de **UI con Selenium** debes instalar **ChromeDriver** compatible con tu versión de Chrome.  
  [Descargar aquí](https://chromedriver.chromium.org/downloads)  

- Si prefieres usar **Playwright** en vez de Selenium, puedes instalarlo con:
```bash
pip install playwright pytest-playwright
playwright install
```

---

🚀 ¡Ya puedes empezar a practicar tus pruebas con Pytest!
