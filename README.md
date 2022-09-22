# **Funny-Blog**
<p>
Funny Blog is the place that can bring many people together to share different news or guitars for sale.<br>Each user has the right to create, edit or delete his own ad. <br>
To follow all the news from the blog and last but not least to notice the many guitars that other people have.
</p><br>

![Responsive](/static/images/readme_img/responsive_design.png "Responsive Design")<hr>

<p>The live link for Funny Blog can be found <a href="https://sbnn3-funny-blog.herokuapp.com/">here</a> :)</p><hr>

# **Table of Content**
<ul>
<li><a href="#ux">UX</a></li>
<li><a href="#user-stories">User Stories</a></li>
<li><a href="#design">Design</a></li>
<li><a href="#features">Features</a></li>
<li><a href="#testing">Testing</a></li>
<li><a href="#unfixed-bugs">Unfixed Bugs</a></li>
<li><a href="#technologies-user">Technologies User</a></li>
<li><a href="#deployment">Deployment</a></li>
<li><a href="#credits">Credits</a></li>
<ul><hr>

# **UX**
### **Site Purpose**
<p>
The main intention of this website was for people to be able to find news that interests them and to be able to share their own ideas, to be able to show that they liked a certain post and to be able to create a post for selling their own guitars.
</p><hr>

### **Site Goal**
<p>
The goal was to create a website for artists who want to easily sell their own guitars and in this way attract more artists who can easily navigate the website in the sound of guitars.
</p><hr>

### **Future Site Goals**
<ul>
<li>To create a profile page for each artist.</li>
<li>Every artist profile page to have attached his own posts.</li>
<li>Artists to have possibility to follow each other.</li>
<li>To create the online shop in order to buy the guitars directly from website.</li>
<li>Automatic display regarding remaining guitars, when a guitar was sold, an automatic to be -1 guitar in post.</li>
</ul><hr>

# **User Stories**

### **As an admin:**
<ul>
<li>I can <strong>manage posts</strong> so that <strong>I can create, read, update and delete posts.</strong></li>
<li>I can <strong>create drafts</strong> so that <strong>I can finish writing the content later</strong></li>
<li>I can <strong>approve comments</strong> so that <strong>I can approve or disapprove comments so that I can filter out objectionable comments.</strong></li>
<li>I can <strong>approve guitar posts</strong> so that <strong>I can approve or disapprove the guitar posts.</strong></li>
</ul><hr>

### **As an User**
<ul>
<li>I can <strong>create account</strong> so that <strong>I can leave comments at posts, create my own guitar post and manage it.</strong></li>
<li>I can <strong>create, edit and delete</strong> so that <strong> I can create create new post or/and edit and delete my own posts.</strong></li>
<li>I can <strong>Like/Unlike</strong> so that <strong>I can Like or/and Unlike different posts.</strong></li>
<li>I can <strong>Set Price</strong> so that <strong>I can set a price that i would like to sell my guitar.</strong></li>
</ul><hr>

### **As an Visitor**
<ul>
<li>I can <strong>visit blog</strong> so that <strong>I can see what's new.</strong></li>
<li>I can <strong>like blog posts</strong> so that <strong>I can easily share my feelings.</strong></li>
<li>I can <strong>like guitars posts</strong> so that <strong>I can easily share my feelings.</strong></li>
<li>I can <strong>access guitars posts</strong> so that <strong>I can navigate and see different types of guitars for sale.</strong></li>
</ul><hr>

# **Design**

### **Home Page (Wireframe)**
![Responsive](/static/images/readme_img/home_page.png "Home Page")<hr>

### **Guitars Page (Wireframe)**
![Responsive](/static/images/readme_img/guitars_page.png "Guitars Page")<hr>

### **Guitars Post (Wireframe)**
![Responsive](/static/images/readme_img/guitars_post.png "Guitars Post")<hr>

### **Database Schema**
![Responsive](/static/images/readme_img/database_schema.png "Database Schema")<hr>

### **Typography**
<p>
All fonts were obtained from Google Fonts Library.
<ul>
<li><strong>Alegreya</strong> - Content, Guitars Posts, Blog Posts.</li>
<li><strong>Bebas Neue</strong> - Logo/Navbar</li>
</ul>
</p><hr>

# **Features**

### **Home Page**
![Responsive](/static/images/readme_img/home_page_live.png "Home Page")<hr>

### **Desktop Navigation Bar**
![Responsive](/static/images/readme_img/nav-bar.png "Desktop Navigation Bar")<hr>

### **Mobile Navigation Bar**
![Responsive](/static/images/readme_img/nav-bar-mob.png "Mobile Navigation Bar")<hr>

### **About Page**
![Responsive](/static/images/readme_img/about_page.png "About Page")<hr>

### **Guitars Page**
![Responsive](/static/images/readme_img/guitars_page_live.png "Guitar Page")<hr>

### **Guitars Post**
![Responsive](/static/images/readme_img/guitars_post_live.png "Guitar Post")<hr>

### **Blog Page**
![Responsive](/static/images/readme_img/blog_page.png "Blog Page")<hr>

### **Blog Post**
![Responsive](/static/images/readme_img/blog_post.png "Blog Post")<hr>

### **Sign In Page**
![Responsive](/static/images/readme_img/sign-in.png "Sign In")<hr>

### **Sign Out Page**
![Responsive](/static/images/readme_img/sign-out.png "Sign Out")<hr>

### **Sign Up Page**
![Responsive](/static/images/readme_img/register.png "Sign Up")<hr>

### **Submit Guitar Button**
<ul>
<li>The "Submit Guitar" button can be found on guitars page and is available only for signed in users.</li>
</ul><hr>

![Responsive](/static/images/readme_img/submit_guitarpost.png "Submit Guitar Post")<hr>

### **Edit & Delete Post**
<ul>
<li>The "Edit & Delete" buttons can be found on guitars post page and is available only for signed in users.</li>
</ul><hr>

![Responsive](/static/images/readme_img/edit-delete-post.png "Edit Delete Post")<hr>

### **Features left to implement**
<ul>
<li>Online Shop</li>
<li>Artist Profile</li>
<li>Password Reset</li>
<li>Contact Page</li>
</ul><hr>

# **Testing**
<ul>
1. Django error message after adding submit guitar form:<br>
<li>CSRF token has been added as {{ csrf_token }} instead of {% csrf_token %}</li>
2. Invalid syntax error after creating the GuitarsPagePost:<br>
<li>A comma was missing on 'guitars': guitars,</li>
3. Django error message after adding the GuitarsPage:
<li>I supposed to declare the model name to anywhere but not the class name.</li>
4. After deployment, all website images and style was missing.
<li>Tutors told me that i have to command: python3 manage.py collectstatic<br>
- After every deployment to Heroku.</li>
5. Am I Responsive website wasn't worked with my Heroku link.
<li>I've imported temporarly the xframe_options_except and declared up-front of my main-page. I did my responsive website screenshot and after removed the import and declaration.</li>
</ul>

### **Validator Testing**
<ul>
<li>HTML files pass through the <a href="https://validator.w3.org/">W3C Validator</a> with not HTML issues.</li>
<li>CSS file pass through the <a href="https://jigsaw.w3.org/css-validator/">Jigsaw Validator</a> with not CSS issues.</li>

![Responsive](/static/images/readme_img/css-validator.png "CSS Validator")<hr>

<li>Page has a very good Accessibility on Lighthouse!</li>

![Responsive](/static/images/readme_img/lighthouse.png "Lighthouse")<hr>

<li>Python files passed through <a href="http://pep8online.com/">PEP8 Online</a></li>
</ul><hr>

# **Unfixed Bugs**
<p>After Heroku deployment i've found few bugs that cannot be fixed, please, see below:</p>
<ul>
<li><a href="https://sbnn3-funny-blog.herokuapp.com/music/guitars/">Guitars Page</a>, when you are not sign in is different sizes of guitars cards. When you're sign in, everything is how supposed to be.</li>
<li><a href="https://sbnn3-funny-blog.herokuapp.com/accounts/logout/">Logout Page</a>, when you are trying to logout the page becomes smaller and footer can be found at middle of page.</li>
<li><a href="https://sbnn3-funny-blog.herokuapp.com/new-guitars-store-opened-in-lucan/">Blog Post</a>, Blogs Images in Post doesn't appear anymore, even if the code is totally correct.</li>
</ul><hr>

# **Technologies User**

### **Main Languages Used**

<ul>
<li>HTML 5</li>
<li>CSS</li>
<li>JavaScript</li>
<li>Python</li>
<li>Django</li>
<li>SQL - Postgres</li>
</ul><hr>

### **Framerworks, Libraries & Programs User**
<ul>
<li>Google Fonts - For the font families.</li>
<li>Font Awesome - Icons to the social links in the footer side.</li>
<li>GitPod - HTML,CSS,Python,JavaScript,Django - Workspace.</li>
<li>GitHub - To store my repository.</li>
<li>Balsamiq - Wireframes App.</li>
<li>Am I Responsive? - To make sure that project looks good to all devices.</li>
<li>Django</li>
<li>Bootstrap</li>
<li>DrawSQL</li>
</ul><hr>

### **Installed Packages**
<ul>
<li> 'django<4' gunicorn </li>
<li>dj_database_url psycopg2</li>
<li>dj3-cloudinary-storage</li>
<li>django-summernote <a href="https://summernote.org/">link</a></li>
<li>django-allauth <a href="https://django-allauth.readthedocs.io/en/latest/">link</a></li>
<li>django-crispy-forms <a href="https://django-crispy-forms.readthedocs.io/en/latest/index.html">link</a></li>
</ul><hr>

# **Deployment**
<p>The website has been deployed to Heroku. Please, see below the steps:</p>
<ul>
<li>Install Django & Gunicorn: pip3 install 'django<4' gunicorn</li>
<li>Install Django Database & Psycopg: pip3 install dj_database_url psycopg2</li>
<li>Install Cloudinary: pip3 install dj3-cloudinary-storage</li>
<li>Creating the requirements.txt file with the following command: pip3 freeze --local > requirements.txt</li>
<li>Django Project was created with follow command: django-admin startproject funny_blog .</li>
<li>The Blog app was created with follow command: python3 manage.py startapp blog</li>
<li>App name have to be declared to settings.py file, section APPS.</li>
<li>Migrations command: python3 manage.py migrate</li>
<li>Access Heroku and created new app using Europe as Location.</li>
<li>Added the Heroku Postgres Database to Resources tab.</li>
<li>Access the Heroku App Settings to add the follow keys/values to the configvars:</li>
1. SECRET_KEY | Balaioara1967!<br>
2. PORT | 8000<br>
3. CLOUDINARY_URL | API environment variable<br>
4. DATABASE_URL | the link provided by Heroku<br>
<li>Added the DATABASE_URL, CLOUDINARY_URL, SECRET_KEY to the env.py file.</li>
<li>Added the DATABASE_URL, CLODUINARY_URL, SECRET_KEY to the settings.py file.</li>
<li>Added an import os at the top of env.py file.</li>
<li>Added Heroku link to ALLOWED_HOSTS in settings.py file.</li>
<li>Created the Procfile.</li>
<li>Pushed the project to GitHub.</li>
<li>Connect the GitHub with Heroku throught the Deploy tab.</li>
<li>Connect my GitHub project and after click "Deploy".</li>
<li>Don't forget to collect static on gitpod after deployment.</li>
<li><a href="https://sbnn3-funny-blog.herokuapp.com/">Funny Blog</a> :)</li>
</ul><hr>

# **Credits**
<ul>
<li><a href="https://codeinstitute.net/">Code Institute</a> - for all course material leading up to this project.</li>
<li><a href="https://github.com/SephTheOverwitch">Martina Terlevic</a> -  My mentor at Code Institute for permanently support and feedback.</li>
<li>Code Institute Tututor Team - For help during the lessons and challenges</li>
</ul>


