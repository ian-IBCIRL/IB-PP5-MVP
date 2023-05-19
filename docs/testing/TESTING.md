# Testing
## Test Cases and Execution Report

To return to the main README click [here](/README.md)

* [Back to top of TESTING.md](#testing) 
* [Go to the automated testing section](#automated-testing) 


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
| User can log into account| the new user can sign in and their name appears in the main page and subsequent posts made | Pass|
|User can log out of account| the logout option returns to the main non logged in page with the register and login options| Pass|

---

#### User Navigation Tests

| Test | Expected Result | Actual Result  |
|--|--|--|
|User can navigate to Post Details | Post details are displayed when post clicked in list | Pass |
|User can access menu items| Menu items are appropriate to state and appear in dropdow for CRUD | Pass|
|SuperUser can access admin panel| Admin user menu item appears and goes to Admin page |Pass|

---

#### Account Security Tests

| Test |Expected Result | Actual Result  |
|--|--|--|
|Non logged in user cannot add a post | non loggd in User cannot create a post (cut and paste create link) and returns to the login page |Pass |
|Non logged in user cannot edit a post | non logged in User cannot edit a post (cut and paste edit link) and returns to login page | Pass|
|Non superuser cannot access admin panel| User not logged in trying to get to admin link fails and goes to admin login page | Pass|

---

#### Policy Viewing and Purchasing Tests

| Test |Expected Result | Actual Result  |
|--|--|--|
|User can post a profile or purchase when all required fields are completed | if fields are missing, informative errors are flagged, and completes successfully when form is complete | Pass |
|User can post a profile or purchase when all required fields are completed | user has the option to complete the post/purchase | Pass |
|User can post a profile or purchase when all required fields are completed | user has the option to draft post a profile or purchase which then needs to be edited to be completed | Pass |
|User tries to submit a profile or purchase with empty form is not possible | if form is blank the profile or purchase does not submit |Pass|
|User can view their profile or purchase | user can see the profile or purchase page when submitted |Pass|
|User can edit the profile or purchase| user can only see the edit button on their profile or purchase detail |Pass|
|Edit button does not present on other users profile or purchase| User only gets edit button on their profile or purchase |Pass|
|Delete button does not present on other users profile or purchase| User only sees the delete button on their purchase |Pass|
|User can delete a profile or purchase| User sees delete button on their own profile or purchase |Pass|
|User presented with a further check when they click delete| site further confirms a second check for deleting profile or purchase  |Pass|
|User can comment on a post when all required fields are completed | Comment form is available to all logged in users and can be submitted when complete. | Pass |

--- 

#### Account Tests

| Test |Expected Result | Actual Result  |
|--|--|--|
|User cannot register username to the same as another user| trying an existing username fails if it already exists |Pass|
|User cannot register their email to the same as another user | trying an existing email fails if it is already recorded |Pass|
|User presented with correct date and time on a post | Date and time are shown correctly for time of post submission  |Pass|


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

---

## Google Lighthouse Testing

### Desktop

> index.html
The lighthouse results do vary depending on Internet contention and time of day, affecting the load times for linked resources such as bootstrap, fonts, css and js.

I did also try using Cloudinary responsive image features, but found it added further load.

Details are [Here](https://cloudinary.com/blog/how_to_automatically_create_images_for_responsive_design) 

And I also tried width="auto" to improve responsiveness.

![Google Lighthouse Index](/docs/testing/main-page-lighthouse.png)

> Product Detail Page

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

I did consider following/modifying the instructions to set up further automated testing on this [page](https://www.digitalocean.com/community/tutorials/how-to-add-unit-testing-to-your-django-project).
But as automated testing is not required for the MVP, I did not want take the risk of breaking the MVP.
I will fork the MVP and try to extend automated testing later.

The link I reviewed is also here.
https://www.digitalocean.com/community/tutorials/how-to-add-unit-testing-to-your-django-project

The first step in automated testing is to check the coverage with the `coverage report` command. This shows the name of each file in the project, the number of statements and and test miss/fail, resuting in a percentage coverage for the file and the project as a whole.

All tests in the project can be run with the `./manage.py test' command

Individual folders can be tested such as `./manage.py test polshop` for the main project python files, with an associated coverage report.

To return to the main README click [here](/README.md)

* [Back to top of TESTING.md](#testing) 

