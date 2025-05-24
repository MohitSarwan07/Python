# print('''
# Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Then the traveler in the dark
# Thanks you for your tiny spark,
# How could he see where to go,
# If you did not twinkle so?

# In the dark blue sky you keep,
# Often through my curtains peep
# For you never shut your eye,
# Till the sun is in the sky.

# As your bright and tiny spark
# Lights the traveler in the dark,
# Though I know not what you are,
# Twinkle, twinkle, little star.

# ''')
# problem 3
# import pyttsx3
# engine = pyttsx3.init()
# engine.say("hey mohit")
# engine.runAndWait()

# problem 4

# import os

# def list_directory_contents(path='/'):
#     try:
#         # List all entries in the directory
#         entries = os.listdir(path)
#         if not entries:
#             print(f"The directory '{path}' is empty.")
#         else:
#             print(f"Contents of '{path}':")
#             for entry in entries:
#                 print(entry)
#     except FileNotFoundError:
#         print(f"Error: The directory '{path}' does not exist.")
#     except PermissionError:
#         print(f"Error: Permission denied to access '{path}'.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# # Example usage
# list_directory_contents()  # Lists contents of the current directory
# # list_directory_contents('/path/to/directory')  # Replace with the desired path
