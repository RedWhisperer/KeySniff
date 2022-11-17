const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const yargs = require('yargs');
const app = express()

app.use(bodyParser.urlencoded({ extended: true }));

const cmdArgs = yargs.argv;

app.post('/upload', (req, res) => {
    const data = req.body.payload;
    const client_key = req.body.key;
    if (client_key == cmdArgs.key) {
        fs.appendFile(cmdArgs.output, '[+] ' + data + '\n', (err, data) => {
            if (err) {
                console.log(err);
            } else {
                console.log('[+] File was updated!')
            }
        });
        res.send('TNX')
    } else {
        res.send('NOT FOUND');
    }
})

const PORT = cmdArgs.port
app.listen(PORT, () => console.log('[+] Upload server is running on port: ', PORT))
