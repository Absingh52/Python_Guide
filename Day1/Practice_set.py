#  Pratice Set with lotss of Questions 

# Program to print Twinkle twinkle star poem for understanding the i/o functions

print('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,r
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star.''')
#use modules 

from cowpy import cow
import pyjokes
import pyttsx3

# Initialize TTS engine
engine = pyttsx3.init()

# Cow ASCII art
cheese = cow.Moose()
msg = cheese.milk("Hello! I am your Python friend 🐮")
print(msg)

# Greeting
print("\nDo you wanna hear a joke? 😆\n")

# Say something
engine.say("Hello! I am your Python friend.")
engine.say("Do you wanna hear a joke?")

# Get and tell a joke
joke = pyjokes.get_joke()
print("Joke:", joke)
engine.say(joke)

# Run speech
engine.runAndWait()

