from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

def calculate(event):
    try:
        index = (4*(int(first_pulse.text) + int(second_pulse.text) + int(third_pulse.text)) - 200)/100
        print(index)
        if int(age_input.text) >= 15:
            if index >= 15:
                app_name.text = 'Низкая работоспособность сердца!'
            elif index >= 11 and index < 15:
                app_name.text = 'Удовлетворительная работоспособность сердца!'
            elif index >= 6 and index < 11:
                app_name.text = 'Средняя работоспособность сердца!'
            elif index >= 0.5 and index < 6:
                app_name.text = 'Работоспособность сердца выше среднего!'
            else:
                app_name.text = 'Высокая работоспособность сердца!'
        elif int(age_input.text) == 13 or int(age_input.text) == 14:
            if index >= 16.5:
                app_name.text = 'Низкая работоспособность сердца!'
            elif index >= 12.5 and index < 16.5:
                app_name.text = 'Удовлетворительная работоспособность сердца!'
            elif index >= 7.5 and index < 12.5:
                app_name.text = 'Средняя работоспособность сердца!'
            elif index >= 2 and index < 7.5:
                app_name.text = 'Работоспособность сердца выше среднего!'
            else:
                app_name.text = 'Высокая работоспособность сердца!'
        elif int(age_input.text) == 11 or int(age_input.text) == 12:
            if index >= 18:
                app_name.text = 'Низкая работоспособность сердца!'
            elif index >= 14 and index < 18:
                app_name.text = 'Удовлетворительная работоспособность сердца!'
            elif index >= 9 and index < 14:
                app_name.text = 'Средняя работоспособность сердца!'
            elif index >= 3.5 and index < 9:
                app_name.text = 'Работоспособность сердца выше среднего!'
            else:
                app_name.text = 'Высокая работоспособность сердца!'
        elif int(age_input.text) == 9 or int(age_input.text) == 10:
            if index >= 19.5:
                app_name.text = 'Низкая работоспособность сердца!'
            elif index >= 15.5 and index < 19.5:
                app_name.text = 'Удовлетворительная работоспособность сердца!'
            elif index >= 10.5 and index < 15.5:
                app_name.text = 'Средняя работоспособность сердца!'
            elif index >= 5 and index < 10.5:
                app_name.text = 'Работоспособность сердца выше среднего!'
            else:
                app_name.text = 'Высокая работоспособность сердца!'
        elif int(age_input.text) == 7 or int(age_input.text) == 8:
            if index >= 21:
                app_name.text = 'Низкая работоспособность сердца!'
            elif index >= 17 and index < 21:
                app_name.text = 'Удовлетворительная работоспособность сердца!'
            elif index >= 12 and index < 17:
                app_name.text = 'Средняя работоспособность сердца!'
            elif index >= 6.5 and index < 12:
                app_name.text = 'Работоспособность сердца выше среднего!'
            else:
                app_name.text = 'Высокая работоспособность сердца!'
    except:
        app_name.text = 'Некорректные данные'
class MyApp(App):
    def build(self):
        global app_name
        global age_input
        global first_pulse
        global second_pulse
        global third_pulse

        app_name = Label(text = 'Работоспособность сердца')
        age_text = Label(text ='Ваш возраст:')
        age_input = TextInput(text = '', multiline = False)
        first_instruction = Label(text = 'Отдохните несколько минут и замерьте пульс в течении 15 секунд')
        first_pulse = TextInput(text='', multiline=False)
        second_instruction = Label(text = 'Сделайте 30 приседаний за 45 секунд и измерьте пульс в течении 15 сек')
        second_pulse = TextInput(text='', multiline=False)
        third_instruction = Label(text = 'Отдохните 30 секунд и измерьте пульс в течении 15 секунд')
        third_pulse = TextInput(text='', multiline=False)
        button = Button(text = 'Посчитать индекс')
        vline = BoxLayout(orientation = 'vertical')
        hline = BoxLayout()
        hline.add_widget(age_text)
        hline.add_widget(age_input)

        vline.add_widget(app_name)
        vline.add_widget(hline)
        vline.add_widget(first_instruction)
        vline.add_widget(first_pulse)
        vline.add_widget(second_instruction)
        vline.add_widget(second_pulse)
        vline.add_widget(third_instruction)
        vline.add_widget(third_pulse)
        vline.add_widget(button)

        button.bind(on_press = calculate)


        return vline

        


app = MyApp()
app.run()
