# Topic - consumer


from channels.consumer import SyncConsumer
from channels.consumer import AsyncConsumer



class MySynConsumer(SyncConsumer):
    

    def websocket_connect(self, event):
        print('Websocket Connected...')




    def websocket_receive(self, event):
        print('Message Received...')

    
    def websocket_disconnect(self, event):
        print('Websocket Disconnected...')



class MyAsynConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print('Websocket Connected...')

    async def websocket_receive(self, event):
        print('Message Received...')


    async def websocket_disconnect(self, event):
        print('Websocket Disconnected...')


        