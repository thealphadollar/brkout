# BrkOut

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)<br>
[![Gitter](https://img.shields.io/gitter/room/:user/:repo.svg)](https://gitter.im/brkout_/Lobby)<br>

A prison escape game with a blend of brick breaking gameplay and innovative implementation of the same to get the look of an escape.

## Screenshots and Gameplay

When you decide to escape
![alt text](/game/assets/HomeScreen.png)

As you fight your way through the unbreakable wall
![alt text](/game/assets/MainGame.png)

You realise that escape might not be as easy as you thought
![alt text](/game/assets/LosingScreen.png)

And when you finally taste the free air after numerous attempts
![alt text](/game/assets/WinningScreen.png)

## Prerequisite

Python2 or Python 3 are the default languages needed for playing this game [on Linux], to check which version of Python you have, type the following in terminal:
```
python --version
```
## Downloading Brkout and Playing

You can use the below commands.

```
sudo apt-get install python-pip
pip install --upgrade pip
```
```
pip install brkout
```
If this does not work, then
```
sudo -H pip install brkout
```
For more info, visit [Pygame download page](http://www.pygame.org/download.shtml)

## Developing on the Game

### On Linux

1. Clone the branch on your local machine:
```
git clone https://github.com/thealphadollar/brkout.git
```
2. Install pipenv (`pip3 install pipenv`) and then install all dependencies (`pipenv install --dev`).
3. Make the required changes
4. Test the game by running `python3 -m game` from the repository's directory.
5. Send a Pull Request

### On Windows

1. Clone the repository by the method appropriate for the Git interface you are using.
2. Install Python 3.x
3. Install the future library
```
pip install future
```
4. Start the game using
```
python -m game
```
5. pip install any missing libraries
6. Always pull changes from the main repo before adding your changes
```
git pull upstream master
```
7. Create a new branch to work on feature
```
git branch <feature_branch>
```
8. Make it the working branch
```
git checkout <feature_branch>
```
9. Commit your changes
10. Merge your feature branch to the master branch when all the changes are done
```
git checkout master
git merge <feature_branch>
```
11. Push your changes to your fork by
```
git push origin master
```
12. Create a new Pull Request on the main repo
13. Make any required changes
14. When the PR is merged, repeat #6 - #14

## Gameplay Help

1. The game can be controlled using arrows keys or the 'w', 'a', 's' and 'd' keys.
2. Spacebar and enter key both act as the selection key.
3. Spacebar or escape key can be used to pause the game.
4. Choose the required difficulty level by clicking on it.
5. Reset the highscore, if needed, by clicking on the 'reset' icon.
6. The game can also be played with a Joystick, which has to be plugged in before you 
   launch the game.It works well with AMKETTE game pad but any standard game pad would also work.

# Enjoy The Game

# Contribute

Please read CONTRIBUTING.md guide to know more.
