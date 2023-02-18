
var spawn = require('child_process').spawn,
    child = spawn('sh');
    child.stdin.setEncoding('utf-8');
    child.stdout.setEncoding('utf-8');
    child.stderr.setEncoding('utf-8');
var out = '';
global.out ='';

child.stdout.on('data', (data) => {
 global.out += data.toString();});

child.stderr.on('data', (data) => {
 global.out += data.toString();});


const http = require('http');
var qs = require('querystring');
const server = http.createServer((req, res) => {

if (req.method === 'POST') {
let body= '';
    req.on('data', chunk => {

        body += chunk.toString(); // convert Buffer to string
    });
    req.on('end', () => {
  //      console.log(body);
var post = qs.parse(body);
//console.log(post['com']);
child.stdin.write(post['com']+"\n");
global.out+=" "+post['com']+"\n";
//child.stdout.on('data', (data) => {
// global.out = data.toString();
// console.log(out);
//});

});
}

setTimeout(function(){

if(global.out.length < 20000){
var temp = global.out.slice(0,-1);}
else
{var l = global.out.length;
var temp = global.out.slice(l-20000,-1); }

var temp1 = temp.replace(/\n/g,'<br>');

var temp2 = temp1.replace(/\s/g,'&nbsp;');

//if(global.out!=undefined){res.write(global.out);}


res.writeHead(400,{"Content-Type" : "text/html"});
res.write(`<!doctype html>
        <html><style>
div {white-space:pre;}
</style>
        <body style="font-family:'Courier New';font-size:17px"
bgcolor="white" text="black" OnLoad="document.myform.com.focus();" >

           <form action="/"  method="post" name="myform">${temp2} <input type="text" name="com" style="display:inline-block; border:'1px solid white'; width:780px; color:black;font-family:'Courier New';
font-size:17px;background-color:white"/>
</form>


        </body>
        </html>`);
   

res.end();},400);

});
server.listen(3000);
