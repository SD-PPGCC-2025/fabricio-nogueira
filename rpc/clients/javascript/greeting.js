const rpc = require('./rpc');

(async () => {
    try {
        const response = await rpc.call('say_hello', ['Mr. Robinson']);
        console.log(response);
    } catch (err) {
        console.error(err);
    }
})();
