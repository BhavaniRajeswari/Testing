from nicegui import events,ui

ui.label('Welcome click below to upload an audio files')

#ui.run()

ui.upload(on_upload=lambda e: ui.notify(f'Uploaded {e.name}'),
          on_rejected=lambda: ui.notify('Rejected!'),
          max_file_size=1_000_000).classes('max-w-full')

with ui.dialog().props('full-width') as dialog:
    with ui.card():
        content = ui.markdown()

def handle_upload(e: events.UploadEventArguments):
    text = e.content.read().decode('utf-8')
    content.set_content(text)
    dialog.open()

ui.upload(on_upload=handle_upload).props('accept=.md').classes('max-w-full')

ui.run()

ui.run()