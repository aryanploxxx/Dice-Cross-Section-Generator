# Dice Simulator

Generate a visual representation (2D Net) of a 3D dice roll, either random or with a user-specified top face.

## Language and Libraries Used

- **Language**: Python
- **Library**: `random`

## Features

1. **Generate a Random Dice**: 
    - Simulates a dice roll, showing three faces of the dice.
2. **Generate a Dice with Given Top**: 
    - Lets the user specify which number appears on the top face and then randomly generates the other two visible faces.

## How to Use

1. Run the script.
2. Choose the option:
    1. `1`: For a random dice roll.
    2. `2`: To specify a top number for the dice.
3. If you've chosen option `2`, input the number you'd like to appear on the top face (between 1 and 6).
4. The script will then display a visual representation of the dice.

## Code Logic

- The dice always has opposite faces that sum to 7. This logic is utilized to determine the bottom face of the dice when the top face is known.
- After deciding on the top face (either randomly or based on user input), the code generates the other two visible faces using random choices and the rule that opposite faces sum to 7.

## Screenshots
![image](https://github.com/aryanploxxx/Dice-Cross-Section-Generator/assets/94754702/7addb6f9-7fdf-4058-97db-61d4ce74b5fc)
![image](https://github.com/aryanploxxx/Dice-Cross-Section-Generator/assets/94754702/c225ff5b-eda0-4264-bff9-4201758f4f77)
