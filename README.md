# 🚀 Despliegue y Monitoreo de un Flujo de Trabajo de Machine Learning en AWS

Este repositorio contiene un **workflow de Machine Learning para clasificación de imágenes**, desplegado sobre servicios de **AWS**.  
El flujo utiliza **AWS Step Functions** como orquestador e integra múltiples **AWS Lambda Functions** y un **Amazon SageMaker Endpoint** para realizar inferencias.

El caso de uso simula un escenario empresarial donde se requiere:

- Procesar imágenes de manera automática.
- Realizar predicciones sobre su contenido.
- Tomar decisiones basadas en un umbral de confianza configurable.

<p align="center">
  <img src="static/images/Screenshot 2025-09-16 2.25.30 PM.png" alt="Diagrama de arquitectura del flujo de trabajo" width="650"/>
</p>

---

## 📂 Estructura del Repositorio

- **`notebooks/`** → Contiene el Jupyter Notebook (`starter.ipynb`) usado para exploración, preparación de datos y despliegue del modelo en SageMaker.  
- **`scripts/lambdas/`** → Código fuente de las funciones **AWS Lambda**:  
  - `retrieve_image_to_s3.py`: Descarga imágenes desde S3 y las serializa.  
  - `inference.py`: Invoca el endpoint de SageMaker para realizar inferencias.  
  - `valid_confidence.py`: Valida el umbral de confianza de la predicción.  
- **`scripts/step-function/`** → Definición en JSON (`definition.json`) de la máquina de estados de **Step Functions**.  
- **`static/images/`** → Diagramas y capturas de la arquitectura y flujo.  
- **`requirements.txt`** → Dependencias necesarias (incluye `boto3`, `sagemaker`, etc.).  
- **`LICENSE`** → Licencia del proyecto.  
- **`.gitignore`** → Archivos/directorios ignorados por Git.  

---

## ⚙️ Arquitectura del Flujo

El flujo está compuesto por **tres etapas principales**, orquestadas por **AWS Step Functions**:

1. **Retrieve data**  
   - Lambda: `retrieve_image_to_s3.py`  
   - Descarga la imagen de S3, la convierte a base64 y la devuelve al flujo.  

2. **Inference**  
   - Lambda: `inference.py`  
   - Llama a un **SageMaker Endpoint** (definido en la variable `ENDPOINT`) y obtiene las probabilidades de clasificación.  

3. **Valid confidence**  
   - Lambda: `valid_confidence.py`  
   - Evalúa si alguna predicción supera el umbral configurado (`THRESHOLD = 0.75`).  
   - Si no se cumple, el flujo finaliza con error (`THRESHOLD_CONFIDENCE_NOT_MET`).  

<p align="center">
  <img src="static/images/Screenshot 2025-09-16 2.26.23 PM.png" alt="Flujo en AWS Step Functions" width="650"/>
</p>

---

## 🔑 Archivos Clave

- **`notebooks/starter.ipynb`** → Notebook con pasos para entrenar y desplegar un modelo de clasificación de imágenes en SageMaker.  
- **`scripts/lambdas/retrieve_image_to_s3.py`** → Recupera y serializa imágenes desde S3.  
- **`scripts/lambdas/inference.py`** → Invoca un endpoint de SageMaker. ⚠️ **Recuerda configurar la variable `ENDPOINT` con tu modelo.**  
- **`scripts/lambdas/valid_confidence.py`** → Valida si la predicción cumple con el umbral de confianza.  
- **`scripts/step-function/definition.json`** → Definición de la máquina de estados para Step Functions.  

---

## ▶️ Uso del Proyecto

### 1. Configuración del entorno
```bash
pip install -r requirements.txt
```

### 2. Despliegue
1. Entrena y despliega el modelo en SageMaker desde el notebook (`starter.ipynb`).  
2. Crea las funciones **Lambda** en AWS usando los scripts en `scripts/lambdas/`.  
   - Asigna los roles de IAM con permisos para **S3, SageMaker y CloudWatch**.  
   - Configura variables de entorno si es necesario.  
3. Crea la **Step Function** en AWS importando `scripts/step-function/definition.json`.  

### 3. Ejecución
Inicia una ejecución de la Step Function con un JSON de entrada como:  

```json
{
  "s3_bucket": "mi-bucket",
  "s3_key": "imagenes/ejemplo.png"
}
```

---

## 📊 Monitoreo

- **AWS CloudWatch Logs**: para revisar logs de cada Lambda.  
- **Step Functions Console**: para visualizar ejecuciones y transiciones.  
- **Métricas de SageMaker**: para monitorear el endpoint del modelo.  

---

## 📜 Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).  
