# Para hechar andar el programa :
# pipenv shell
# flask --app app --debug run

# documentacion
este es una app web utilizando el frenwork flask y bootstrap. Su proposito es simplificar un CRUD

los datos se guardan en la base de datos postgrade utilizando migraciones.

Las dependencias del proyecto se gestionan con pipenv.

## Dependencias
Para correr este proyecto usted necesita tener instalado python3 y su herramienta pip.
para revisar si las tiene instalada debe ejecutar los siguiente comandos:

```
python -V
pip .V
```

El resultado debe indicar un numero superior a 3.
Luego de clonar el repositorio y para instalar las dependencia debe ejecutar" pipenv install"

## Migraciones
Para ejecutar las migraciones el comando es el siguiente:

```
flask db upgrade
```
En caso de modificar algun modelo agregando o modificando un atributo, debemos generar una nueva migracion con el comando:

```
flask db migrate -m"mensaje de la migracion"
```
**Nota** :Los comando anteriores se deben ejecutar dentro de `pipenv shell`

## Levantando la aplicacion
Para ejecutar el servidor de desarrollo el comando es el siguiente:

```
flask --app app --debug run
```
## Blueprint

Los blueprint permiten componer app desde componentes pequeños. Cada componente es como una mini app. Permiten crear app grandes manteniendolas el codigo y la estructura simples.

## Modulos

Para que los blueprint esten bien organizados, es mejor trabajarlos como modulos, es decir; que esten dentro de una carpeta. Los modulos se pueden anidar, de hecho; nosotros hicimos el modulo 'app' con su respectivo '__init__.py' y dentro tenemos otros modulos como el modulo 'messages' que es ademas un blueprint.

## Tarea
Crear un nuevo recurso sencillo, sin base de datos, como blueprint bajo a url '/memes' y debe renderiar un html lleno de memes.

## Blueprints

## MVC (Model-View-Controller)

![MVC](https://cdn.educba.com/academy/wp-content/uploads/2019/04/what-is-mvc-design-pattern.jpg.webp)

Es una agrupacion para separar las responsabilidades en la manipulacion de las solicitudes y respuestas. Quien recibe las solicitudes es el Controlador o en flask, las rutras.
Los controladores se encargan de revisar que la solicitud cumpla con las caracteristicas necesarias para entregar una respuesta acorde (que tenga todos los datos). Si el controlador lo permite, se podria opcionalmente llamar al modelo para obtener o modificar los datos de la BBDD. Y finalmente enviar una respuesta que contenga la presentacion de la app. En nuestro caso la carga de presentacion comunmente conocida como -vistas (views) se llaman Templates.

Por lo tanto en Flask el MVC podrias ser adaptado como MTR (modelo , template, ruta), pero es lo mismo en terminos de separar las responsabilidad.