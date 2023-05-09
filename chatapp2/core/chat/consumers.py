from channels.generic.websocket import WebsocketConsumer
import json
from asgiref import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_code']
        self.group_name = f'room_{self.room_name}' 

        async_to_sync(self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        ))

        self.accept()

        data = {'type':'connected'}
        self.send(taxt_data = json.dumps(
            {'payload':'connected'}
        ))
        
    def receive(self, text_data):
        pass
    def disconnect(self, close_code):
        pass