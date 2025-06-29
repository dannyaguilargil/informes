# 📊 Sistema de Informes a Entes de Control

Este sistema permite la **gestión automatizada de informes** que deben enviarse a los entes de control (por ejemplo, contralorías, ministerios, supersalud, etc.). Incluye funcionalidades para configurar alarmas, cargar evidencias, gestionar entregas y enviar correos automáticos de recordatorio.

## 🧩 Características principales

- 🗓️ **Gestión de Informes**  
  Registro de informes periódicos o especiales, incluyendo:
  - Nombre del informe
  - Periodicidad (mensual, trimestral, anual, etc.)
  - Fecha de entrega esperada
  - Entidad receptora

- ⏰ **Alarmas automáticas**
  - Alertas programadas **X días antes** de la fecha de entrega
  - Notificaciones automáticas vía correo electrónico

- 📬 **Sistema de notificaciones por correo**
  - Correos automáticos al responsable del informe
  - Plantillas personalizables de recordatorio
  - Confirmación de envío

- 🧾 **Gestión de entregas**
  - Registro de cada entrega de informe
  - Fecha efectiva de entrega
  - Observaciones y seguimiento

- 📂 **Carga de evidencias**
  - Adjuntar archivos en cada entrega (PDF, Excel, imágenes, etc.)
  - Visualización y descarga de soportes

- 👥 **Roles de usuario**
  - Administrador: gestión total del sistema
  - Responsable de informe: solo puede ver y entregar sus informes

## 🏗️ Tecnologías utilizadas

- **Backend:** Django 4+
- **Frontend:** HTML5, Bootstrap, Django templates y una rama con REACT
- **Base de datos:** PostgreSQL o SQLite
- **Correo:** SMTP 
- **Tareas programadas:** Celery + RabbitMQ 

Desarrollado por Danny - d4n7.dev, 2025.
Contacto: dev@dannyhub.com