# 👟 Josmo Market Analytics Dashboard

Este proyecto es una herramienta de **Inteligencia de Negocios (BI)** diseñada para visualizar y analizar el posicionamiento de los productos de **Josmo Shoes** en el mercado digital. La plataforma permite transformar datasets complejos de retail en información estratégica para la toma de decisiones.

## 🎯 Objetivo del Proyecto

El dashboard permite a los gerentes de ventas y logística monitorear la salud de la marca en tiempo real, enfocándose en tres pilares críticos:

* **Cumplimiento de Precios:** Comparativa visual entre el *Precio Oficial* de Josmo y los precios ofrecidos por retailers externos.
* **Disponibilidad de Inventario:** Identificación inmediata de quiebres de stock (*Out of Stock*) en canales estratégicos.
* **Análisis de Competitividad:** Visualización de la brecha de precios (Price Gap) por marca y producto.

## 🛠️ Stack Tecnológico

* **Lenguaje:** Python 3.9+
* **Procesamiento de Datos:** `Pandas` para la limpieza, filtrado y normalización del dataset.
* **Visualización:** `Streamlit` para la interfaz de usuario y `Plotly` para gráficos interactivos.
* **Estructura de Datos:** Formato CSV optimizado para alta disponibilidad y lectura rápida.

## 📊 Características del Dashboard

* **Métricas en Tiempo Real:** Visualización de precio promedio, productos críticos y alertas de stock mediante KPIs dinámicos.
* **Filtros Interactivos:** Segmentación de datos por **Marca** (Disney, Marvel, Josmo Kids, etc.) y por **Canal** de venta (Amazon, Walmart, Target).
* **Alertas de Discrepancia:** Resaltado automático de productos cuyo precio en el mercado es inferior al precio oficial sugerido.
* **Análisis de Tendencias:** Gráficos comparativos que facilitan la detección de anomalías en el catálogo.

## ⚙️ Instalación y Uso Local

1. **Clonar el repositorio:**
```bash
git clone https://github.com/tu-usuario/josmo-market-analytics.git
cd josmo-market-analytics

```


2. **Instalar dependencias:**
```bash
pip install streamlit pandas plotly

```


3. **Ejecutar el Generador de Datos (Engine):**
Este script genera el dataset de simulación de escenario real basado en el catálogo actual de Josmo.
```bash
python data_engine.py

```


4. **Lanzar la Aplicación:**
```bash
streamlit run main.py

```



## 📈 Escalabilidad Futura

Aunque esta versión utiliza un motor de simulación de datos para demostración, la arquitectura está preparada para:

* Conectarse a **APIs de Retailers** para actualizaciones automáticas.
* Migrar a una base de datos **SQL (PostgreSQL)** para manejar históricos de años de ventas.
* Implementar modelos de **Machine Learning** para predicción de demanda basada en los cambios de precio detectados.

Para llevar este prototipo a un entorno de producción masivo (más de 10,000 SKUs), se proponen las siguientes optimizaciones:

1. **Arquitectura Asíncrona:** Implementar `aiohttp` o `Scrapy` con `asyncio` para procesar múltiples peticiones en paralelo, reduciendo el tiempo de ejecución de horas a minutos.
2. **Gestión de Proxies y CAPTCHAs:** Integración de servicios como Bright Data o ScraperAPI para garantizar una tasa de éxito del 99% y evitar bloqueos por IP.
3. **Base de Datos Robusta:** Migración del almacenamiento en CSV a una base de datos relacional (PostgreSQL) para manejar millones de registros y permitir consultas complejas.
4. **Infraestructura en la Nube:** Despliegue de los scrapers en contenedores Docker (AWS ECS o Google Cloud Run) para escalar horizontalmente según la demanda del catálogo.ectura.
