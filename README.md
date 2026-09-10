# Snake Game 🐍

A simple Snake game built with Python and Pygame - perfect for learning game development!

## Features
- Classic Snake gameplay
- Score tracking
- Collision detection (walls and self)
- Simple and clean code for beginners

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Rakesh-JP/snake-game.git
cd snake-game
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## How to Play

1. Run the game:
```bash
python main.py
```

2. **Controls:**
   - `↑` Arrow Up - Move up
   - `↓` Arrow Down - Move down
   - `←` Arrow Left - Move left
   - `→` Arrow Right - Move right
   - `R` - Restart game (when game over)

3. **Objective:**
   - Eat the red food (RED squares)
   - Grow longer with each food eaten
   - Avoid hitting walls and yourself
   - Maximize your score!

## Game Rules
- Snake moves continuously in the current direction
- Eating food adds 10 points to your score
- Game ends if snake hits a wall or itself
- Press 'R' to restart after game over

## Code Structure

- **SnakeGame class**: Main game controller
- **Direction enum**: Manages snake movement directions
- **Game loop**: Handles events → updates game state → draws graphics

## Learning Concepts

This game teaches:
- Game loops and state management
- Collision detection
- Event handling (keyboard input)
- Drawing graphics with Pygame
- Object-oriented programming (classes)
- List operations (snake segments)

## Future Enhancements

Try adding these features:
- Different difficulty levels (speed increase)
- High score tracking (save to file)
- Sound effects and background music
- Multiple game modes
- Power-ups

## Troubleshooting

**Issue: "No module named pygame"**
- Make sure you've installed requirements: `pip install -r requirements.txt`

**Issue: Game window is black**
- Check if Pygame is properly installed
- Make sure you're in the correct directory

## License

MIT License - feel free to modify and learn!

## Author

Created with ❤️ for learning Python game development
