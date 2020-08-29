# milestone-project-Urban Shirts


This project is a startup  business where you find very good T-shirts for a very good price.
My idea at first was to make clothing line where I provide all sorts of clothing them I figured is best to start my business small just to avoid complications, so I decided to only leave I as T-shirts.
This project is inspired by a desire that I had to start a clothing line from a young age, I really didn’t know where to start, but with the help of code institutes mini project I already knew exactly what I wanted to do .iThis application is a T-shirt clothing line for boy and girls at all ages I want this application to be somewhere customers list and leave with the desires fulfilled, I updated the product frequently I do this by changing the prise and even the items sometimes.
## UX
My UX process was to  examine the customer’s requirements and try and think of different ways to include this into not only just a website but a website that is user friendly and easy to navigate around.
### The customers requirements are:
* To be able to register and sign into an account
* To be able to choose a shirt of there choose and add it to the cart when they do so.
* To be able to edit and choose the quantity of items the desire to purchase.
* To be able to rate, comment and even read other customers review of company as a whole.
* To be able to buy items online by adding bank details.

## User stories:
* As a user I want to be able to create an account
* As a user I want to be able to pick the shirt of my choose, edit and delete it from/or in the cart.
* As a user I want to view all available shirts and the price.
* As a user I want to be able to vote on other user’s videos as well as them with my videos
* As a user I want be able to leave a review and rating 
* As a user I want to be able to log out of my account

## Design

### Front-End
My design inspiration was essentially from code institutes mini project . I just modified it slightly to by adding a vote and comment section.I have a few small very basic sketches as I more or less knew in my head how I wanted the site to look. I did my sketches using (…..uxdesign here….). 
I was considering also doing some mobile resolution mockups but its more or less the same except for the mobile menu and the fact that instead of having 3 shirts in a row on a mobile devise you can only see one.
Login/Register Pages These pages are more or less the same design wise. If there is an issue with either login or registration then a brief information message should appear on the screen. New users will be able too register a new account.
home  Page This page displays all the shirts available and it allows you to add the shirt of your choose to the carts.
 carts page On this page you would see all the shirts you added to the cart, fro m there you would purchase your shirts and you would do this by filling a form out where you put your card details.

### Back-End (MySQL Database)
My backend consists of a relatively simple MySQL database. For testing and Development I use the local Cloud 9 Database and then for the live version I use the ClearDB heroku add on. The databases can be set in the applications db.py file with options for local or remote databases.
My Database consists of 4 tables:
* checkout
* products
* sites
* feedback

## Features
The features of this application are as follows:
* Ability to Register, Sign into and Logout of an Account
* Ability to Create, Edit, Delete and View shirts
* Ability to rate and leave a comments about the shirts
* Ability to order shirts of your choose.

## Features Left to Implement
###Technologies Used

In the future I would like to grow my website by adding more product which is not only shirts I would like to make a clothing line for Both male and female from all age groups that provide all sorts of clothing including jumpers, trousers and many more. I also want to make a place where customers can custom design the own shirt then order it it.
Python and Flask
Flask is the Python Framework I’m using for this application

## CSS
I'm using SCSS to build my css style sheets and probably a little  I'm using  Bootstrap 4. I am using bootstrap and a bit of materialize. It doesn't seem to have any  effects that wouldn’t be pleasant for the users and  the over all look is responsive and visually pleasing.
JQuery
I have only used minimal JQuery. I have used it  the mobile menu.
Testing

## Manual Testing
For manual testing I have tested on the following browsers. Firefox, Chrome, and iphone xr. I had to add some fixes on the nabber.
I used an Iphone xr for mobile phone resolution testing and a MacBook Air for all other testing.
After running each possible scenario multiple times, going over each feature, user stories and client requirements I then validated my HTML and CSS using the following:
* HTML Validation
* CSS Validation

## Scenarios
* Try registering a user that already exists on the system
* Register a new user
* Login with incorrect details
* Login in with correct details
* Add items to the cart
* Remove items from the cart 
* Amend t-shirts in the cart
* Logout

## Deployment
During development, all code was written in Cloud 9 and updates were saved and tested locally. Throughout the process I used GitHub to keep track of changes and to maintain version control in my code base.
The development version of my application is on GitHub and I push this code using git push origin master and the code is run and tested on Cloud 9 before being updated to heroku
The production version of my application is deployed to heroku and I push this code using git push heroku master and the live application can be found here.

## Heroku Deployment Steps
1. Go to the Heroku Website and create new app
2. Create requirements.txt and Procfile to tell heroku what is required to run the app
3. Login into Heroku Account via command line and add the newly created app
4. Go back to Heroku Website and in the settings tab click Reveal Config Vars and add IP and PORT vars from Project Config
5. Install ClearDB and import local MySQL Database dump.sql
6. Restart all dynos
7. Finally do an initial git commit and push to heroku

## Content and Media
 Code institute mini project
Bootstrap


