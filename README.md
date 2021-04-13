# Georgina's Craft Candles 

Code Institute Diploma in Full-Stack Web Development Milestone 4 - Final Project

<img src="/readme_imgs/logo.png" />

### View the live project: https://ginas-candles.herokuapp.com/

-----------------

### <u>Scope of the project</u>

Georgina's Craft Candles is an e-Commerce site or webshop built with the use of Python & Django. The project code is based on the Code Institute mini-project from Chris Z. The inspiration for the project idea came from my finacée. She was telling me one day how she'd like to get different molds, shapes, materials, coloring, and fragrances to make candles. It hasn't happened yet, but it was enough to push me towards creating a site as my final project which potentially in the future could be used as a real & live site, where she can show & distribute her creations, and people can browse, search, order, and pay for the handcrafted candles.

-----------------

### <u>Contents</u>

-----------------

### <u>UX Design / Presentation</u>

#### User Stories

###### As a visitor, I expect to be able to:

  - browse all products
  - search products
  - select products based on categories 
  - see more details of individual products 
  - add, delete & update the number of products in a bag
  - securely check out and pay for my items of choice
  - view the site on pc or mobile devices
  - see non-broken, responsive layout on all resolutions and screen sizes
  - view all images, not seeing broken images
  - easily navigate on the site and clear feedback on user interaction
  - register on the site and have my details saved

###### As a registered user, I expect in addition to the above to:

  - log in to and log out from my personal profile
  - save & edit my personal details
  - see my previous orders in detail

###### As the administrator, I expect in addition to the above to:

 - provide customers with a secure and safe e-commerce shop
 - make profit from selling products
 - edit products in detail from the frontend
 - delete products from the frontend
 - add, remove or edit categories & products in detail from the backend
 - see all orders generated from the backend
 - manage registered users from the backend

-----------------

#### **Wireframing**

##### **index page**

On the index page, you'd find a full-screen background image which would be also carried over to the other pages of the project. There's a top navigation bar that would be always visible and change form on small screen devices. In the navigation, there are further dropdown options as well as buttons to go to the profile and the basket. A slogan and a button inviting visitors to shop now would be contained in the body. On the bottom, you'd see the slogan again on the left side and some navigation links on the right. This would also be carried over to all pages.

<img src="/readme_imgs/index_mob.png" />
--------

##### **login & registration**

On the left side of the body, you'd see text input rows asking for personal details appropriate for logging in or registering a new user. Below the form, there would be buttons for submitting the form or canceling input.

<img src="/readme_imgs/login_reg_pc.png" />
--------

##### **profile**

After logging in users would be able to enter their shipping details in a form that can be saved and updated afterward on the left side of the page. On the right, the registered user would see a list generated of their previous orders.

<img src="/readme_imgs/profile_pc.png" />
--------

##### **products**

The products would be displayed as cards laid out in a row of 4's, 3's, 2's, and single according to change in the viewport. The top part of the card would contain the product image and the bottom would be showing the name and the price. You are also able to search for products in the navbar.

<img src="/readme_imgs/productsearch_tab.png" />
--------

##### **product in detail**

Again the page would be split in half and the layout would shift according to the viewport. On the left side, you can see the product image and on the right, you'd see the name, price, product description, quantity select controls, and both a 'back' and 'add to bag' button.

<img src="/readme_imgs/productdetail_pc.png" />
--------

##### **shopping bag**

In the shopping bag, there would be a detailed list of items you previously saved to it. You could then adjust the quantity or remove these if you'd like. On interacting with items in the store toasts provide feedback to the users. Adding or removing products would also update prices live. On the bottom, you'd find buttons either to go back to browse more products or to the checkout page.

<img src="/readme_imgs/bag_tab.png" />
--------

##### **checkout**

On the checkout page again you'd see a less detailed list of your items and a form where you need to enter your details and bank details. It would also show you the final total price including delivery. On the bottom, you will find buttons to either go back to the products or complete the order. 

<img src="/readme_imgs/checkout_mob.png" />
--------

##### **order confirmation**

On successfully providing all details and completing the order the user would be redirected to an order confirmation page, where they'd see a report generated with a unique order number, personal details, and the purchased products listed. There would be a button below it pointing back to the products page.

<img src="/readme_imgs/order_pc.png" />
--------

##### **product edit**

You could only see this page if you have the proper credentials. If you are logged in with them, you can access this page either from the navbar to upload a new product or there would be 'edit & delete' links generated on every single item in the shop both in the generic and the detailed product view. This page would contain a form where you can enter all details for the products and add a product image if you have one.

<img src="/readme_imgs/edit_pc.png" />
--------

**Color scheme and typography**

<img src="/readme_imgs/screen_1.jpg" />

The full-page background image of a candle is carried through all pages. Sometimes it does have an overlay on it but this image is the baseline for setting the color scheme of the project. I used dark backgrounds with shades of pink-ish & purple-ish colors which are in good contrast with the backdrop.

<img src="/readme_imgs/colors.png" />

The fonts I used are `Tangerine` for the logo, which is a nice cursive font, and `Fira Sans Condensed` which is a modern style font for all text content in different weights. Most of the text is colored white except for some pink hyperlinks.

<img src="/readme_imgs/text.png" />

-----------------

### Technologies Used

The main frontend development was created using HTML, CSS, JavaScript and their libraries. The main backend development was powered by Python and Django.

## Languages

HTML5, CSS3, JavaScript-ES6, Python3

## Libraries and Packages

- [Django](https://www.djangoproject.com/)
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [Bootstrap (v5.0)](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- [JQuery](https://jquery.com/)
- [Stripe](https://stripe.com/ie)

## Tools

- [Git/GitHub](https://github.com/)
- [GitPod](https://www.gitpod.io/)
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [AWS S3 bucket](https://aws.amazon.com/)

## Databases

- [SQlite3](https://www.sqlite.org/index.html)- database used for development.
- [PostgreSQL](https://www.postgresql.org/) - database used for production.

#### Django-allauth features

Sign Up: The users will be asked to fill out E-mail, User Name and Password to create an account. When the sign up form is submitted, a verification email will be sent to the user's email address to complete the sign up process.

Log In: Users will be asked to input User Name or Email, and Password to login. If the user successfully logged in, a success message will pop up and redirect to the landing page.

Log out: Log out page is accessible from the site menu. After the user successfully signed out button on the sign out page, a success message will appear and redirect to the landing page.

Forgot password: Forgot password page is accessible from Sign In page. Users will be asked to put in an email address which they have used for their registration to the site. An email with a link to reset the password will be sent after submitting the form.

-----------------

## Information Architecture
### Database choice
- Development phase
**SQLight** database was used for the development which is installed with Django. 

- Deployment phase
**PostgreSQL** was used on the deployment stage, which is provided as add-on by Heroku application.

- User model is provided as a default by [Django's authentication system](https://docs.djangoproject.com/en/3.1/ref/contrib/auth/).

### Data Modeling

#### User
The user model utilised for this project is the standard model, provided by from django.contrib.auth.models 

#### Products app models
Within the products app, the <strong>Product</strong> model holds all the data necessary for the functionality of the store. The <strong>Category</strong> model provides the categories on which the products depend on. 

##### Category Model
| Title | Key in db | Form validation type | Data type |
-----  | ---  | --- | ---
Category | name| max_length=254 | CharField

##### Product Model
| Title | Key in db | Form validation type | Data type |
-----  | ---  | --- | ---
category | category | null=True,blank=True, on_delete=models.SET_NULL | ForeignKey 
name | name | max_length=254  | CharField    
scent | scent | max_length=50 | CharField
color | color | max_length=20 | CharField
material | material | max_length=20 | CharField
description | description | none | TextField
price | price | max_digits=6, decimal_places=2 | DecimalField 
promotion | promotion | default=False | BooleanField
product image URL | image_url | max_length=1024, null=True, blank=True | CharField
product image | image | null=True, blank=True | ImageField

<img src="/readme_imgs/dev1.jpg" />

#### Checkout app models
Within the checkout app, the <strong>Order</strong> model holds all the data of the users' order. The <strong>OrderLineItem</strong> model, mainly extracts data from the order model, to get the order number, but also returns the user on the front end the information about each individual product. 

##### Order Model
| Title | Key in db | Form validation type | Data type |
-----  | ---  | --- | ---
Order number | order_number| max_length=32, null=False, editable=False| CharField
User | user_profile  | on_delete=models.SET_NULL,null=True, blank=True, related_name='orders'| ForeignKey
Full name | full_name | max_length=50, null=False, blank=False | CharField
Email | email | max_length=254, null=False, blank=False | EmailField
Phone number | phone_number | max_length=20, null=False, blank=False | CharField
Country | country | blank_label='Country *', null=False, blank=False | CountryField
Postcode | postcode | max_length=20, null=True, blank=True| CharField
Town or city | town_or_city | max_length=40, null=True, blank=True | CharField
Street address1 | street_address1 | max_length=80, null=True, blank=True | CharField
Street address2 | street_address2 | max_length=80, null=True, blank=True | CharField
County | county | max_length=80, null=True, blank=True | CharField
Date | date | auto_now_add=True | DateTimeField
Delivery cost | delivery_cost | max_digits=6,decimal_places=2, null=False, default=0 | DecimalField
Order total | order_total | max_digits=10,decimal_places=2, null=False, default=0 | DecimalField
Grand total | grand_total | max_digits=10,decimal_places=2, null=False, default=0 | DecimalField
Original bag | original_bag | null=False, blank=False, default='' | TextField
Stripe pid | stripe_pid | max_length=254, blank=False, default='' | CharField

##### OrderLineItem Model
| Title | Key in db | Form validation type | Data type |
-----  | ---  | --- | ---
Order | order | null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' | ForeignKey
Product | product | null=False, blank=False, on_delete=models.CASCADE | ForeignKey
Quantity | quantity | null=False, blank=False, default=0 | IntegerField
Total | lineitem_total | max_digits=6, decimal_places=2, null=False, blank=False, editable=False | DecimalField

#### Profile app model
Within the profile app, the <strong>UserProfile</strong> model holds all the data necessary for the user to have a prefilled order form, if they create a profile. This saves them time and energy, when checking out. 

##### UserProfile Model
| Title | Key in db | Form validation type | Data type |
-----  | ---  | --- | ---
User | user | on_delete=models.CASCADE | OneToOneField
Phone number | default_phone_number | max_length=20, null=True, blank=True | CharField
Country | default_country | blank_label='Country *', null=True, blank=True | CountryField
Postcode | default_postcode | max_length=20, null=True, blank=True| CharField
Town or city | default_town_or_city | max_length=40, null=True, blank=True | CharField
Street address1 | default_street_address1 | max_length=80, null=True, blank=True | CharField
Street address2 | default_street_address2 | max_length=80, null=True, blank=True | CharField
County | default_county | max_length=80, null=True, blank=True | CharField


-----------------

### **Version Control**

I used Git for version control and uploading the project to GitHub.

My GitHub repository for this project: https://github.com/Adamsky94/Georginas_Craft_Candles

### Testing write-up

HTML code validated on - https://validator.w3.org/ - only shows errors on templating

CSS code validated on - https://jigsaw.w3.org/css-validator/

<a href="http://jigsaw.w3.org/css-validator/check/referer">
    <img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" />
    </a>

Python3 code is PEP8 compilant - Built in linter plugin in the IDE shows no errors

Responsivity for mobile devices tested on:

- http://www.responsinator.com/ and https://techsini.com/multi-mockup/
- Google Chrome Developer Tools
- Microsoft Edge
- Opera Browser
- Mozilla Firefox on Galaxy S9 setting
- The deployed site on Samsung Galaxy S7 and S8 phones

<img src="/readme_imgs/multimockup.png" />

Used online [autoprefixer](https://autoprefixer.github.io/) for maximum browser compatibility

Used online [code formatter](https://webformatter.com/) to achieve optimal syntax

#### Site in action / login

<img src="/readme_imgs/login.gif" />
--------

#### Site in action / products

<img src="/readme_imgs/products.gif" />
--------

#### Site in action / checkout

<img src="/readme_imgs/checkout.gif" />
--------

#### Site in action / search & modify

<img src="/readme_imgs/search_modify.gif" />
--------

##### Bug Fixes

- Fixtures
<img src="/readme_imgs/db_err.jpg" />

When I was trying to upload the project to Heroku I did not have any fixtures as I have uploaded my products one-by-one in the development phase. I was stuck with this issue, but `Fatima` from the Tutor Team helped me to solve this issue.

- Heroku H10 error

On the first few occasions when I was trying to deploy my project to Heroku I have got `H10 Error`. As I couldn't fix the issue myself I went to the Tutor Team again. `Jo Heyndels & Igor Basuga` were helping me making sure that my file structure is correct, I have every variable set properly and everything is correct in my Procfile. Finally the site was working on the Heroku servers.

- Stripe API key
<img src="/readme_imgs/stripe_err.jpg" />

I came across this error with Stripe that it no longer wanted to accept my test API key. As it was working fine before I got in touch with their `customer service` to try to sort the issue. We concluded that the issue is on my end so I checked the code again. I realized that I have opened a new GitPod workspace and I `improperly copied the test API key` to my environment variables.

- AWS storage
<img src="/readme_imgs/static_err.jpg" />

After setting up an AWS S3 bucket for hosting my static files I noticed that on deploying to Heroku the build log said that my files are `uploaded to a temp` folder. I was not sure if my AWS setup was correct so I went to the Tutor Team again. `Tim Nelson` was helping me making sure that my images are hosted on the AWS servers. We fixed the setup issue at the end.

##### Lighthouse 

Inspecting the deployed page with Google Chrome's `Lighthouse` tool highlighted potentional issues on `accessible name on buttons`, `accessible names on links`, `cross-origin destination` & `document meta description`.

<img src="/readme_imgs/lighthouse_1.png" />

After applying a `fix` for most of the above recommendations the project's Lighthouse score looks like the following:

<img src="/readme_imgs/lighthouse_2.png" />

-----------------

## Deployment

### Heroku Deployment with AWS

This website is deployed on [Heroku](https://www.heroku.com/), following these steps:

1. Install these packages to your local environment, since these packages are required to deploy a Django project on Heroku.

- [gunicorn](https://gunicorn.org/): `gunicorn` is Python WSGI(web server gateway interface) server for UNIX.
- [gninx](https://www.nginx.com/): `gninx` is a free, open-source, high-performance HTTP server and reverse proxy, as well as an IMAP/POP3 proxy server.
- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/): `psycopg2-binary` is PostgreSQL database adapter for the Python programming language.
- [dj-database-url](https://pypi.org/project/dj-database-url/): `dj-database-url` allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.

1. Create a `requirements.txt` file and freeze all the modules with the command `pip3 freeze > requirements.txt` in the terminal.
2. Create a `Procfile` write `web: gunicorn ginas_candles.wsgi:application` in the file.
3. `git add` and `git commit` and `git push` all the changes to the Github repositoty of this project.
4. Go to Heroku and create a **new app**. Set a name for this app and select the closest region (Europe) and click **Create app**.
5. Go to **Resources** tab in Heroku, then in the **Add-ons** search bar look for **Heorku Postgres**(you can type postgres), select **Hobby Dev — Free** and click **Submit Order Form** button to add it to your project.
6. In the heroku dashboard for the application, click on **Setting** > **Reveal Config Vars** and set the values as follows:

| Key                   | Value                        |
| --------------------- | ---------------------------- |
| AWS_ACCESS_KEY_ID     | `Your AWS Access Key`        |
| AWS_SECRET_ACCESS_KEY | `Your AWS Secret Access Key` |
| DATABASE_URL          | `Your Postgres Database URL` |
| SECRET_KEY            | `Your Django Secret Key`     |
| STRIPE_PUBLIC_KEY     | `Your Stripe Public Key`     |
| STRIPE_SECRET_KEY     | `Your Stripe Secret Key`     |
| STRIPE_WH_SECRET      | `Your Stripe WH Key`         |
| USE_AWS               | `True`                       |
| DEVELOPMENT           | `False`                      |


1. Comment out the current database setting in settings.py, and add the code below instead. This is done temporarily to migrate the datbase on Heroku.

```
  DATABASES = {     
        'default': dj_database_url.parse("<your Postrgres database URL here>")     
    }
```

1. Migrate the database models to the Postgres database using the following commands in the terminal: `python3 manage.py migrate`
2. Load the data fixtures(categories, products) into the Postgres database using the following command: `python3 manage.py loaddata <fixture_name>`
3. Create a superuser for the Postgres database by running the following command: `python3 manage.py createsuperuser`
4. Replace the database setting with the code below, so that the right database is used depending on development/deployed environment.

```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```

1. Disable collect static, so that Heroku won't try to collect static file with: `heroku config:set DISABLE_COLLECTSTATIC=1`
2. Add `'ginas-candles.herokuapp.com', 'localhost' to `ALLOWED_HOSTS` in settings.py.

```
ALLOWED_HOSTS = ['ginas-candles.herokuapp.com', 'localhost']
```

1. In Stripe, add Heroku app URL a new webhook endpoint.
2. Update the settings.py with the new Stripe environment variables and email settings.
3. Commit all the changes to Heroku. Medial files are not connected to the app yet but the app should be working on Heroku.

### Amazon Web Service S3

The static files and media files for this deployed site (e.g. image files for product/blog) are hosted in the [AWS](https://aws.amazon.com/) S3 Bucket. You will need to create S3 bucket, complete the setting up and upload static files and media files to the S3 bucket. You can find [Amazon S3 documentation](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html) for more information on the setting. I used CORS configuration below:

```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```

- Setting for static/media files in settings.py

1. Install `boto3` and `django-storages` with command `pip3 install boto3` and `pip3 install django-storages` in your terminal, to connect AWS S3 bucket to Django.
2. Add 'storages' to `INSTALLED_APPS` in settings.py.
3. Add the following in settings.py.

```
if 'USE_AWS' in os.environ:
    # Cache Control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'ginas-candles'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3-eu-west-1.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

    # Roots
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

1. Add custom_storages.py
2. Delete DISABLE_COLLECTSTATIC from Heroku Config Var.
3. Push all the changes to Github/Heroku and all the static files will be uploaded to S3 bucket. By setting up above, Heroku will run python3 manage.py collectstatic during the build process and look for static and media files.

### Automatic Deploy on Heroku

You can enable automatic deploy in the following steps that pushes update to Heroku everytime you push to GitHub.

1. Go to Deploy in Heroku dashboard.
2. At `Automatic deploys`, choose a GitHub repository you want to deploy.
3. Click `Enable Automatic Deploys`.

## Local Deployment

For local deployment, you need to have an IDE (I used GitPod for this project) and you need to install the following:

- Git, Python3, PIP3 Also, you need to create account in the following services if you don't own yet:
- Stripe, AWS (S3 bucket), Gmail

In the IDE you are using, copy and paste the following command into the terminal to clone this repository. `git clone `(the other ways to clone a repository are written in this [GitHub documentation](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository))

#### Cloning this repository

If you'd like to see and work on my code locally feel free to clone the repository. When you clone a repository, you copy the repository from GitHub to your local machine. 

1. On GitHub, navigate to the main page of the repository.

2. Above the list of files, click **Code**.

3. To clone the repository using HTTPS, under "Clone with HTTPS", click . To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click **Use SSH**, then click . To clone a repository using GitHub CLI, click **Use GitHub CLI**, then click .

4. Open Git Bash.

5. Change the current working directory to the location where you want the cloned directory.

6. Type `git clone`, and then paste the URL you copied earlier.

   ```shell
   $ git clone https://github.com/Adamsky94/Georginas_Craft_Candles.git
   ```

7. Press **Enter** to create your local clone.

8. Set up environment variable in your selected IDE, or you can create `.env` file in your root directory and add `.env` to `.gitignore` file, and add the followings to the `.env` file.

```
import os  
os.environ["DEVELOPMENT"] = "True"    
os.environ["SECRET_KEY"] = "<Your Secret Key>"
os.environ["STRIPE_PUBLIC_KEY"] = "<Your Stripe Public Key>"    
os.environ["STRIPE_SECRET_KEY"] = "<Your Stripe Secret Key>"    
os.environ["STRIPE_WH_SECRET"] = "<Your Stripe WH Secret Key>"    
```

9. Install all the required packages with `pip3 install -r requirements.txt`

10. Migrate the models to create a database using in your IDE with `python3 manage.py makemigrations` and `python3 manage.py migrate`

11. Load the data fixtures(categories, products into the database using the following command: `python3 manage.py loaddata <fixture_name>`

12. Create a superuser for the Postgres database by running with `python3 manage.py createsuperuser`

13. Now you can access the app using the command `python3 manage.py runserver`

#### The live project page: https://ginas-candles.herokuapp.com/

-----------------

### Credits

***Antonio Rodriguez*** - My Mentor at Code Institute - Technical and Visual `feedback` on my Project 

***Chris Z*** - **ckz8780** @ GitHub -  Lecturer/Developer at Code Institute - For the MS4 mini-project videos, introduction to `Slack & AWS` , and the `project code` which is the foundation of my own MS4 Project

***Matt Rudge*** - Lecturer/Developer at Code Institute - for [template](https://github.com/Code-Institute-Org/gitpod-full-template) used with `GitPod IDE` for developing this project

***Fatima*** - Code Institute Tutor Team - Help in creating and understanding `fixtures`

***Jo Heyndels & Igor Basuga*** - Code Institute Tutor Team - Help in `fixing Heroku H10 error`

***Tim Nelson*** - Code Institute Tutor Team - Help in `connecting to AWS`

***Maya Saffronhan*** - fellow student - Help in `Deployment, Technologies, Django-allauth & Information Architecture` sections in README.md

***George Becker*** @ [Pexels](https://www.pexels.com/photo/lighted-purple-candle-against-black-background-356660/) - For the `Lighted Purple Candle` background image which I also based the colors of the site on

***Vie Studio*** @ [Pexels](https://www.pexels.com/photo/love-people-art-sign-4439444/) - For the `Coming Soon` image used when no product image uploaded or image URL entered

***Etsy.com*** - [Credit](https://www.etsy.com/) for most `product images and descriptions` due to their respective creators/owners. These assets WILL NOT be used for commercial purposes! 

***Xbox Game Bar*** - [App](https://www.microsoft.com/en-us/p/xbox-game-bar/9nzkpstsnw4p?cid=msft_web_chart&activetab=pivot:overviewtab) used for capturing on-screen content

***EZgif.com*** - [Converting](https://ezgif.com/) the project's `captured videos to GIF's`

***Font Awesome*** - [CDN](https://fontawesome.com/) for icons used in the project

***Google Fonts*** - [CDN](https://fonts.google.com/) for fonts used in the project

***Favicon.io*** - For [generating](https://favicon.io/) `favicon.ico`

***JQuery*** - https://jquery.com/

***Autoprefixer CSS online*** - https://autoprefixer.github.io/