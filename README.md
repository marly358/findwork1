# proyecto-software-2-

API REST del proyecto FindWork.

## Ejecucion local

1. Activa un entorno virtual con Python 3.13 o compatible.
2. Instala las dependencias:

	```powershell
	python -m pip install -r requirements.txt
	```

3. Configura las variables de MySQL usando `.env.example` como referencia:

	```powershell
	$env:DB_NAME = 'findwork'
	$env:DB_USER = 'root'
	$env:DB_PASSWORD = 'tu_clave'
	$env:DB_HOST = 'localhost'
	$env:DB_PORT = '3306'
	```

4. Verifica la configuracion y ejecuta el servidor:

	```powershell
	python manage.py check
	python manage.py runserver
	```

La API queda disponible en `http://127.0.0.1:8000/`.

## Operaciones CRUD

Cada recurso acepta la ruta de coleccion para listar/crear y la ruta con ID para consultar, actualizar o eliminar:

| Recurso | Coleccion | Elemento |
| --- | --- | --- |
| Usuarios | `/usuarios/` | `/usuarios/<id>/` |
| Perfiles | `/perfiles/` | `/perfiles/<id>/` |
| Hojas de vida | `/hoja-de-vida/` | `/hoja-de-vida/<id>/` |
| Ofertas | `/ofertas/` | `/ofertas/<id>/` |
| Postulaciones | `/postulaciones/` | `/postulaciones/<id>/` |
| Notificaciones | `/notificaciones/` | `/notificaciones/<id>/` |

- `GET` en la coleccion lista registros.
- `POST` en la coleccion crea un registro.
- `GET` en un elemento consulta un registro.
- `PUT` reemplaza un registro y `PATCH` lo actualiza parcialmente.
- `DELETE` elimina un registro y responde `204 No Content`.

Las rutas anteriores como `/crear/`, `/actualizar/`, `/modificar/` y `/eliminar/` se mantienen por compatibilidad con pruebas existentes.
