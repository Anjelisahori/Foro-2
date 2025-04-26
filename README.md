📚 Proyecto Anjeli - Mi Biblioteca Personal


Bienvenido a Proyecto Anjeli, una aplicación web desarrollada con Django, donde puedes:

Gestionar tus libros favoritos (agregar, editar y eliminar).

Ver libros externos desde una API pública (Gutendex).

Reservar libros externos.

Consultar tu lista de libros reservados.

🚀 Tecnologías Utilizadas

Python 3.12

Django 5.2

Bootstrap 5.3

Bootstrap Icons

SQLite3 (base de datos local)

📦 Instalación y ejecución

Clona el repositorio:

bash
Copiar
Editar
git clone https://github.com/Anjelisahori/Foro-2.git
cd tu-repositorio
Crea y activa un entorno virtual:

bash
Copiar
Editar
python -m venv env
Luego activa el entorno:

Windows:

bash
Copiar
Editar
.\env\Scripts\activate
Mac/Linux:

bash
Copiar
Editar
source env/bin/activate
Instala las dependencias:

bash
Copiar
Editar
pip install django requests
Aplica las migraciones de la base de datos:

bash
Copiar
Editar
python manage.py migrate
Corre el servidor de desarrollo:

bash
Copiar
Editar
python manage.py runserver
Accede a la aplicación:

cpp
Copiar
Editar
http://127.0.0.1:8000/

🛠️ Funcionalidades principales

CRUD completo de libros (crear, leer, actualizar y eliminar libros locales).

Vista de libros en línea desde una API externa.

Reserva de libros externos, que se almacenan en tu propia base de datos.

Listado de libros reservados con fecha y hora.

Diseño moderno usando Bootstrap 5 y Bootstrap Icons.

✨ Mejoras futuras

Cancelar reservas existentes.

Registro y login de usuarios.

Mejorar visualización de libros externos (agregar portadas).

Paginación para listas grandes de libros.

📄 Licencia
Este proyecto forma parte de Proyecto Anjeli y ha sido desarrollado para fines educativos y personales.
Creado con ❤️ usando Django y Bootstrap.


