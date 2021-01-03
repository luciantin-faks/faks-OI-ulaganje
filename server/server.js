const express = require('express');
const path = require('path');
const app = express();
const WebSocket = require('ws')
const wsServer = new WebSocket.Server({port:9090});

const {spawn} = require('child_process');

const staticFileMiddleware = express.static(path.join(__dirname, 'dist'));
app.use(staticFileMiddleware);

const port = 8080;
app.listen(port, () => {
    console.log(`App listening on port ${port}!`);
});

wsServer.on('connection',socket =>{
    socket.on('message',message=>{
        var largeDataSet = [];
        const python = spawn('python3', ['app.py']);
        python.stdout.on('data', function (data) {
            largeDataSet.push(data);
        });
        python.on('close', (code) => {
            socket.send(`${largeDataSet}`)
        });
    })
})



// const express = require('express')
// const {spawn} = require('child_process');
// const app = express()
// const port = 3000
//
// app.get('/', (req, res) => {var largeDataSet = [];
//     // spawn new child process to call the python script
//     const python = spawn('python3', ['app.py']);
//     // collect data from script
//     python.stdout.on('data', function (data) {
//         console.log('Pipe data from python script ...',data);
//         largeDataSet.push(data);
//     });
//     // in close event we are sure that stream is from child process is closed
//     python.on('close', (code) => {
//         console.log(`child process close all stdio with code ${code}`);
//         // send data to browser
//         console.log(largeDataSet)
//         res.send(largeDataSet.join(""))
//     });
//
// })
// app.listen(port, () => console.log(`Example app listening on port ${port}!`))
