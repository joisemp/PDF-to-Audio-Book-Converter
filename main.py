from gtts import gTTS
import os  # Imported the required module for text to speech

# The text that you want to convert to audio
mytext = input("Enter the text that you want to convert to speech : ")

# Language in which you want to convert
language = 'ml'

# Passing the text and language to the engine,
# here I have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

converted_file_name = str(input("Enter your new file name with extension : "))
myobj.save(converted_file_name)  # Saving the converted audio in a mp3 file in the file name you entered

# Playing the converted file
os.system(converted_file_name)