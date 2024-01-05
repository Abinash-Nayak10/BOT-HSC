from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
import nltk
from nltk.chat.util import Chat, reflections
import spacy
import os

# Download required nltk data
nltk.download("punkt")

# Create a chatbot instance and train it on some data
chatbot = ChatBot("My Bot")
trainer = ListTrainer(chatbot)
#for files in os.listdir('data/'):
 #   data = open('data/' + files, 'r', encoding='utf-8').readlines()
data_list = ['which colleges are best in odisha',
            'IIT Bhubaneswar,NIT Rourkela,SOA Bhubaneswar',
             'which engineering college are best in odisha',

             'IIT Bhubaneswar,NIT Rourkela,CET Bhubaneswar,KIIT Bhubaneswar,VSSUT Sambalpur,SIT bhubaneswar',
             'which are top secondary  schools',
             '1.DAV Public school,Chandrasekharpur,Bhubaneswar,2.Loyal school ,Bhubaneswar,3.Delhi public school'
             '4.kalinga Bhubaneswar,5.Sai international Bhubaneswar',
             'which school are best for English',
             'Aparna World school Bhubaneswar,DAV Public school Bhubaneswar,St. Xaviers High School Bhubaneswar,'
             'Kendriya Vidyalaya, Bhubaneswar,ODM Public School, Bhubaneswar',
             'which school are best for mathematics',
             'DAV Public School Chandrasekharpur Bhubaneswar,Delhi Public School Kalinga,Cuttack,St. Xaviers High School, Bhubaneswar,SAI International School, Bhubaneswar,Buxi Jagabandhu English Medium School, Bhubaneswar',
             'which hospital are best in odisha',
             'All India Institute of Medical Sciences (AIIMS), Bhubaneswar,SCB Medical College, Cuttack,Kalinga Institute of Medical Sciences (KIMS), Bhubaneswar,Hi-Tech Medical College and Hospital, Bhubaneswar,MKCG Medical College, Berhampur,Veer Surendra Sai Institute of Medical Sciences and Research (VIMSAR), Burla,Hi-Tech Medical College and Hospital, Rourkela,Instt. Of Medical Sciences & SUM Hospital, Bhubaneswar,Pt. Raghunath Murmu Medical College and Hospital, Baripada,Saheed Laxman Nayak Medical College and Hospital, Koraput,Please note that this is not an exhaustive list and there may be other good medical colleges in Odisha as well',
             'best private hospital in odisha',
             ' Some of the best private hospitals in Odisha are:Apollo Hospitals, Bhubaneswar,Kalinga Institute of Medical Sciences (KIMS), Bhubaneswar,AMRI Hospitals, Bhubaneswar,CARE Hospitals, Bhubaneswar,SUM Ultimate Medicare, Bhubaneswar,Kar Clinic and Hospital, Bhubaneswar,Sparsh Hospitals, Bhubaneswar,Hi-Tech Medical College and Hospital, Bhubaneswar,Sunshine Hospital, Bhubaneswar,Ayush Hospital, Bhubaneswar.Please note that this is not an exhaustive list and there may be other good private hospitals in Odisha as well',
             'which department doctors are highly payable',
             'Neurosurgery,Cardiothoracic surgery,Orthopedic surgery,Gastroenterology,Urology,Dermatology,Anesthesiology,Ophthalmology,Radiation Oncology,Hematology/Oncology',
             'the best doctor in neurosurgery of odisha',
             'Dr. Pradyut Ranjan Bhuyan,Dr. Ashok Kumar Mallik,Dr. Akhila Kumar Panda,Dr. Amitav Rath,Dr. Payod Kumar Jena,Dr. Biswajyoti Rath,Dr. Srikant Kumar Sahoo.you can know more to go this-https://drugresearch.in/neurologist/odisha/#:~:text=List%20Of%20The%20Best%20Neurologists%20in%20Odisha%202023,8%20Dr.%20Biswajyoti%20Rath%20%28Neurologist%29%20%28Odisha%29%20More%20items'
             ]
trainer.train(data_list)


def preprocess_input(input_text):
    tokens = nltk.word_tokenize(input_text.lower())
    return " ".join(tokens)


class ChatApp(App):
    def build(self):
        layout = GridLayout(cols=1)

        # Add School button
        school_button = Button(text='SCHOOL', font_size=30)
        school_button.bind(on_press=self.on_school)
        layout.add_widget(school_button)

        # Add College button
        college_button = Button(text='COLLEGE', font_size=30)
        college_button.bind(on_press=self.on_college)
        layout.add_widget(college_button)

        # Add Hospital button
        hospital_button = Button(text='HOSPITAL', font_size=30)
        hospital_button.bind(on_press=self.on_hospital)
        layout.add_widget(hospital_button)

        return layout

    def open_chatbot_interface(self, instance):
        button_text = instance.text
        response = chatbot.get_response(button_text)
        self.output.text += "\nBot: " + str(response)

    def on_school(self, instance):
        # Create a new chatbot instance and train it on the school data
        school_chatbot = ChatBot("My School Bot")
        trainer = ListTrainer(school_chatbot)
        with open('school.yml', 'r', encoding='utf-8') as f:
            training_data = f.read().splitlines()
        trainer.train(training_data)

        layout = GridLayout(cols=1)

        # Add input widget
        self.input = TextInput(multiline=False)
        self.input.bind(on_text_validate=self.on_enter)
        layout.add_widget(self.input)

        # Add output widget
        self.output = Label(text="", font_size=14, text_size=(None, None))
        layout.add_widget(self.output)

        # Add a button to close the window
        close_button = Button(text='Close')
        close_button.bind(on_press=self.close_chatbot_interface)
        layout.add_widget(close_button)

        # Open the window
        self.popup = Popup(title='School Chatbot', content=layout)
        self.popup.open()

    def close_chatbot_interface(self, instance):
        # Close the chatbot window
        self.popup.dismiss()

    def on_college(self, instance):
        self.chatbot = chatbot
        self.chatbot.name = "My College Bot"
        self.chatbot.set_trainer(ListTrainer)
        self.chatbot.train("data/college.yml")

        layout = GridLayout(cols=1)

        # Add input widget
        self.input = TextInput(multiline=False)
        self.input.bind(on_text_validate=self.on_enter)
        layout.add_widget(self.input)

        # Add output widget
        self.output = Label(text="", font_size=14)
        layout.add_widget(self.output)

        # Add a button to close the window
        close_button = Button(text='Close')
        close_button.bind(on_press=self.close_chatbot_interface)
        layout.add_widget(close_button)

        # Open the window
        self.popup = Popup(title='College Chatbot', content=layout)
        self.popup.open()

    def close_chatbot_interface(self, instance):
        # Close the chatbot window
        self.popup.dismiss()

    def on_hospital(self, instance):
        self.chatbot = chatbot
        self.chatbot.name = "My Hospital Bot"
        self.chatbot.set_trainer(ListTrainer)
        self.chatbot.train("data/hospital.yml")

        layout = GridLayout(cols=1)

        # Add input widget
        self.input = TextInput(multiline=False)
        self.input.bind(on_text_validate=self.on_enter)
        layout.add_widget(self.input)

        # Add output widget
        self.output = Label(text="", font_size=14)
        layout.add_widget(self.output)

        # Add a button to close the window
        close_button = Button(text='Close')
        close_button.bind(on_press=self.close_chatbot_interface)
        layout.add_widget(close_button)

        # Open the window
        self.popup = Popup(title='Hospital Chatbot', content=layout)
        self.popup.open()

    def close_chatbot_interface(self, instance):
        # Close the chatbot window
        self.popup.dismiss()

    def on_enter(self, instance):
        user_input = self.input.text
        self.input.text = ""
        preprocessed_input = preprocess_input(user_input)
        response = chatbot.get_response(preprocessed_input)
        self.output.text += "\nYou: " + user_input
        self.output.text += "\nBot: " + str(response)


if __name__ == '__main__':
    ChatApp().run()
