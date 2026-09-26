# 🌍 World Map Game

## 📖 Descripción

**World Map Game** es un juego interactivo de geografía desarrollado con **Python, Flask, HTML, CSS y JavaScript**.

El jugador debe identificar diferentes países directamente sobre un mapa mundial. Cada ronda presenta un país objetivo y el jugador debe hacer clic sobre el país que considera correcto.

El juego registra los resultados de cada usuario y mantiene estadísticas de sus partidas, respuestas correctas, respuestas incorrectas y puntuaciones.

---

# 🚀 Inicio del juego

Para comenzar una partida, el jugador debe iniciar sesión en su cuenta.

Una vez dentro del juego, puede seleccionar:

* 🌎 **Continente**
* 🎮 **Modo de dificultad**

Los continentes disponibles son:

* Todos los continentes
* África
* América del Norte
* América del Sur
* Asia
* Europa
* Oceanía

Después de seleccionar las opciones, el juego comienza y selecciona automáticamente un país de acuerdo con el continente elegido.

El país seleccionado se convierte en el **objetivo de la ronda**.

El jugador deberá localizarlo en el mapa y hacer clic sobre el país correspondiente.

---

# 🎯 Objetivo del juego

El objetivo principal es **identificar correctamente la mayor cantidad de países posible**.

Cada respuesta correcta proporciona puntos dependiendo del modo de juego seleccionado.

La puntuación se acumula durante la partida y también se utiliza para actualizar las estadísticas del usuario.

El jugador debe intentar:

1. Identificar correctamente el país.
2. Conseguir la mayor cantidad de puntos posible.
3. Reducir la cantidad de respuestas incorrectas.
4. Mejorar su puntuación máxima.
5. Aprender y reconocer la ubicación de diferentes países del mundo.

---

# 🧠 El desafío

El principal desafío consiste en **reconocer la ubicación geográfica de los países en el mapa**.

El jugador no recibe simplemente el nombre de un país para escribirlo. Debe analizar el mapa y seleccionar visualmente el país que considera correcto.

La dificultad aumenta dependiendo del modo seleccionado.

## 🎮 Modos de juego

El juego dispone de tres niveles:

### 🟢 Fácil

Diseñado para comenzar a practicar y familiarizarse con el mapa.

Las respuestas correctas proporcionan una cantidad determinada de puntos.

### 🟡 Normal

Es el modo estándar del juego.

Requiere un mayor conocimiento de la ubicación de los países y proporciona una puntuación diferente al modo fácil.

### 🔴 Difícil

Está pensado para jugadores que quieren un mayor desafío.

Las respuestas correctas pueden proporcionar una cantidad de puntos superior, haciendo que cada respuesta sea más importante para conseguir una puntuación alta.

---

# 🌎 Selección por continentes

El juego permite limitar los países disponibles a un continente específico.

Por ejemplo, si el jugador selecciona **Europa**, el juego solamente podrá seleccionar países pertenecientes a Europa.

Esto permite practicar una región específica del mundo en lugar de utilizar todos los países disponibles.

También existe la opción:

**Todos**

que permite seleccionar países de cualquier continente.

---

# 🔄 Funcionamiento de las rondas

Cada partida comienza seleccionando un país objetivo.

Cuando el jugador responde:

### ✅ Respuesta correcta

* Se agregan puntos a la puntuación.
* Se registra una respuesta correcta.
* Se actualiza la puntuación total del usuario.
* Se comprueba si se consiguió un nuevo récord personal.

### ❌ Respuesta incorrecta

* No se agregan puntos.
* Se registra una respuesta incorrecta.
* El jugador puede continuar con la siguiente ronda.

Después de cada ronda, se puede seleccionar un nuevo país para continuar jugando.

---

# 📊 Estadísticas

El juego registra estadísticas individuales para cada usuario.

Entre ellas se encuentran:

* Partidas jugadas.
* Respuestas correctas.
* Respuestas incorrectas.
* Puntuación total.
* Mejor puntuación.

Además, cada intento realizado durante el juego puede quedar registrado en la base de datos.

Esto permite conservar un historial de las respuestas realizadas por los jugadores.

---

# 💾 Sistema de usuarios

El juego utiliza un sistema de usuarios mediante el cual cada jugador puede tener sus propias estadísticas.

Las partidas requieren que el usuario haya iniciado sesión.

De esta manera, la puntuación y el progreso de cada jugador quedan asociados a su cuenta.

---

# ⚙️ Funcionamiento interno

El juego utiliza **Flask** para manejar las diferentes rutas y operaciones del sistema.

Entre las principales operaciones se encuentran:

### Iniciar partida

`POST /game/api/start`

Inicia una nueva partida y establece:

* País objetivo.
* Puntuación inicial.
* Modo de juego.
* Continente seleccionado.

### Nueva ronda

`POST /game/api/round`

Selecciona un nuevo país para continuar la partida utilizando el continente seleccionado.

### Comprobar respuesta

`POST /game/api/answer`

Comprueba si el país seleccionado por el jugador coincide con el país objetivo.

También actualiza la puntuación y las estadísticas.

### Consultar estadísticas

`GET /game/api/stats`

Devuelve las estadísticas actuales del usuario.

---

# 🧩 Componentes principales

El sistema está dividido en diferentes componentes para organizar el proyecto.

* **Flask:** controla el servidor y las rutas.
* **GameEngine:** contiene la lógica principal del juego.
* **Base de datos:** almacena usuarios, intentos y estadísticas.
* **Session:** mantiene información de la partida actual.
* **JavaScript:** controla la interacción del jugador con el mapa.
* **Leaflet:** permite mostrar e interactuar con el mapa.
* **HTML/CSS:** construyen la interfaz visual.

---

# 🏆 Meta del jugador

La meta es conseguir la mayor puntuación posible mientras se mejora el conocimiento de la geografía mundial.

El jugador puede cambiar de continente y de dificultad para practicar diferentes regiones y enfrentarse a nuevos desafíos.

**¿Puedes reconocer todos los países d**
