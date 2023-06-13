# Testing
## Test Cases and Execution Report

To return to the main README click [here](/README.md)

* [Back to top of TESTING.md](#testing) 
* [Go to the automated testing section](#automated-testing) 

I managed to get [automated](#automated-testing) testing to work for most of the models, with up to 76% coverage overall, according to the coverage [report](/report.txt)

I will continue to develop automated testing and continue to check coverage.

## Home Page testing

Home page: The home page provides the user with a clear understanding as to the purpose of the site. 
There is a clear call to action for the user to login or sign up at the top of the home page. 
The welcome message is clearly visible to the user when they first see the site, using any device.

![Home Page Screenshot](/docs/screenshot/homepage.png)

## Device responsiveness testing

Device responsivness: Each page of the site was tested on a range of relevant devices and checked against the purpose of the page. 

See more details in Lighthouse testing results and attempts to improve image loading with Cloudinary.

![Device Responsiveness Testing](/docs/screenshot/testing/responsive.png)


### Testing Phase

#### Manual Testing

> Each user story was manually tested in line with intended functionality on both desktop & mobile.
> As this project was detailed by User Stories, manual testing was sufficient for all code, and met project requirements.
> If the expected outcome appears then a given test will be noted as a pass. If it does not then a fail is noted.

#### Account Registration Tests
| Test |Expected Result | Actual Result  |
|--|--|--|
| User can create account | the sign up page creates a new user when correctly completed | Pass |
| User can log into account| the new user can sign in and their name appears in the main page and subsequent orders made | Pass|
| User can log out of account| the logout option returns to the main non logged in page with the register and login options| Pass|

---

#### User Navigation Tests

| Test | Expected Result | Actual Result  |
|--|--|--|
|User can navigate to Product Details | Product details are displayed when product clicked in list | Pass |
|User can access menu items| Menu items are appropriate to state and appear in dropdow for CRUD | Pass|
|SuperUser can access admin panel| Admin user menu item appears and goes to Admin page |Pass|

---

#### Account Security Tests

| Test |Expected Result | Actual Result  |
|--|--|--|
|Not logged in user cannot add a product | Not logged in User cannot create a product (cut and paste create link) and returns to the login page |Pass |
|Not logged in user cannot edit a product | Not logged in User cannot edit a product (cut and paste edit link) and returns to login page | Pass|
|Non superuser cannot access admin panel | User not logged in trying to get to admin link fails and goes to admin login page | Pass|

---

#### Policy Viewing and Purchasing Tests

| Test |Expected Result | Actual Result  |
|--|--|--|
|User can save a profile or order when all required fields are completed | if fields are missing, informative errors are flagged, and completes successfully when form is complete | Pass |
|User can save a profile or order when all required fields are completed | user has the option to complete the profile/order | Pass |
|User can save a profile or order when all required fields are completed | user has the option to draft save a profile or order which then needs to be edited to be completed | Pass |
|User tries to submit a profile or order with empty form is not possible | if form is blank the profile or order does not submit |Pass|
|User can view their profile or order | user can see the profile or order page when submitted |Pass|
|User can edit the profile or order| user can only see the edit button on their profile or order detail |Pass|
|Edit button does not present on other users profile or order| User only gets edit button on their profile or orer |Pass|
|Delete button does not present on other users profile or order| User only sees the delete button on their order |Pass|
|User can delete a profile or order| User sees delete button on their own profile or order |Pass|
|User presented with a further check when they click delete| site further confirms a second check for deleting profile or order  |Pass|
|User can comment on a product when all required fields are completed | Comment form is available to all logged in users and can be submitted when complete. | Pass |

--- 

#### Account Tests

| Test |Expected Result | Actual Result  |
|--|--|--|
|User cannot register username to the same as another user| trying an existing username fails if it already exists |Pass|
|User cannot register their email to the same as another user | trying an existing email fails if it is already recorded |Pass|
|User presented with correct date and time on an order | Date and time are shown correctly for time of order submission  |Pass|


#### Admin Tests

| Test |Expected Result | Actual Result  |
|--|--|--|
|Admin can add products to site| Admin panel has the option to add products and products appear when published  |Pass|
|Admin can add FAQs to site| Admin panel has the option to add FAQs and FAQs appear when published  |Pass|
|Admin can edit products and FAQs on site| Admin panel can edit products and FAQs  and updates show on products and FAQs  |Pass|
|Admin can products and FAQs posts on site| Admin panel has delete option and products and FAQs disappear when deleted |Pass|
|Products and FAQs changed by the admin display correctly on main site when updated / added| Changes appear when main site is viewed |Pass|

To return to the main README click [here](/README.md)

* [Back to top of TESTING.md](#testing) 

### User Story

### As a User


- I can rapidly grasp what the website is presenting so that I can determine whether it satisfies my needs.

    - The front page of the website gives the user information about the content of the website.
- I can sign up for a monthly newsletter
    - A newsletter sign up form is provided on the footer of every page.
- I can browse frequently asked questions
    - Every page of the website has a footer with a link to the FAQ page
- I can fill in a contact form if I needed to contact the store owner
    - A form is provided in the contact page which is located at the bottom of the page.

**User Story:**

### As a site I can view the products on the home page so that I can easily browse them 

**Acceptance Criteria:**
- A list of products is available on the home page

**Expected Results**
- A list of Featured  products should be displayed on the page 
- A list of recently added products should be displayed on the page

**Actual Results**
- A list of recently added products is displayed on the page 
- A list of recently added products is displayed on the page 

**Results: Pass**


### As a site user I can see the featured products so that I know which items are featured

**Acceptance Criteria:**
- Users can view the featured products on the home page

**Expected Results**
- A list of Featured  products should be displayed on the page [Image](docs/screenshot/testing/featured-product.png)

**Actual Results**
- A list of recently added products is displayed on the page [Image](docs/screenshot/testing/featured-product.png)

**Results: Pass**


### As a site user I can see the menu all the time so that I don't have to scroll all the way up
**Acceptance Criteria:**
- The navigation menu must be user-friendly and stays on top of the page

**Expected Results**
- The drop down menu opens up on hover, so that users do not need to click on it
- The menu stays on top all the time 

**Actual Results**
- The drop down menu opens up on hover, so that users do not need to click on it
- The menu stays on top all the time 

**Results: Pass**


### As a site user I can search products so that I can find them easily 

**Acceptance Criteria:**
- User can search for products
- User can click on the searched products to view the products

**Expected Results**
- The search bar is located on the nav menu and user have access to search on all pages all time
- Search an item, and if the search is successful, it will display the product, and you can view the product.
- If no item is found, it will tell you '0 Products Found' 
- IT will also show you number of products found

**Actual Results**
- The searched item is displayed on the page if the item is found 
- If no item is found, it will tell you '0 Products Found' 
- It shows the number of products found

**Results: Pass**

### As a site user I can sort out products so that I can view them in different ways 

**Acceptance Criteria:**
- User can sort out the products

**Expected Results**
- Click on the sort out button
- It will display a drop-down menu with different ways of sorting 
- Click on any of the drop-down menus, and the products will be sorted accordingly.

**Actual Results**
- The products are sorted accordingly when clicked on it [Image](docs/screenshot/testing/sort.png)

**Results: Pass**

### As a site user I can **see review of each products ** so that I know the opinion of other people

**Acceptance Criteria:**
- As a site user I can see review of each products so that I know the opinion of other people

**Expected Results**
- The user can see reviews of a product related to a product if a review exists.
- User can create a review for a product 
- User can also see review in the home page in a carousel 

**Actual Results**
- The user can see reviews of a product related to a product if a review exists.
- User can create a review for a product 
- User can also see review in the home page in a carousel 

**Results: Pass**

### As a site user I can change the quantity so that I can add the required number of items in the bag

**Acceptance Criteria:**
- User can change the quantity of the products
- The +/- button will disable at 1 and 100,

**Expected Results**
- Navigate to any product detail page and you will see a +/- button
- Click on the +/- button to change the quantity of the items 
- Click "Add to Bag" to add the product to the bag 

**Actual Results**
- The +/- button changes the quantity of the products

**Results: Pass**

### As a site user I can get notified so that i know every steps i am taking before buying products 
**Acceptance Criteria:**
- Users should know what they are doing by giving them visual interactions

**Expected Results**
- The user should get notified of all the actions they take on the page
- sign in, sign out, add to basket, email notification etc

**Actual Results**
- The user is notified about their interaction

**Results: Pass**

### As a site user I can adjust shopping bag quantity so that I don not have to go back to products to adjust my bag 

**Acceptance Criteria:**
- User can change the quantity of the products
- The +/- button will be disable at 1 and 100,

**Expected Results**
- Navigate to the shopping bag page and you will see a +/- button
- Click on the +/- button to change the quantity of the items 
- Click "Add to Bag" to add the product to the bag 
- The +/- button is disabled at 1 and 100,

**Actual Results**
- The +/- button changes the quantity of the products
- The +/- button is disabled at 1 and 100,

**Results: Pass**

### As a site user I can get email confirmation about my order so that I have all the details of my order 

**Acceptance Criteria:**
- Users can view their order details after they completed the order
- Users need to receive an email with the order confirmation

**Expected Results**
- Navigate to the shopping bag page and complete an order
- You will see checkout success page with your order details 
- You will also receive an email with your order details 


**Actual Results**
- Checkout success page loads with order details 
- An email is sent with order details 

**Results: Pass**

### As a user I can see the number of items in shopping bag so that I can keep track of what I am purchasing 

**Acceptance Criteria:**
- Users can see the number of each product in the bag
- Users can update the number of products from the bag

**Expected Results**
- Navigate to the shopping bag page and you will see a +/- button
- The number of items in the bag is displayed between the + and - buttons 

**Actual Results**
- The number of items in the bag is displayed between the + and - buttons 

**Results: Pass**


### As a site user I can see the price of individual items so that I know how much I am spending on each item 

**Acceptance Criteria:**
- Users can see the number of each product in the bag and their individual price
- Users can see the subtotal of a product as well

**Expected Results**
- Navigate to the ordersheet page and you will see a +/- button
- The number of items in the bag is displayed between the + and - buttons 
- The individual price of each item is displayed on the right side
- Subtotal is displayed at the far end 

**Actual Results**
- The individual price of each item is displayed on the right side
- Subtotal is displayed at the far end 

**Results: Pass**


### As a site user I can see the total cost so that I can track my total purchasing amount 

**Acceptance Criteria:**
- Users can see the total price of the products

**Expected Results**
- Add some products to the shopping bag and navigate to the shopping bag
- The total price of the items in the bag is shown at the bottom, right hand side 

**Actual Results**
- The total price of the items in the bag is shown at the bottom, right hand side 

**Results: Pass**


### Orders and Checkout - Delivery info 

**Acceptance Criteria:**
- As a site user I can enter my delivery and shipping info so that I can checkout quickly and easily

**Expected Results**
- Add a product and go to the shopping bag and go to checkout page
- Enter your details to purchase the product 
- No need to sign up to purchase item unless you want to save your details for future

**Actual Results**
- The Users can fill up the delivery information form 
- The users can purchase products without needing to create an account

**Results: Pass**


### Orders and Checkout - Delete Shopping bag items 

**Acceptance Criteria:**

-  As a site user I can get a notification if i want to delete items from bag so that I can correct my mistake if I pressed the delete button accidentally 

**Expected Results**
- Add a product and go to the shopping bag
- Click on delete product
- Notify users if they really want to delete the product 
- On final confirmation delete the product

**Actual Results**
- Notify users if they really want to delete the product 
- On final confirmation delete the product 

**Results: Pass**

### Orders and Checkout - Delivery cost 

**Acceptance Criteria:**
- As a site user I can see the delivery cost so that I know how much I am paying for delivery 

**Expected Results**
- Add a product to the basket that is less than €30, and you will be notified how much you need to spend more to get free delivery.
- When you go the bag page, you can see the delivery cost for the purchase 

**Actual Results**
- Add a product to the basket that is less than €30, and you will be notified how much you need to spend more to get free delivery.
- When you go the bag page, you can see the delivery cost for the purchase 


**Results: Pass**


### As a site user I can register and login to my account so that I can store my details securely 

**Acceptance Criteria:**
- User needs to receive a confirmation email on registration
- Once the email is confirmed user can log in to the site
- Notify a user about login and account creation

**Expected Results**
- Once you have registered for an account, you will be sent an email
- Once the email confirmed you can log in page where you can login to the site  

**Actual Results**
- Use is able to sign in to the site from the sign in page

**Results: Pass**

### As a site user I can get email confirmation so that I know that my email id is correct

**Acceptance Criteria:**
- User needs to receive a confirmation email on registration
- Once the email is confirmed user can log in to the site
- Notify a user about login and account creation

**Expected Results**
- Click on Account and then Register button from the menu
- Fill out the form and hit sign up
- You will receive an email with a link to verify your email 
- Click on the link in the email 
- You will be brought back to the site to confirm again
- Once confirmed you will be redirected to log in page

**Actual Results**
- Click on Account and then Register button from the menu
- Fill out the form and hit sign up
- You will receive an email with a link to verify your email
- Click on the link in the email 
- You will be brought back to the site to confirm again
- Once confirmed you will be redirected to log in page

**Results: Pass**


### As a site user I can login so that I can keep track of my purchases and store my details securely

**Acceptance Criteria:**
- Notify a user about login to the site
- Give users the option to save their details for the next purchase

**Expected Results**
-  Click on the Sign In button from the menu
-  If you already have your account, fill up the form and click Sign In.
-  You will be redirected to home page
-  A pop up appears saying that 'You are logged in as NAME'
-  In checkout page page you can save your details for future purchases 

**Actual Results**
-  Click on the Sign In button from the menu
-  If you already have your account, fill up the form and click Sign In.
-  You will be redirected to home page
-  A pop up appears saying that 'You are logged in as NAME'
-  In checkout page page you can save your details for future purchases

**Results: Pass**

### As a site I can logout so that my account remains safe

**Acceptance Criteria:**
- Notify a user about log out from the site

**Expected Results**
- Click on the Sign Out button from the menu
- It will ask you if you really want to log out
- A pop up appears saying that 'You have logged out' 
- You will be redirected to home page

**Actual Results**
- Click on the Sign Out button from the menu
- It will ask you if you really want to log out
- A pop up appears saying that 'You have logged out'
- You will be redirected to home page

**Results: Pass**


### As a Store Owner

### As a admin I can add products from the site so that I do not have to log in to the admin site 

**Acceptance Criteria:**
- Store owners can add products

**Expected Results**
- Log in to the site with your admin details
- Go to stock management under the account section in the menu
- Here, you can add a product 

**Actual Results**
- Store owners or admin can add a products without logging into the admin site 

**Results: Pass**

### As a admin I can edit an item so that I can edit and update the items easily 

**Acceptance Criteria:**
- Store owners can edit products

**Expected Results**
- Log in to the site with your admin details
- Go to any product you wish to edit
- Click on the edit button which is only vissible to admin or superuser
- Here, you can edit a product


**Actual Results**
- Store owners or admin can edit a products without logging into the admin site

**Results: Pass**


### As a admin I can delete item so that I can move it from website

**Acceptance Criteria:**
- Store owners can delete products

**Expected Results**
- Log in to the site with your admin details
- Go to any product you wish to delete
- Click on the delete button which is only vissible to admin or superuser
- Here, you can delete a product 
- You will be asked to confirm if you really want to delete the product

**Actual Results**
- Store owners or admin can edit a products without logging into the admin site 

**Results: Pass**

### As a Admin I can add faqs so that I can faqs easily to the page 

**Acceptance Criteria:**
- Store owners can add faqs

**Expected Results**
- Log in to the site with your admin details
- Go to FAQS at the bottom of the page
- Click on ADD FAQS to add new faqs
- Here, you add FAQS 


**Actual Results**
- Store owners or admin can add faqs without logging into the admin site


**Results: Pass**


### As a Admin I can add faqs so that I can faqs easily to the page

**Acceptance Criteria:**
- Store owners can edit faqs

**Expected Results**
- Log in to the site with your admin details
- Go to FAQS at the bottom of the page
- Click on EDIT FAQS to add 
- Here, you edit FAQS 


**Actual Results**
- Store owners or admin can edit faqs without logging into the admin site

**Results: Pass**


### As an admin I can delete faqs so that I can remove from the page

**Acceptance Criteria:**
- Store owners can delete faqs

**Expected Results**
- Log in to the site with your admin details
- Go to FAQS at the bottom of the page
- Click on Delete FAQS to add 
- Here, you edit FAQS

**Actual Results**
- Store owners or admin can edit faqs without logging into the admin site


**Results: Pass**


### As a Admin I can approve or delete comments so that I can keep my website safe 

**Acceptance Criteria:**
- Only the admin can approve or delete comments

**Expected Results**
- Log in to the admin-site with your admin details
- Go to Comment section from the menu on the left hand side
- Click on the comment that you want to approve or delete 

**Actual Results**
- Store owners or admin can approve or delete comments 

**Results: Pass**

---

## Google Lighthouse Testing

### Desktop

- index.html

The lighthouse results do vary depending on Internet contention and time of day, affecting the load times for linked resources such as bootstrap, fonts, css and js.
The necessary bootstrap modules, particularly for Popper dropdown menus and Stripe functionality do add siginificant load, but are essential.
Even with preload statements they still take time to load, so the Lighthouse performance stat is as good as it can be at this time.
I did also try using Cloudinary responsive image features, but found it added further load.
So I managed to get good results by using WEBP file type for images, especially now that Apple IoS supports webp.

Details I found for the Cloudinary options are [Here](https://cloudinary.com/blog/how_to_automatically_create_images_for_responsive_design) 

And I also tried width="auto" to improve responsiveness. 

![Google Lighthouse Index](/docs/testing/main-page-lighthouse.png)

- Product Detail Page

![Google Lighthouse Profile](/docs/testing/detail-page-lighthouse.png)


## HTML W3 Validation

### index.html

![W3 Validation checker](/docs/testing/HTMLValidation.png)
#### Result: No Errors

### Product detail html

![W3 Validation checker](/docs/testing/HTMLValidationDetail.png)
#### Result: No Errors

### CSS Validation

![w3 Jigsaw CSS checker](/docs/testing/CSSValidation.png)
Details [here](https://validator.w3.org/nu/?doc=https%3A%2F%2Fib-polshop.s3.amazonaws.com%2Fstatic%2Fcss%2Fbase.css)
#### Result: Pass - No Errors

### JSHint Validation

![w3 Jigsaw CSS checker](/docs/testing/jshint.png)
#### Result: Pass - No Errors - note about bootstrap expected.

### PyLint Validation

![CodeInst Python checker](/docs/testing/pylint.png)
#### Result: Pass - No Errors - and same across all files for pylint addin for Gitpod/VSCode.

To return to the main README click [here](/README.md)

* [Back to top of TESTING.md](#testing) 

## Automated testing

- Automated testing was conducted for some apps using the "unittest" module from the Python standard library. 
- This library is is integrated into Django's unit tests. 
- I got automated testing to work for most of the models, with up to 76% coverage overall, according to the coverage [report](/report.txt)
- My current coverage report is [here](/report.txt)
- Note the database settings also need to be local to have permissions to set up the test environment.
- See [here](#test-database) for more info about the [test database](#test-database).

I did consider following/modifying the instructions to set up further automated testing on this [page](https://www.digitalocean.com/community/tutorials/how-to-add-unit-testing-to-your-django-project).
But as automated testing is not required for the MVP, I did not want take further risk of breaking the MVP at this late stage, and 76% automated test coverage is decent.
I will fork the MVP and try to add further automated testing later.

The link I reviewed is also here.
https://www.digitalocean.com/community/tutorials/how-to-add-unit-testing-to-your-django-project

The first step in automated testing is to check the coverage with the `coverage run manage.py test  && coverage report` command. 
This shows the name of each file in the project, the number of statements and and test miss/fail, resuting in a percentage coverage for the file and the project as a whole.

All tests in the project can be run with the `./manage.py test' command

Individual folders can be tested such as `./manage.py test checkout` for the checkout app python files, with an associated coverage report.

## Test database

- Note the database settings also need to be local to have permissions to set up the test environment.
  So that means changing the local env.py to redirect the database from the production ElephantSQL to the django local db, by setting DEVELOPMENT to True
  This also means the testing runs in the development CLI/IDE environment and not in production.
  This is primarily so that the Django test libraries can have permission to create, setup and delete the test database.
  This is not something we usually want to do in the production database.
  Although it is possible to use the production database, I did not do so at this time, to avoid further risk and over complication.
  
  I was also able to preload the test database with fixtures code like the following in each test.
  
        fixtures = [  # set up test data
                'categories.json',
                'user.json',
                'May23datadump.json',
                'checkout.json'
        ]
  
### Settings.py settings.

  To get this all to work we can use a conditional statement in settings.py to check a DEVELOPMENT environment variable set to true in env.py, if testing
  Or we could even have a specific TESTING variable.
  If that doesnt work for some reason, we can also un comment the DATABASES settings lines below.

  i.e. in env.py change the DEVELOPMENT variable below to True/exist

        # un-comment to use local test database for testing, not production
        os.environ.setdefault("DEVELOPMENT", "True")

  and/or uncomment/add the following to settings.py, if not in a conditional IF: ELSE:

        #    DATABASES = {
        #        'default': {
        #            'ENGINE': 'django.db.backends.sqlite3',
        #            'NAME': BASE_DIR / 'db.sqlite3',
        #        }
        #    }

  And you can revert to the production settings, which should pull the DATABASE_URL from the environment.

        DATABASES = {
                'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
        }

To return to the main README click [here](/README.md)

* [Back to top of TESTING.md](#testing) 

