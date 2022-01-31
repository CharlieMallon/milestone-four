/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
console.log('clientSecret :>> ', clientSecret);
var stripe = Stripe(stripePublicKey);
let elements = stripe.elements({clientSecret: clientSecret});
var paymentElement = elements.create('payment');
paymentElement.mount('#payment-element');
