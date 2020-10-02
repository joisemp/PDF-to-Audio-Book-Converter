from gtts import gTTS
import os  # Imported the required module for text to speech
import PyPDF2

file_name = input("Enter the file name : ")
book = open(file_name, 'rb')  # converting the file to binary format
pdf_reader = PyPDF2.PdfFileReader(book)
pages = pdf_reader.numPages
page_no = int(input("Enter a page no to convert it's text to speech : "))

page = pdf_reader.getPage(page_no)  # storing the entered page no to the variable page
text = page.extractText()  # extracting text from the page

my_text = text  # assigning the extracted text to the variable my_text

language = 'en'

my_obj = gTTS(text=my_text, lang=language, slow=False)

new_file_name = input("In which name do you like to save the audio file : ")
converted_file_name = new_file_name + ".mp3"
my_obj.save(converted_file_name)  # Saving the converted audio in a mp3 file in the file name you entered

os.system(converted_file_name)  # Playing the converted file
