let stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
let clientSecret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements({clientSecret});
let paymentElement = elements.create('payment');
paymentElement.mount('#payment-element');

function setLoading(Loading){
    if (Loading){
        document.getElementById('spinner').classList.remove('hidden')
        document.getElementById('button-text').classList.add('hidden')
        document.getElementById('submit').disabled = true
    } else {
        document.getElementById('spinner').classList.add('hidden')
        document.getElementById('button-text').classList.remove('hidden')
        document.getElementById('submit').disabled = false
    }
}

let form = document.getElementById('payment-form');

checkStatus()

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    handleSubmit()
});

async function handleSubmit() {
    setLoading(true);

    const { error } = await stripe.confirmPayment({
        elements,
        confirmParams: {
        // Make sure to change this to your payment completion page
        return_url: `${window.location.origin}/checkout/success/`,
        },
    });

    // This point will only be reached if there is an immediate error when
    // confirming the payment. Otherwise, your customer will be redirected to
    // your `return_url`. For some payment methods like iDEAL, your customer will
    // be redirected to an intermediate site first to authorize the payment, then
    // redirected to the `return_url`.
    if (error.type === "card_error" || error.type === "validation_error") {
        showMessage(error.message);
    } else {
        showMessage("An unexpected error occurred.");
    }

    setLoading(false);
}

// Fetches the payment intent status after payment submission
async function checkStatus() {
    const clientSecret = new URLSearchParams(window.location.search).get(
        "payment_intent_client_secret"
    );

    if (!clientSecret) {
        return;
    }

    const { paymentIntent } = await stripe.retrievePaymentIntent(clientSecret);

    switch (paymentIntent.status) {
        case "succeeded":
            showMessage("Payment succeeded!");
            break;
        case "processing":
            showMessage("Your payment is processing.");
            break;
        case "requires_payment_method":
            showMessage("Your payment was not successful, please try again.");
            break;
        default:
            showMessage("Something went wrong.");
            break;
    }
}