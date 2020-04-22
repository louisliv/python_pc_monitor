import tkinter as tk
import json
import os

PADDING_Y = 10

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(padx=15, pady=15, anchor="w")
        self.create_widgets()

    def create_widgets(self):
        self.buttons = {}
        self.text_fields = {}

        this_folder = os.path.dirname(os.path.abspath(__file__))
        constants_json_path = os.path.join(this_folder, 'constants.json')
        self.config_json_path = os.path.join(this_folder, 'config.json')
        config_file = open(self.config_json_path)
        self.config = json.load(config_file)
        config_file.close() 

        with open(constants_json_path) as json_file:
            data = json.load(json_file)

            form_frame = tk.Frame(self)
            form_frame.pack(anchor='w')

            for field_section in data['text_fields_sections']:
                tk_label = tk.Label(
                    form_frame, 
                    text = field_section['title'],
                    font=("", 12)
                )

                tk_label.pack(anchor='w')

                for text_field in field_section['text_fields']:
                    text_field_frame = tk.Frame(form_frame)

                    text_field_label = tk.Label(
                        text_field_frame,
                        text = text_field['label']
                    )

                    text_field_label.pack(side=tk.LEFT, anchor='w')

                    tk_entry = tk.Entry(text_field_frame)
                    tk_entry.pack(anchor='e')
                    tk_entry.insert(0, self.config[text_field['id']])
                    text_field_frame.pack(anchor='w')

                    self.text_fields[text_field['id']] = tk_entry

            button_row = len(data['text_fields_sections'])
            button_frame = tk.Frame(self)
            button_frame.pack()

            for index, button in enumerate(data['buttons'], 0):
                tk_button = tk.Button(
                    button_frame, 
                    text = button['title'],
                    command=self.handle_set_config
                )

                tk_button.grid(row=0, column=index)

                self.buttons[button['name']] = tk_button

    def handle_set_config(self):
        self.set_config()

        f = open(self.config_json_path, "w")
        f.write(json.dumps(self.config))
        f.close()

    def set_config(self):
        for key, text_field in self.text_fields.items():
            current = text_field.get()
            self.config[key] = current
        

root = tk.Tk()
root.title('PC Monitor Connect')
app = Application(master=root)
app.mainloop()