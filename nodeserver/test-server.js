//simple nodejs server server-client comms



//servidor web



var express = require('express');
var app = express();
var http = require('http');
var io = require('socket.io');


app.use(express.static('public'));


var server = http.createServer(app).listen(3001);

io = io.listen(server);


//app.get('/', function (req, res) {   res.send('Hello World');})


//io.send('j');

setInterval(function(){ io.emit('message','test'); }, 3000);






io.sockets.on("connection",function(socket_web){

console.log('client connected');

//recibo información del cliente
    socket_web.on("message",function(data){
        /*This event is triggered at the server side when client sends the data using socket.send() method */

 
			console.log(data)

    });
    

    

      
  
 
});





