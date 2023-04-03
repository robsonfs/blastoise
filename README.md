# Blastoise - Django + Vue App to scrape links from webpages

This project is made up of three parts
- **Backend Side:** A Django app on top of Django Rest Framework, responsible for all databases interaction to store, retrieve and update pages info.
- **Frontend Side:** A Vue app which allows users to submit pages to be scraped.
- **A Background Job:** Responsible for,  well, running the scrape requests in background. It uses a [python library](https://pypi.org/project/links-fetcher-robsonfs/) developed specifically for this project.


# Checklist
## Backend
- [x] Route for pages retrieve
- [x] Route for page update
- [x] Route for page detail
- [ ] Enqueue scrape tasks

## Frontend
- [x] Bootstrap Vue App
- [x] Connect to the frontend
- [ ] List Pages View
- [ ] Scrape form
- [ ] Page Detail View

## Background Job
- [x] Create a help library and upload it to the PyPi
- [ ] Bootstrap Celery
- [ ] Process the tasks


## Chroes
- [ ] Improve Docs
- [ ] Add automated tests
- [ ] Dockerize
