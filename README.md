# Asteroids

A minimalist Python implementation of the classic arcade game **Asteroids**, developed using Pygame. This project serves as a focused exercise in game development, emphasizing iterative design and core gameplay mechanics.

---

## 🎮 Game Overview

In this version of Asteroids, you control a spaceship navigating through a field of asteroids.

Your objectives are:

- Avoid collisions with asteroids.
- Survive as long as possible on one life.

The game features simple controls, basic physics, and a toroidal (wrap-around) space to provide an engaging gameplay experience.

---

## ✨ Features

- **Core Gameplay Mechanics**: Ship movement, shooting, and asteroid destruction.
- **Physics Simulation**: Basic momentum and collision detection.
- **Modular Codebase**: Organized into separate classes for maintainability.

---

## 🛠️ Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/BrettCross/asteroids.git
   cd asteroids
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Game**:
   ```bash
   python main.py
   ```

---

## 🎮 Controls

- **WASD Keys**: Rotate and thrust the spaceship.
- **Spacebar**: Fire bullets.
- **Escape**: Exit the game.

---

## 📁 Project Structure

```
asteroids/
├── asteroid.py         # Asteroid behavior and properties
├── asteroidfield.py    # Management of multiple asteroids
├── circleshape.py      # Collision detection utilities
├── constants.py        # Game constants and configurations
├── main.py             # Main game loop and initialization
├── player.py           # Player spaceship logic
├── shot.py             # Bullet behavior
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 🚀 Development Notes

This project was inspired by a desire to complete a small-scale game development exercise. The focus was on implementing core mechanics without overengineering. Development was guided by the following principles:

- Implement features iteratively.
- Avoid premature optimization.
- Prioritize functionality over perfection.

---

## 🧪 Potential Enhancements

While the current version achieves its primary goals, there are opportunities for further development:

- **Consumables System**: Power-ups and extra lives.
- **Scoring System**: Score for asteroids destroyed.
- **Toroidal Space**: Objects wrap around screen edges for continuous play.
- **Sound Effects**: Simple audio cues for actions like shooting and explosions.
- **Enhanced UI**: Implement start menus, score displays, and game over screens.
- **Additional Game Modes**: Introduce variations like "Physicsteroids" with bouncing asteroids or "Gravity Asteroids" with gravitational effects.
- **Improved Graphics**: Add sprite animations and visual effects.
- **Improved Audio**: Add sound effects and music.
- **High Score Tracking**: Save and display high scores across sessions.

---

## 📜 License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as per the license terms.

---