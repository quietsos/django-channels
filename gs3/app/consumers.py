# Topic - Routing

from channels.consumer import  SyncConsumer, AsyncConsumer



class MySyncConsumer(SyncConsumer):


    def websocket_connect(self, event):
        print('Websocket connected...', event)
        self.send({
            'type':'websocket.accept'
        })

    def websocket_receive(self,event):
        print('Message Received...', event)
        print('Message is: ',event['text'])

    def websocket_disconnect(self,event):
        print('Websocket Disconnected...', event)




class MyAsyncConsumer(AsyncConsumer):


    async def websocket_connect(self, event):
        print('Websocket connected...', event)

    async def websocket_receive(self,event):
        print('Message Received...', event)

    async def websocket_disconnect(self,event):
        print('Websocket Disconnected...', event)

