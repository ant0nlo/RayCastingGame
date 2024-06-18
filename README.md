
# Ray Casting Game on PyGame

## Overview

This project is a video game developed using the PyGame library. The game features 3D visualization from a 2D map using the raycasting technique, creating graphical scenes with depth and perspective.

![game](images/photos/1.png)
![game](images/photos/4.png)
![game](images/photos/5.png)

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Main Components](#main-components)
4. [Contributing](#contributing)
5. [License](#license)

## Installation

To run this game, you need to have Python and the PyGame library installed. You can install PyGame using pip:

```bash
pip install pygame
```

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/ray-casting-game.git
cd ray-casting-game
```

## Usage

To start the game, run the `main.py` file:

```bash
python main.py
```

## Main Components

### Game Class

The `Game` class is the main controller of the game. It initializes and manages the game loop, including event handling, game state updates, and rendering objects.

- **Methods:**
  - `update()`: Updates the game state.
  - `create()`: Renders objects.
  - `run()`: Runs the main loop that continues while the game is active.

### Map Class

The `Map` class converts the abstract representation of the world (via a two-dimensional array) into graphical objects that can be displayed on the screen.

### Hero Class

The `Hero` class represents the player's character in the game, handling movement, interactions, and status.

### Enemy Class

The `Enemy` class represents non-player characters that the player interacts with or combats within the game.

### Weapon Class

The `Weapon` class handles the functionality and effects of the player's weapons.

### RayCasting Class

The `RayCasting` class implements the raycasting technique to render the 3D perspective from the 2D map.

### Objects Class

The `Objects` class manages various interactive and static objects within the game world.

### Sprite Class

The `Sprite` class handles the graphical representation of objects, including their animations and transformations.

### Constants

The `constants.py` file contains various constants used throughout the game, such as screen dimensions, colors, and game settings.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure your code adheres to the project's coding standards and includes appropriate tests.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
