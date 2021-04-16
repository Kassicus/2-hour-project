# 2 Hour Project

## What I was going for
I sat down at 6:30, started a 2 hour timer and started brainstorming something that felt like it could be accomplished in 2 hours.

My original target was to be a wizard killing zombie pigs as they came at the player from either side.

## What I got
This of course, didn't pan out as I very quickly realized that 2 hours was a lot less time than I thought it was. This is the first time I have ever written code under a time limit, and I over-estimated my abilities.

The art quickly devolved, the wizard has some form of shadow, and a little more than 2 seconds of time put into it, everything else was thrown together as fast as I could get it. I originally intended to add audio to the game as well... That got cut entirely.

For some reason my idiot self wrote the collision code in a very stupid way the first time around, and was getting spotty collisions... This led to me fumbling around with the pygame.Rect.colliderect function (something ive never used before) and wasting a ton of time before realizing that I could solve it much simpler.

I also wasted the last 15 minutes trying to get pyinstaller to package the game up into something I could execute, but I have never built for linux before and I don't use windows anymore and didn't want to mess around with wine.

## The Takeaway
This was a lot of fun, if I knew more about pixel art, I would probably jump into a game jam here or there, having evn 24 hours sounds like such a luxury. I am not a game developer, most of the work that I do is simple tools or website related. **If you are reading this far**, please scrutinize my code. I would love input on how I can optimize what I wrote, as im pretty sure its mostly garbage and poorly written.


# How To Install

## Python + Pygame
You will need python 3.8+ and pygame in order to run this (as I never got around to packaging it)

You can download python from https://www.python.org/downloads/ 
After you install that, open a command prompt (Windows) or terminal (MacOS, Linux)
Run these commands (you may need to upgrade or install pip, if so an error will be thrown and it will show you the command you need to run to fix it)

```
pip install pygame
```

## Cloning and Running
Once you have python and pygame installed, either:
 -Download the project and extract it.
 -Clone the directory. 

(I recommend creating a python folder in your Documents folder and cloning/extracting into there)

Then all you have to do is run the game, open a command prompt or terminal and type

```
python3 main.py
```

The game should pop up and you are ready to play!


# Playing the Game
The game is very simple to play, use 'A' and 'D' to move left and right, and shoot with 'SPACE'. If you get touched by a slime, you lose some health.

~Enjoy! (or don't, the game isn't very enjoyable :^))
