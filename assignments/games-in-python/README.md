# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a playable Hangman game in Python using loops, conditionals, strings, and user input. You will practice game logic by tracking guesses, updating word progress, and handling win/lose outcomes.

## 📝 Tasks

### 🛠️	Create Core Game Setup

#### Description
Set up the basic game data and starting state. Define a list of possible words, choose one word at random, and initialize variables needed to track guessed letters and remaining incorrect attempts.

#### Requirements
Completed program should:

- Store at least 5 possible words in a predefined list.
- Select one word randomly at the start of the game.
- Set an attempts counter for incorrect guesses.
- Initialize an empty collection to track letters already guessed.


### 🛠️	Implement Gameplay Loop

#### Description
Build the main game loop that asks the player to guess a letter, updates the displayed word progress, and checks whether the player has won or lost.

#### Requirements
Completed program should:

- Prompt the player for a single-letter guess each round.
- Display current progress using placeholders (for example: `_ _ _ _`).
- Decrease remaining attempts only when the guess is incorrect.
- End the game with a win message when the full word is guessed.
- End the game with a lose message when attempts reach zero.
