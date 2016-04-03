import dockercloud

def process_event(event):
    print event

events = dockercloud.Events()
events.on_message(process_event)
events.run_forever()
