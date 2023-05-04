<a name="readme-top"></a>



<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/mylogo.png" alt="Logo" width="105" height="80">
  </a>

  <h3 align="center">News_Portal</h3>

  <p align="center">
    A news website that allows users to write and read their own articles and news on a wide range of categories
    <br />
    <a href="https://github.com/Dmitro-belous/News_Portal"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Dmitro-belous/News_Portal">View Demo</a>
    ·
    <a href="https://github.com/Dmitro-belous/News_Portal/issues">Report Bug</a>
    ·
    <a href="https://github.com/Dmitro-belous/News_Portal/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

News_Portal is a dynamic news website built on the Django framework and using materials from Skillfactory. It offers users a platform to explore a diverse range of categories and publish their own news articles, creating a vibrant community of readers and writers.

Opportunities provided by the project:
* On the website, you can read the latest news and articles on various spheres of life, which are conveniently sorted by categories
* You can subscribe to categories that interest you and follow their updates via email
* You will receive a weekly update on the latest news and articles in the categories you have subscribed to, as well as a notification when a new post is added
* If you want to share your knowledge, skills, or thoughts on a certain topic, you can become an author and write your own articles and news

Stay up-to-date with the latest happenings from around the world on News_Portal!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][PythonBadge]][Python-url]
* [![Django][DjangoBadge]][Django-url]
* [![Redis][RedisCloudBadge]][RedisCloudUrl]
* [![Celery][CeleryBadge]][Celery-url]
* [![Allauth][AllauthBadge]][Allauth-url]
* [![Start Bootstrap][SBBadge]][SBUrl]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an installation guide for News_Portal on a local computer running the Windows operating system.
To get a local copy up and running follow these simple example steps.

### Prerequisites

* Git - you can download the installer from <a href="https://git-scm.com/downloads">the official website</a>
* Python 3.6 and higher - for installing Django, Celery, Redis, and Allauth
* Redis Cloud account - to work with Redis Cloud and Celery

### Installation

1. Register for <a href="https://redis.com/try-free/">Redis Cloud</a> and create a database. You will receive a connection URL for the Redis Cloud database.
2. Install Python by following <a href="https://www.python.org/downloads/windows/">the official Python documentation</a>.
3. Clone the News_Portal repository to your local computer.
   ```cmd
   git clone https://github.com/Dmitro-belous/News_Portal.git
   ```
4. Navigate to the project directory and create a Python virtual environment.
   ```cmd
   cd news_portal
   python -m venv env
   ```
5. Activate the virtual environment.
   ```cmd
   env/scripts/activate
   ```
6. Install dependencies.
   ```cmd
   pip3 install -r requirements.txt
   ```
7. In the **settings.py** file, replace `EMAIL_HOST_USER`, `DEFAULT_FROM_EMAIL`, `EMAIL_HOST_PASSWORD`, `REDIS_LOGIN`, `REDIS_PASSWORD`, `REDIS_ENDPOINT`, `REDIS_PORT`, `SECRET_KEY` with the corresponding values that you obtained when creating a Redis Cloud database and installing Django and Allauth.
   ```cmd
   SECRET_KEY = os.getenv('SECRET_KEY')
   EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
   EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
   DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')
   CELERY_BROKER_URL = f'redis://{os.getenv("REDIS_LOGIN")}:{os.getenv("REDIS_PASSWORD")}@{os.getenv("REDIS_ENDPOINT")}:{os.getenv("REDIS_PORT")}'
   CELERY_RESULT_BACKEND = f'redis://{os.getenv("REDIS_LOGIN")}:{os.getenv("REDIS_PASSWORD")}@{os.getenv("REDIS_ENDPOINT")}:{os.getenv("REDIS_PORT")}'
   ```
8. Run database migrations.
   ```cmd
   python manage.py migrate
   ```
9. Create a superuser.
   ```cmd
   python manage.py createsuperuser
   ```
10. Run the server.
   ```cmd
   python manage.py runserver
   ``` 
11. Open your web browser and navigate to http://127.0.0.1:8000/news. You will see the home page of News_Portal.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add requirements.txt
- [x] Hide all confidential information
- [ ] Add the ability to view and edit the user profile page
- [ ] Add the ability to comment on posts
- [ ] Add a rating system: the ability to like/dislike authors, posts, or comments

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@dmitrobelous](https://twitter.com/dmitrobelous) - dimon20_20@mail.ru

Project Link: [https://github.com/Dmitro-belous/News_Portal](https://github.com/Dmitro-belous/News_Portal)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Choose an Open Source License](https://choosealicense.com)
* [Skillfactory](https://apps.skillfactory.ru)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [React Icons](https://react-icons.github.io/react-icons/search)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Dmitro-belous/News_Portal.svg?style=for-the-badge
[contributors-url]: https://github.com/Dmitro-belous/News_Portal/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Dmitro-belous/News_Portal.svg?style=for-the-badge
[forks-url]: https://github.com/Dmitro-belous/News_Portal/network/members
[stars-shield]: https://img.shields.io/github/stars/Dmitro-belous/News_Portal.svg?style=for-the-badge
[stars-url]: https://github.com/Dmitro-belous/News_Portal/stargazers
[issues-shield]: https://img.shields.io/github/issues/Dmitro-belous/News_Portal.svg?style=for-the-badge
[issues-url]: https://github.com/Dmitro-belous/News_Portal/issues
[license-shield]: https://img.shields.io/github/license/Dmitro-belous/News_Portal.svg?style=for-the-badge
[license-url]: https://github.com/Dmitro-belous/News_Portal/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/Dmitro-belous
[product-screenshot]: images/screenshot.png
[PythonBadge]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[DjangoBadge]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://djangoproject.com/
[RedisCloudBadge]: https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white
[RedisCloudUrl]: https://redislabs.com/redis-enterprise-cloud/
[CeleryBadge]: https://img.shields.io/badge/Celery-37814A?style=for-the-badge&logo=celery&logoColor=white
[Celery-url]: http://www.celeryproject.org/
[AllauthBadge]: https://img.shields.io/badge/Django%20Allauth-6D4F9D?style=for-the-badge&logo=django&logoColor=61DAFB
[Allauth-url]: https://django-allauth.readthedocs.io/en/latest/
[SBBadge]: https://img.shields.io/badge/Start%20Bootstrap-FFA500?style=for-the-badge&logo=start-bootstrap&logoColor=white
[SBUrl]: https://startbootstrap.com/
