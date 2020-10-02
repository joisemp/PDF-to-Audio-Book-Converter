from gtts import gTTS
import os  # Imported the required module for text to speech
import PyPDF2

file_name = input("Enter the file name : ")
book = open(file_name, 'rb')
pdf_reader = PyPDF2.PdfFileReader(book)
pages = pdf_reader.numPages
page_no = int(input("Enter a page no to convert it's text to speech : "))

page = pdf_reader.getPage(page_no)
text = page.extractText()

# The text that you want to convert to audio
mytext = text

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here I have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

new_file_name = input("Enter your converted file name : ")
converted_file_name = new_file_name + ".mp3"
myobj.save(converted_file_name)  # Saving the converted audio in a mp3 file in the file name you entered

# Playing the converted file
os.system(converted_file_name)