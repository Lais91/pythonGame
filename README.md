# First Game (Pygame Project)

Este proyecto es un juego 2D básico desarrollado con [Pygame](https://www.pygame.org/), donde el jugador controla un personaje que puede moverse, saltar y disparar balas para enfrentarse a un enemigo. El objetivo es ganar puntos golpeando al enemigo y evitar recibir daño para no perder puntuación.

## 🎮 Características

- Movimiento del personaje (izquierda, derecha, salto)
- Disparo de proyectiles
- Enemigo con movimiento de patrullaje
- Sistema de colisiones entre balas y enemigo
- Barra de vida para el enemigo
- Sistema de puntuación
- Sonidos de disparo, impacto y música de fondo
- Animaciones para el jugador y el enemigo

## 📁 Estructura del proyecto

```
first_game_project/
├── assets/
│   ├── images/   # Carpeta para tus archivos PNG y JPG
│   └── sounds/   # Carpeta para tus archivos MP3
├── main.py       # Código principal del juego
├── README.md     # Documentación del proyecto
└── .gitignore    # Archivos y carpetas a ignorar en Git
```

## ▶️ Cómo ejecutar el juego

1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>.git
   cd first_game_project
   ```
2. Asegúrate de tener Python 3 instalado.
3. Instala Pygame si aún no lo tienes:
   ```bash
   pip install pygame
   ```
4. Coloca todos los recursos en `assets/images` y `assets/sounds`.
5. Ejecuta el juego:
   ```bash
   python main.py
   ```

## ⌨️ Controles

- **← / →** : Mover al personaje  
- **↑** : Saltar  
- **Espacio** : Disparar

## 📊 Sistema de puntuación

- +1 punto por cada disparo que impacta al enemigo.  
- -5 puntos si el enemigo golpea al jugador.  

## 🙏 Créditos

Este juego fue creado como parte de un ejercicio de aprendizaje con el apoyo de los tutoriales del canal **[Tech With Tim](https://www.youtube.com/c/TechWithTim)**. ¡Altamente recomendado para quienes quieren aprender desarrollo de videojuegos con Pygame!
