//nodeserver


var PythonShell = require('python-shell');
var express        =         require("express");

var bodyParser     =         require("body-parser");
var app            =         express();
var app2            =         express();


var json ='empty'

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.use('/public', express.static('public'));

app.get('/',function(req,res){
  res.sendfile("public/index1.html");
});
app.post('/bancamarch',function(req,res){
  json=req.body.json;
  
  json = convert_to_table(json)
  //console.log(json);
  res.end("yes");
});
app.listen(3000,function(){
  console.log("Started on PORT 3000");
})




app2.use(bodyParser.urlencoded({ extended: false }));
app2.use(bodyParser.json());

app2.use(express.static(__dirname + '/public'));

app2.get('answer',function(req,res){
  res.send(json);
});

app2.post('/tranz',function(req,res){
  var user=req.body.user;
  var pass=req.body.pass;
  
  lanzar_scrapy(user,pass);
  res.end("yes");
});
app2.listen(3001,function(){
  console.log("Started on PORT 3001");
})





function lanzar_scrapy(us,ps){



var options = {
  mode: 'text',
  scriptPath: '/home/ubuntu/tranz-scrapy/tutorial',
  args: [ us, ps]
};

PythonShell.run('script.py', options, function (err, results) {});

}

function convert_to_table(o){





}
