# AnarchyPedia
Bitcamp 2018 Hackathon Submission

## Inspiration
Everyone has, at some point, tried and failed to edit a Wikipedia article. There's a reason not just anyone can make changes - or else _anarchy_ would ensue, right? Well... _hmmm_ ....

## What it does
Anarchypedia allows users to anonymously view, edit and save Wikipedia articles.

## How I built it
Anarchypedia is a simple CRUD (or, rather, CRU) web app built with Django on the back end. When a user searches for a previously non-Anarchypedia-ed article, the article's original content is queried from the Wikipedia API in XML. The main body (not including subheaders) of the article is then extracted from the XML as raw HTML and saved into the database with other relevant metadata. The user is then presented with the article.
When editing an article, the user is manipulating the HTML saved from earlier (I would've liked to have the user edit in WikiCode or some other markup language, but then I'd end up [parsing HTML with regex](https://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags/1732454#1732454)).
 
## Challenges I ran into
* Matching Wikipedia's styling and fonts was a pain
* Deploying this app was a pain

## Accomplishments that I'm proud of
* Managed to finish minimum viable product by the end of night 1 and go Maryland sightseeing :)

## What I learned
* Parsing  XML with Python
* Django 2.0
* Deploying with PythonAnywhere

## What's next for Anarchypedia
What's next is a laundry list of polishing:
* Random anarchy-ed article link on sidebar
* Search bar on base template
* Match fonts and styling more closely
* Responsive design
* Fetch/Save full Wikipedia articles instead of only main content
* Full edit history tracking
