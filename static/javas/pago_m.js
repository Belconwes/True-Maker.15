
const mp = new MercadoPago('APP_USR-a4aff583-5735-4121-b959-786138c9e851');
const bricksBuilder = mp.bricks();
mp.bricks().create("wallet", "wallet_container", {
    initialization: {
        preferenceId: "<PREFERENCE_ID>",
        
    },
 });
 console.log(preferenceId);