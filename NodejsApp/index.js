// 1 vamos a llamar el paquete de mysl
const mysql=require('mysql');
// 2 llamar express
const express = require('express');
// 3 llamar body-parser
const bodyparser= require('body-parser');
//4 crear nueva instancia de express
var app = express();
//5 llamar json request
app.use(bodyparser.json());
//6. crear mysql coneccion

var mysqlconnection= mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'market'
});
mysqlconnection.connect((err)=>{
    if(!err)
        console.log('hay conexion');
    else
        console.log('la conexion fallo'+JSON.stringify(err,undefined,2));
});

app.listen(3000,()=> console.log('..:el servidor esta corriendo sobre el puerto 3000:..'));

//9 read all users
app.get('/list_user',(req,res)=>{
    mysqlconnection.query('SELECT * FROM mark',(err,rows,fields)=>{
        if(!err)
        console.log(rows);
        res.send(rows);
        else
        console.log(err);

    })
});
