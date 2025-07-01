const rpc = require('./rpc');

(async () => {
    try {
        while (true) {
            const response = await rpc.call('update_counter');
            console.log(response);

            await new Promise(r => setTimeout(r, 2000));
        }
    } catch (err) {
        console.error(err);
    }
})();
