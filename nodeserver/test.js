
var PythonShell = require('python-shell');


var user = '5078281'
var pass = '5709'

var options = {
  mode: 'text',
  scriptPath: '/home/ubuntu/tranz-scrapy/tutorial',
  args: [ user, pass]
};

PythonShell.run('script.py', options, function (err, results) {});