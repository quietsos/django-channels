
from channels.consumer import SyncConsumer, AsyncConsumer



class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('Websocket connected....', event)
        self.send({
            'type':'websocket.accept'
        })
        
    def websocket_receive(self,event):
        print('Message Received...', event)
        print('Received message: ', event['text'])
        
    
    def websocket_disconnect(self,event):
        print('Websocket Disconnected...', event)