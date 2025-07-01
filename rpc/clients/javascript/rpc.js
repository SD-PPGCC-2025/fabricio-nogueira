const net = require('net');

function call(func, args = [], kwargs = {}, host = 'localhost', port = 5000) {
    return new Promise((resolve, reject) => {
        const client = new net.Socket();
        let responseData = '';

        client.connect(port, host, () => {
            const payload = JSON.stringify({ func, args, kwargs });
            client.write(payload);
        });

        client.on('data', (data) => {
            responseData += data.toString();
        });

        client.on('end', () => {
            try {
                const response = JSON.parse(responseData);
                resolve(response);
            } catch (err) {
                reject(err);
            }
        });

        client.on('error', (err) => {
            reject(err);
        });
    });
}

module.exports = {
    call: call
}
