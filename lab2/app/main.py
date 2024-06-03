from nicegui import events, ui
from nicegui.events import ValueChangeEventArguments
from utils import caesar_cipher

data = {'source_text':"",
        'dest_text':"",
        'dest_filename':"file2.txt"}
def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    ui.notify(f'{name}: {event.value}')

def handle_upload(e: events.UploadEventArguments):
    text = e.content.read().decode('utf-8')
    data.update(source_text=text)
    ui.notify(f'Uploaded {e.name}')

def handle_save(e: events.UploadEventArguments):
    with open(data['dest_filename'], 'w', encoding='utf-8') as output_file:
        output_file.write(data['dest_text'])
    ui.notify('File saved')

def handle_encrypt():
    new_text = caesar_cipher(data['source_text'], 3)
    ui.notify('Encrypted')
    ui.notify(new_text) 
    data['dest_text'] = new_text 

def handle_decrypt():
    new_text = caesar_cipher(data['source_text'], -3)
    ui.notify('Decrypted')
    ui.notify(new_text) 
    data['dest_text'] = new_text 

with ui.card():
    with ui.row():
        ui.upload(label="Завантажити файл", on_upload=handle_upload, auto_upload=True)
        with ui.column():
            ui.button('Encrypt', on_click=handle_encrypt)
            ui.button('Decrypt', on_click=handle_decrypt)
        ui.input('Назва файлу', value='file2.txt', on_change=lambda e:data.update(dest_filename=e.value))
        ui.button('Зберегти файл', on_click=handle_save)
    with ui.row().classes('w-full flex-nowrap'):
        with ui.card().classes('w-1/2'):
            with ui.element('h2').classes('text-lg'):
                ui.label('Вихідний текст:')
               
                ui.label('').bind_text_from(data, 'source_text')
        with ui.card().classes('w-1/2'):
            with ui.element('h2').classes('text-lg'):
                ui.label('Результат:')
               
                ui.label('').bind_text_from(data, 'dest_text')     
ui.run()