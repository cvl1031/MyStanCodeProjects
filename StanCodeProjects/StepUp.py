"""
File: StepUp.py
Name: TODO:
------------------------
This file shows Karel picking up 
the beeper at Street 1 Avenue 2,
putting it onto Street 2 Avenue 4.
Karel will be facing East at Street
2 Avenue 5 at the end of this program.
"""

from karel.stanfordkarel import *


Def main ():
  For i in range(3):
     go_in()
     put_99()
     go_out()

  Def go_in():
    move()
    turn_left()
    turn_left()
    turn_left()
    Move()

Def put_99():
   for i in range(99):
      put_beeper()

Def go_out():
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    Move()


def put_99():
    for i in range(99):
        put_beeper()















####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
