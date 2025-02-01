# MAIS Hacks 2025 - Beginner backend workshop

Hello! I'm Josh Katofsky, 2022 McGill grad, and MAIS exec team alumni (fun fact: I made the hackathon website!). I'm currently working as a Full Stack Developer at Coveo (P.S. we're [hiring summer interns right now](https://www.coveo.com/en/company/careers/open-positions#t=career-search&numberOfResults=9&f:employmenttype=[Intern])).

This presentation will go over setting up a basic local web server that can be used to perform sentiment analysis on provided text.

It is aimed at *beginners*. And feel free to ask questions at any time!

## Prerequesites

- basic programming skills (ideally some familiarity with Python)
- your IDE or text editor of choice
- Python installed

## The workshop

### Setup

#### Create a virtual environment to encapsulate our project
  - Mac/Linux: `python3 -m venv venv/`
  - Windows: `py -m venv venv\`

#### Activate that virtual environment
  - Mac/Linux: `source venv/bin/activate`
  - Windows: `venv\Scripts\activate`

#### Create a requirements.txt
  - `nltk`: a library containing lots of tools for working with natural language
  - `fastapi`: an easy web server framework for Python (similar to Flask, if you've heard of it)

#### Install the packages
```bash
pip install -r requirements.txt
```

### Coding

#### Getting the sentiment of a text

- Instantiating a sentiment analyzer
- Writing a function to analyze text sentiment
- Running the function on user input

```bash
python app.py
```

Tip: if you get a certificate error on Mac when trying to download the `nltk` lexicon, find the python folder in your `Applications` folder, and run the `Install Certificates.command` script inside. ([reference](https://stackoverflow.com/a/42890688/6867216))

#### API Concepts

- Route/Resource/Endpoint
  - Some path that will be appended ot the URL of the server, corresponding to some functionality on the server

- JSON: **J**ava**S**cript **O**bject **N**otation
  - A data format; technically, the serialization of a JavaScript object, has become the standard format for sending data to/from routes

```json
{
  "someKey": "someValue",
  "anotherKey": 2025,
  "nestedObject": {
    "array": [1, 2, 3, 4]
  }
}
```

- HTTP verbs (AKA "request methods")
  - `GET` - retrieve a resource (e.g., `GET /resource`)
  - `DELETE` - delete a resource (`DELETE /resource`)
  - `PUT` - replace the resource (`PUT /resource`, with a request "body" specified in JSON)
  - `POST` - submit data to the server (`POST /some/route`, with a request "body" specified in JSON)
  - ...

*Which is the most suitable for our use case?*

#### Creating the API endpoint

Now, with this knowledge, and our sentiment-analyzing function, we can create a `POST` endpoint that returns the sentiment data for submitted text in JSON.

#### Testing

Once the code is ready, rather than running the file directly, we pass it to `fastapi`, where it recognizes the endpoint we defined, and serves the API locally on the port `8000`.

```bash
fastapi dev app.py
```

We can now send a web request to our server, and it will respond! (MacOS only; for Windows alternatives there are some good ideas [here](https://superuser.com/questions/362152/native-alternative-to-wget-in-windows-powershell?_gl=1*1rlea1n*_ga*MTQ1NjY3ODc5Ni4xNzM4Mzg1NDg2*_ga_S812YQPLT2*MTczODM4NTQ4Ni4xLjAuMTczODM4NTQ4Ni4wLjAuMA..)).

```bash
curl -H 'Content-Type: application/json' \
     -d '{ "text": "YOUR TEXT HERE"}' \
     -X POST http://127.0.0.1:8000/sentiment
```

### Next steps

#### Project ideas

You now have a python program that can communicate with the "outside world" using API endpoints. The world is your oyster!

- Train your *own* model and serve it using the server
- Persist data in your app using a database ([mongodb with pymongo](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/) is a good quick-and-dirty choice)
- ...

#### Deployment

I did not touch on deployment options here. At the moment, this server will only be accessible on your local machine. Hackathon pro-tip: that's fine!!! It's all about that demo ;)

Otherwise, so long as the machine it executes on is available to outside connections on the correct port, then tada, your app is deployed! This machine can be:

- yours! McGill wifi permitting, you can use [ngrok to serve a flaskapi app](https://github.com/ngrok/ngrok-python)
- a deploy-your-repo-directly solution such as [railway](https://railway.com/new)
- a more standard cloud offering such as AWS or GCP that requires manual deployments

The following command runs the "production" version of the server:

```bash
fastapi run app.py
```

No matter where you deploy your app, if you are going to be requesting the endpoint from a different domain than it is hosted on, you need to configure [CORS](https://fastapi.tiangolo.com/tutorial/cors/?h=cors)!

### Happy hacking!