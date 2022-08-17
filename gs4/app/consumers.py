from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer


class MySyncConsumer(SyncConsumer):
    
    def websocket_connect(self,event):
        print("Websocket connected....", event)
        self.send({
            'type': 'websocket.accept',
        })
        
    def websocket_receive(self,event):
        print("Message received from client..", event)
        print(event['text'])
        
        self.send({
            'type':'websocket.send',
            'text':'Message send from application to client',
            
        })
        
        
    def websocket_disconnect(self,event):
        print("Websocket disconnect...", event)
        raise StopConsumer()
    
    
    
        
class MyAsyncConsumer(AsyncConsumer):
    
    async def websocket_connect(self,event):
        print("Websocket connected...", event)
        await self.send({
            'type':'websocket.accept',
        }) 
        
        
    async def websocket_receive(self,event):
        print("Message receive from client...", event)
        print(event['text'])
        
        await self.send({
            'type':'websocket.send',
            'text':'message from application to client',
            
        })
        
    async def Websocket_disconnect(self,event):
        print('Websocket disconnect...', event)
        raise StopConsumer()
 
 

    
            