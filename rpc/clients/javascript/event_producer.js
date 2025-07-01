const rpc = require('./rpc');

function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

(async () => {
    try {
        while (true) {
            let event_time = await rpc.call('event_increment')

            let message = `Mensagem #${event_time.result}`

            await rpc.call('queue_add', [message])
            console.log(message)
            await delay(1000);
        }
    } catch (err) {
        console.error('Erro:', err);
    }
})();
