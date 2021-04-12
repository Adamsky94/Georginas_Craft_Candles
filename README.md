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
<img src="/readme_imgs/index_mob.png" />

##### **login**
<img src="/readme_imgs/login_reg_pc.png" />

##### **profile**
<img src="/readme_imgs/profile_pc.png" />

##### **products**
<img src="/readme_imgs/productsearch_tab.png" />

##### **product in detail**
<img src="/readme_imgs/productdetail_pc.png" />

##### **shopping baG**
<img src="/readme_imgs/bag_tab.png" />

##### **checkout**
<img src="/readme_imgs/checkout_mob.png" />

##### **order confirmation**
<img src="/readme_imgs/order_pc.png" />

##### **product edit**
<img src="/readme_imgs/edit_pc.png" />

**Color scheme and typography**

<img src="/readme_imgs/colors.png" />

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

#### Site in action / products

<img src="/readme_imgs/products.gif" />

#### Site in action / checkout

<img src="/readme_imgs/checkout.gif" />

#### Site in action / search & modify

<img src="/readme_imgs/search_modify.gif" />

##### Bug Fixes


##### Lighthouse Speed Tool

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

***Maya Saffronhan*** - fellow student - Help in `Deployment` & `Technologies` sections in README.md

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