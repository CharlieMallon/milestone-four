# Testing of Cake Shop

## User stories

### Shopper Story 1 - PASS
-   As a Shopper, I want to browse products and add them to my basket.
### Testing Summary
There is a summary page which you can filter by category, use the search bar to search for terms and sort by price, name and category.  Clicking on the image or product title takes you to a product page with all the details about the product. the user can add multiples of a product to the basket and there is feedback telling the user what they have added to the basket in the form of a Message bar above the search bar.

#### Shopper Story 2 - PASS
-   As a Shopper, I want to be able to view/edit my basket.
### Testing Summary
The basket is visible in the top right corner of every page and in the nav bar. when clicked on it takes the user to a summary of the items in the basket, with delivery cost and total price of the order. The product quantity can be changed from the basket page and the line item can be deleted. When Empty the basket page encourages the user to shop. When minimum order quantity has not been met it is clear that you cannot checkout.
#### Shopper Story 3
-   As a Shopper, I would like to pay for my items.
### Testing Summary - FAIL
When the checkout button is clicked it takes the user to a checkout form. The form fields are logical and set in sections.  However the next buttons re-load the page instead of progressing the form. The stripe card needs opening twice to see all of the fields. When an incorrect information is put into the card field it is clear and when the card is declined a message is displayed. The containing card's height is not responsive when errors are displayed meaning the card has to be closed and re-opened to see the buttons. When correct information is inputted the card payment is taken, and the order is created, the user is re0direct to a summary page, the basket is emptied and the user is given a message that an email has been sent (not-the site doesn't currently support email, see readme for more details)
#### Shopper Story 4
-   As a Shopper, I would like to navigate the site easily on any device.
### Testing Summary - FAIL
On Mobile and Tablet there are clear menu options, the Nav bar slides nicely in from the right to display the options clearly and concisely. However it also does this on Desktop which is not expected.
#### Shopper Story 5
-   As a returning user, I would like to see my previous orders and edit my information.
### Testing Summary

#### Shopper Story 6
-   As a returning user, I would like to re-set my password.
### Testing Summary

#### Shopper Story 7
-   As a user, I would like contact the store owner.
### Testing Summary
