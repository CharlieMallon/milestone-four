# Cake Shop

### Milestone Four

Over the last year or so, Jane has changed a hobby into a growing business. In order to stay competitive and viable, new markets need to be opened, the largest market she can tap into is online shopping. Therefore the next logical step is an e-commerce site. As well as providing sales a full-stack site can give her a greater understanding of her client base and the products that they buy.

## Demo

[View the live website here](#)

<!-- ![mockUp](readme-docs/mockup.jpg) -->

## User Experience (UX)

The aim is to build a user-friendly e-commerce store. It will be based around browsing, selecting and buying products.

Users should be able to view products in a collection or as an individual product. They should be able to search the product base for a particular product or keyword. Items should be easily added and removed from the shopping basket. Users should be able to checkout with ease. Users with a account should be able to see their pervious orders, order status and edit any personal information.

An Admin users should be able to add, edit and remove both products and images conveniently from the frontend. They should be able to edit and update orders status and information.

### User stories
#### Shopper Story 1
-   As a Shopper, I want to browse products and add them to my basket.
#### Acceptance Criteria
-   Show a summary of all products on a page.
-   Be able to filter by
    -   product type
    -   colour
    -   season
    -   dietary restriction
-   Be able to search the product list for key words.
-   Show the detail of an individual product.
-   Mechanism to add multiples of a product to the basket.
-   Confirmation that the product has been added to the basket.
#### Shopper Story 2
-   As a Shopper, I want to be able to view/edit my basket.
#### Acceptance Criteria
-   Show a summary of the basket items.
-   Items have the ability to change quantity.
-   Items can be deleted from the basket.
#### Shopper Story 3
-   As a Shopper, I would like to pay for my items.
#### Acceptance Criteria
-   Inputs are clear and rational.
-   Payments are confirmed on the site and via email.
-   Payment should be taken from the account.
#### Shopper Story 4
-   As a Shopper, I would like to navigate the site easily on any device.
#### Acceptance Criteria
-   Clear menu options.
-   Responsive on all devices.
#### Shopper Story 5
-   As a returning user, I would like to see my previous orders and edit my information.
#### Acceptance Criteria
-   There is a working Register page.
-   The user can log in/out.
-   The account page has a list of orders.
-   The account contains;
    -   Billing address
    -   Name
    -   Dietary requirement
#### Shopper Story 6
-   As a returning user, I would like to re-set my password.
#### Acceptance Criteria
-   A forgotten my password link on the login page.
-   A forgotten my password form, that works.
-   The user can change the password on the account page.
#### Shop Owner Story 1
-   As a Shop Owner, I would like to manage products.
#### Acceptance Criteria
-   There is an add product page
-   There is an edit products page
-   There is a delete products button
-   Deleting a product is easy
-   There should be mechanisms in place to prevent accidental deletion
#### Shop Owner Story 2
-   As a Shop Owner, I would like to manage orders.
#### Acceptance Criteria
-   There is a way to view all orders
-   Orders can be viewed in detail
-   Status of the order can be changed
### Skeleton (wireframes)

**Home page**
<br/>
Welcomes user to the site. Large image with a call to action button. Fixed navigation bar at the top of the page, which will be carried on to the rest of the site, with the logo, name, search bar and menu items.
<br/>
[Mobile](readme-docs/wireframes/phone/Mobile-Home.png) / [Tablet](#) / [Desktop](#)
<br/>

**All products page**
<br/>
The products will be shown in their own cards. Each card will contain an image, price and short description. search and filter products each product should link to its own product.
<br/>
[Mobile](readme-docs/wireframes/phone/Mobile-All_Products) / [Tablet](#) / [Desktop](#)
</br>

**Product page**
<br/>
This page will be a blown up version of the product card on the 'all products' page. The card will contain an image or two of the product, the price, a short description, colour selection dropdown (if applicable), diary requirements dropdown (if applicable), a quantity selector and a buy button.
<br/>
[Mobile](readme-docs/wireframes/phone/Mobile-Product.png) / [Tablet](#) / [Desktop](#)
<br/>

**Shopping Basket page**
<br/>
This will be a list of the products in the basket, each item in the basket will show a small image, product title, colour, dietary requirement, quantity and price. Items will be able to be edited or removed from the shopping basket. Subtotals will be shown at the end of each row with the Total for the order being shown at the bottom of the table. Checkout button will only be accessible when minimum order quality has been met.
<br/>
[Mobile](readme-docs/wireframes/phone/Mobile-Basket.png) / [Tablet](#) / [Desktop](#)
<br/>

**Checkout page**
<br/>
This will contain all the necessary information to check out in a simple form. This form will contain; name, email address, delivery address, billing address (if different) and delivery date. There will also be a comments box that can be used to give any special requests/allergy's or dietary requirement. If the user is logged in fields will be pre-filled with name and delivery address. A brief summary of the charge to made on the account. Stripe will be used for the payment/card details section.
<br/>
[Mobile](readme-docs/wireframes/phone/Mobile-Checkout.png) / [Tablet](#) / [Desktop](#)
<br/>

**We will process your order page**
<br/>
This page confirms that the order has been received. It will confirm the delivery date and that a payment of £xx.xx has been taken, as well as wether any special requests/dietary requirements have been made. It will encourage users who don't have an account, to register for an account so they can track there order.
<br/>
[Mobile](readme-docs/wireframes/phone/Mobile-Order_Success.png) / [Tablet](#) / [Desktop](#)
<br/>

**Register page**
<br/>
This page will allow the user to register for an account using a simple form. This form will contain; name, email address, billing address, password field, dietary requirements, comments box for allergies and confirm password field. If the user has come from the checkout page the form will be pre-filled with the details from the checkout form. This page is also contain a link to the log in page
<br/>
[Mobile](readme-docs/wireframes/phone/Mobile-Register.png) / [Tablet](#) / [Desktop](#)
<br/>

**Login page**
<br/>
This page is a simple log in page, It will have a link to the register page and will prompt users if they don't use a registered email address.
<br/>
[Mobile](readme-docs/wireframes/phone/Mobile-LogIn.png) / [Tablet](#) / [Desktop](#)
<br/>

**Account page**
<br/>
user account
log in/out
register
show personal information
<br/>
[Mobile](readme-docs/wireframes/phone/Mobile-Account.png) / [Tablet](#) / [Desktop](#)
<br/>

**Gallery page**
<br/>
shows pictures of previous orders in a instagram style gallery
<br/>
[Mobile](readme-docs/wireframes/phone/Mobile-Gallery.png) / [Tablet](#) / [Desktop](#)
<br/>

**Admin page**
<br/>
admin user
CRUD functionality for products, images and orders
<br/>
[Mobile](readme-docs/wireframes/phone/Mobile-Admin.png) / [Tablet](#) / [Desktop](#)
<br/>

**Contact page**
<br/>
Contact Form
Facebook option
<br/>
[Mobile](readme-docs/wireframes/phone/Mobile-Contact_Us.png) / [Tablet](#) / [Desktop](#)
<br/>

**Notifications**
<br/>
Notifications will be triggered when:

-   Item is added to basket
-   Item is removed from basket
-   [Mobile](#) / [Tablet](#) / [Desktop](#)
    <br/>

## Design Considerations
This is where I say why I made some of my more controversial decisions.

why checkout on top
## Features
I have split the features into Beta, Issue 1, Issue 2 & Issue 3. The project is currently at the Issue one.
-   ### Beta
    -   Register
    -   Log on/off
    -   Make Responsive on all Devices.
-   ### Issue 1
    -   some sort of user/customer blog
        -   option to post to fb too?
-   ### Issue 2
    -   Track the users?
    -   Add Filters to the products page?
-   ### Issue 3
    -
## Database
![Database](readme-docs/database-image.jpg)
## Technologies Used
### Languages Used
-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JS](https://en.wikipedia.org/wiki/JavaScript)
-   [Django](https://docs.djangoproject.com/en/4.0/)
### Frameworks, Libraries & Programs Used
-   [Google Fonts](https://fonts.google.com/)
-   [Heroku](https://id.heroku.com/)
-   [Cypress](https://docs.cypress.io/guides/overview/why-cypress)
### Resources
-   [Code Institute Course Content](https://courses.codeinstitute.net/)
-   Code Institute **SLACK Community**
-   [Stack Overflow](https://stackoverflow.com/)
-   [YouTube](https://www.youtube.com/)
-   [CSS-Tricks](https://css-tricks.com/)
-   [Balsamiq](https://balsamiq.com/wireframes/)
-   [techsini](https://techsini.com/multi-mockup/)
-   [dbdiagram](https://dbdiagram.io/)
## Testing
Full Testing is detailed in a separate file [here](testing.md).
### Interesting Bugs / Issues
This section will detail the interesting Issues and Bugs that I came across whilst coding and the main ones that I found during testing.

**During coding**

| Issue/Bug | Comments | Final Fix |
| --------- | -------- | --------- |
| image not fully deleting | When a product is deleted the image is left in the database, this could cause storage and coding issues in the future | Installed django cleanup. deletes the image completely from the database. https://pypi.org/project/django-cleanup/0.1.9/ |

**During Testing**

| Issue/Bug | Comments | Final Fix |
| --------- | -------- | --------- |
|           |          |           |

## Deployment
### Project Creation
I used VScode and git to produce this project.
The following commands were used to keep version control
-   `git add .` to stage files before committing
-   `git commit -m "message explaining commit"` to commit the local repository
-   `git push` to push all committed changes to the GitHub repository
### Deployment to Heroku

**Create application:**

1. Navigate to Heroku.com and login or sign up.
2. Click on the new button.
3. Select create new app.
4. Enter the app name, this must be unique.
5. Select region.
6. Click Create App.

**Set up connection to Github Repository:**

1. Click the deploy tab
2. Select GitHub as the deployment method.
3. A prompt to find a github repository to connect to will then be displayed.
4. Enter the repository name for the project and click search.
5. Once the repo has been found, click the connect button.
6. To enable automatic deployment (_optional_)
    1. Scroll to the Automatic deploys section
    2. Choose the branch you want to deploy from
    3. Click Enable Automation Deploys.

**Set environment variables:**

1. Click on the settings tab
2. Click the 'reveal config vars' button.
3. Variables needed:
    - IP
    - MONGO_DBNAME
    - MONGO_URI
    - PORT
    - SECRET_ACCESS_KEY

_These variables change depending on your set up so I will not add mine here._

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/CharlieMallon/milestoneTwo)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

8. Once this has been completed use the following command to install all the packages required.

```
$ pip install -r requirements.txt
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Code

| Source | Comments |
| ------ | -------- |
|        |          |

### Content
-   All content was written by the developer.
-   insperation https://github.com/mitchdavenport88/hop_shop/blob/main/README.md
- https://simpleicons.org/ - social media imgs from here

### Media

-   Stock photos are from Pexels a [Cute Animal Collection](https://www.pexels.com/collections/cute-animals-17ey6em/)


### Acknowledgements

-   My Mentor Brian Macharia for some good guidance.

---

## Notes

Secret key - moved to the env.py before deployment.

Cantelo Treats

facebook - https://www.facebook.com/cantelotreats/?ref=page_internal

## Minimum Requirements

-   Allows users to store and manipulate data records
-   The project must be a brand new Django project, composed of multiple apps
-   Create at least 2 custom django models beyond the examples shown on the course (changing the field names of the miniproject models is not customisation)
-   User can register, log in (and has a reason to do so) - stretch also can DELETE account
-   Shop owner has crud abilities
-   Use stripe for payments
-   Incorporate a main navigation menu and structured layout
-   The frontend should contain some JavaScript logic you have written to enhance the user experience
-   Write a README.md file for your project that explains what the project does and the value that it provides to its users
-   Use gitHub for version control
-   Attribute any code from external sources to its source via comments above the code and (for larger dependencies) in the README
-   Deploy to Heroku.
-   Ensure site is secure.

## Project Idea

Build a site to sell pretty cakes for Cantelo Treats

### External user’s goal:

-   Buy cakes to celebrate.

### Site owner's goal:

-   Sell cakes in their local area

### Potential features to include:

-   Showcase previous work
-   Browse current available products
-   The site owner, logging in as a special user, can add/remove products and images

### Advanced potential feature (nice-to-have):

-   The site owner can view and access their upcoming orders.
-   Messaging between site user and customer is done using facebook or emails (depending on user preference)
-   messaging on site between Customer and Shop owner

## Assessment Criteria

### Pass

| LO1  | Design, develop and implement a full stack web application, with a relational database, using the Django/Python Full Stack MVC framework and related contemporary technologies.              |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.1  | Design a full stack web application to be built using the Django framework and to incorporate a relational database and multiple apps (an app for each potentially reusable component)       |
| 1.2  | Design a front end for a full stack web application that meets accessibility guidelines, follows the principles of UX design, meets its given purpose and provide a set of user interactions |
| 1.4  | Implement at least one form, with validation, that allows users to create and edit models in the backend                                                                                     |
| 1.5  | Build a Django file structure that is consistent and logical, following the Django conventions.                                                                                              |
| 1.6  | Write code that clearly demonstrates characteristics of ‘clean code’                                                                                                                         |
| 1.7  | Define application URLs in a consistent manner                                                                                                                                               |
| 1.8  | Incorporate a main navigation menu and structured layout                                                                                                                                     |
| 1.9  | Demonstrate proficiency in the Python language by including sufficient custom logic in your project                                                                                          |
| 1.10 | Write Python code that includes functions with compound statements such as if conditions and/or loops                                                                                        |
| 1.11 | Design and implement manual, or automated test procedures to assess functionality, usability, responsiveness and data management within the full web application                             |

| LO2 | Design and implement a relational data model, application features and business logic to manage, query and manipulate relational data to meet given needs in a particular real-world domain |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2.1 | Design a relational database schema with clear relationships between entities                                                                                                               |
| 2.2 | Create at least TWO original custom Django models.                                                                                                                                          |
| 2.3 | Create at least one form with validation that will allow users to create records in the database (in addition to the authentication mechanism).                                             |
| 2.4 | All CRUD (create, select/read, update, delete) functionality is implemented.                                                                                                                |

| LO3 | Identify and apply authorisation, authentication and permission features in a full stack web application solution                                 |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3.1 | Implement an authentication mechanism, allowing a user to register and log in, addressing a clear reason as to why the users would need to do so. |
| 3.2 | Implement login and registration pages that are only available to anonymous users.                                                                |
| 3.3 | Implement functionality that prevents non-admin users from accessing the data store directly without going through the code                       |

| LO4 | Design, develop and integrate an e-commerce payment system in a cloud-hosted, full stack web application           |
| --- | ------------------------------------------------------------------------------------------------------------------ |
| 4.2 | Implement a feedback system that reports successful and unsuccessful purchases to the user, with a helpful message |

| LO5 | Document the development process through a git based version control system and deploy the full application to a cloud hosting platform                                                                                                     |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 5.1 | Deploy the final version of your code to a hosting platform and test that it matches the development version.                                                                                                                               |
| 5.2 | Ensure that all final deployed code is free of commented out code and has no broken internal links                                                                                                                                          |
| 5.3 | Ensure the security of the deployed version, making sure to not include any passwords in the git repository, that all secret keys are hidden in environment variables or in files that are in .gitignore, and that DEBUG mode is turned off |
| 5.4 | Use a git-based version control system for the full application, generating documentation through regular commits and in the project README                                                                                                 |
| 5.5 | Create a project README that is well-structured and written using a consistent markdown format                                                                                                                                              |
| 5.6 | Document the full deployment procedure, including the database, and the testing procedure, in a README file that also explains the application’s purpose and the value that it provides to its users                                        |

## Merit

To evidence performance at Merit level, a learner will, in general, demonstrate characteristics of performance at Merit level as outlined below. The learner must achieve ALL Pass and Merit criteria for merit to be awarded.

|          |                                                                                                                                                                                                                        |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.1      | Design and build a real-world full stack MVC application with a front end:                                                                                                                                             |
| 1.1b     | that is easy to navigate and allows the user to find information and resources intuitively                                                                                                                             |
| 1.1c     | where the user has full control of their interaction with the application                                                                                                                                              |
| 1.1d     | where all data (CRUD) actions are immediately reflected in the user interface                                                                                                                                          |
| 1.1e     | where the purpose is immediately evident to a new user                                                                                                                                                                 |
| 1.1f     | which provides a good solution to the user’s demands and expectations                                                                                                                                                  |
| 1.1g     | which has a clear, well-defined purpose addressing the needs of a particular target audience (or multiple related audiences)                                                                                           |
| 1.2      | Produce a codebase that is fully robust                                                                                                                                                                                |
| 1.3      | Follow a Test Driven Development (TDD) approach (for JavaScript and/or Python), demonstrated in the git commits.                                                                                                       |
| 1.4      | Configure the project efficiently through well-kept Procfile, requirements.txt file, settings files, keep the data store configuration in a single location where it can be changed easily.                            |
| 2.1      | Fully describe the data schema in the project README file                                                                                                                                                              |
| 3.1, 4.1 | Demonstrate solid understanding of Django template syntax, logic and usage, placing Django logic in the component where it is best suited (e.g., data handling logic is in the models, business logic is in the views) |
| 5.1      | Use version control software effectively to provide a record of the development process                                                                                                                                |

Error pages

-   404 & 500. 403?
-   include in read me!
-   same error page different messages (in code? root?)
