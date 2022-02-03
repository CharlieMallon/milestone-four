// get stripe secret and public keys from the checkout page
// remove the quotes using slice
let stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
let clientSecret = $('#id_client_secret').text().slice(1, -1);
// sets up stripe
let stripe = Stripe(stripePublicKey);
// create a instance of elements and create the payment element
let elements = stripe.elements({clientSecret});
let paymentElement = elements.create('payment');
// mount the payment element to the payment element div on the checkout page
paymentElement.mount('#payment-element');

// get the form
let form = document.getElementById('payment-form');

// check stripes payment status
checkStatus()

// add an event listener to the submit button
// prevent the default and run the handle submit function
form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    handlePayment()
});

async function handlePayment() {
    // set loading so user cannot edit
    setLoading(true);

    // get stripe to do its thing
    const { error } = await stripe.confirmPayment({
        elements,
        redirect: 'if_required',
    });

    if (error) {
        // if error print them in a user friendly way
        if (error.type === "card_error" || error.type === "validation_error") {
        showMessage(error.message);
        } else {
        showMessage("An unexpected error occurred.");
        }
        // set loading so user can edit for resubmission
        setLoading(false);
    } else {
        // if no errors get the payment status and go to createOrder
        const { paymentIntent } = await stripe.retrievePaymentIntent(clientSecret);
        let orderStatus = paymentIntent.status
        createOrder(orderStatus)
    }
}


function createOrder(orderStatus){
    if (orderStatus == 'succeeded'){
        // submit the form!
        form.submit()
    } else {
        // if we got here something has gone quite wrong
        showMessage("There has been an issue with your payment.");
    }
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

// If stripe is loading/working deactivate the button and change the text,
// If not activate the button and show buy now text
function setLoading(Loading){
    if (Loading){
        document.getElementById('spinner').classList.remove('hidden')
        document.getElementById('button-text').classList.add('hidden')
        document.getElementById('btn-submit').disabled = true
        document.getElementById('payment-element').disabled = true
    } else {
        document.getElementById('spinner').classList.add('hidden')
        document.getElementById('button-text').classList.remove('hidden')
        document.getElementById('btn-submit').disabled = false
        document.getElementById('payment-element').disabled = false
    }
}

// Print the message in the payment message box
function showMessage(messageText) {
    const messageContainer = document.querySelector("#payment-message");

    messageContainer.classList.remove("hidden");
    messageContainer.textContent = messageText;
}