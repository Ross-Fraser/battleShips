
![battleship](assets/images/screenshots/battleship.png)

# Battleship Game - Solo-Play

Welcome to the Battleship Game! In this version of the Battleship game, you'll be challenging yourself to strategically place your fleet and guess the locations of your own ships.


## Contents

* [Design](#design)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#licence)

# Features

## Design

My design process consisted of thinking of each logic step in the game then creating a flowchart detailing the steps as seen below. 

![flowchart](flowcharts.png)

### Playing the Game

1. Open the game in your web browser.
2. Select the board size
3. Position your ships
4. Attack the ships

# Bugs
## Remaining bugs

There is currently 2 bugs which after firing the first round (10 rounds) ValueError displays "Invalid input: Please enter 'F' or 'C'." and also print message "Out of ammo! You Lose.
Game Over!"

# Validator Testing

- PEP8
    - No errors were returned from https://pep8ci.herokuapp.com/


# Deployment

The site was deployed to Heroku.
- Create a new Heroku app.
- Set the config var to Port 8000.
- Set the buildpacks to Python and NodeJS in that order.
- Link the Heroku app to the repository.
- Click on Deploy


## Screenshots

The pep8 validator results

![pep8 validator](assets/images/screenshots/pep8_validator.png)


## Requirments

The only requirments are that you are running python 3.11 and have colorama.

# Credits

- Code Institute for the deployment terminal.