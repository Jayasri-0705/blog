📝 Blog Project

A full-stack blog web application built with Django. Visitors can browse posts, search by keyword, and read individual articles. The site is deployed on Render with a PostgreSQL database.

🔗 Live Demo: blog-project-k9vg.onrender.com

⏳ The app is hosted on a free tier, so the first load may take 30–60 seconds while the server wakes up.

✨ Features
Home page listing the latest blog posts with images and short previews
Pagination (5 posts per page)
Search posts by keyword
Individual post pages with clean, SEO-friendly URLs (slugs)
Post categories
About and Contact pages
Django admin panel to create, edit, and delete posts
Deployed to production on Render
🛠️ Tech Stack
Area	Technology
Backend	Python, Django 6
Database	PostgreSQL (production) via psycopg2 and dj-database-url
Frontend	HTML, CSS, Django Templates
Static files	WhiteNoise
Server	Gunicorn
Deployment	Render
📁 Project Structure
blog/
├── blog/                  # Main blog app (models, views, urls)
├── mysite/                # Project settings and configuration
├── templates/             # HTML templates
├── about_data.json        # Data for the About page
├── blog_data.json         # Blog post data
├── create_superuser.py    # Script to create an admin user
├── build.sh               # Build script used for deployment
├── Procfile               # Process file for deployment
├── manage.py              # Django management script
└── requirements.txt       # Python dependencies
🚀 Getting Started (Run Locally)
Prerequisites
Python 3.10 or higher
pip
Git
Installation
Clone the repository
bash
   git clone https://github.com/Jayasri-0705/blog.git
   cd blog
Create and activate a virtual environment
bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS / Linux
   source venv/bin/activate
Install dependencies
bash
   pip install -r requirements.txt
Apply database migrations
bash
   python manage.py migrate
Create an admin user
bash
   python manage.py createsuperuser
Start the development server
bash
   python manage.py runserver
Open http://127.0.0.1:8000/ in your browser.

To add or manage posts, go to http://127.0.0.1:8000/admin/ and log in with the account you created.

☁️ Deployment

This project is deployed on Render:

gunicorn runs the application
whitenoise serves static files
dj-database-url reads the PostgreSQL connection from an environment variable
build.sh and Procfile define the build and start steps
🔮 Future Improvements
User registration and login
Comment system on posts
Rich text editor for writing posts
Like and bookmark features
Unit tests
👩‍💻 Author

Jayasri

GitHub: @Jayasri-0705

⭐ If you like this project, consider giving it a star!
