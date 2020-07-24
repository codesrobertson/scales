# Scales
A project to explore NLP semantic analysis and APIs. Scales provides an accessible, machine learning API and semantic analysis-based tool for determining the bias of a given article. Scales offers an incomprehensive diagnostic solution for the problem of uneven online media literacy in the United States. Presently, the project allows users to access a simple UI, enter a url to an article of their choosing, and be returned a summary of API and semantic analysis assessments and scores. Over time, the project will grow to include a user database, user data analytics, and hopefully, a sentence-by-sentence fact-checking feature. 

# Technologies 
The back-end of the stack includes:
* Python
* Flask
* Docker

The front-end of the stack includes:
* HTML
* CSS3
* Heroku

Other technologies in the project include:
* Machinebox external API (specifically, FakeBox)
* Python's Requests library
* TextBlob
* Beautiful Soup 4

# Running Scales

## Dependencies 

You'll need to have the following installed on your computer before you can run Scales locally:
* Python 3.8.3

If you don't have Python installed, follow the instructions at https://www.python.org/downloads/

If you already have Python installed, check to ensure it's the right version before continuing on: 
```

  $ python3 --version
  
 ```

* Pipenv
If you're using a Mac and Homebrew, install Pipenv: 
```

  $ brew install pipenv
 
```

If you're not on a Mac, try:
```

  $ pip install pipenv
  
 ```

Once you've installed Pipenv, install all Scales' bundled dependencies with:
```

   $ pipenv install --dev
   
```
   
## Quickstart
Now that you've installed all pre-requisite dependencies, you are ready to run the program locally. 

First, cd into the project's root directory. Then run the following in your terminal:
```

  $ pipenv run python3 app.py

```
  
 You should now be able to access the project from Localhost:5000 in your web browser. 


## Deployed Version

Don't want to go to the trouble of spinning up? You can check out the deployed version of the project on Heroku: https://dashboard.heroku.com/apps/scales-capstone/deploy/github . 


