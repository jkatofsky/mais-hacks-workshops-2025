# MAIS Hacks 2025 - Beginner frontend workshop

Hello! I'm Josh Katofsky, McGill grad in 2022, and MAIS Alumni from 2021-2022 (fun fact: I made the hackathon website!), currently working as a Full Stack Developer at Coveo (fun fact: we're [hiring summer interns right now](https://www.coveo.com/en/company/careers/open-positions#t=career-search&numberOfResults=9&f:employmenttype=[Intern])).

This will be a little HTML/JS crash course.

It is aimed at *beginners* to web dev. And feel free to ask questions at any time!

## Prerequesites

- basic programming skills
- your IDE or text editor of choice

**In this workshop, we will:**

1. Set up a basic webpage using HTML
2. Create a form on that page to capture user input
3. Make our page look pretty using a CSS library
4. Send the user input as an input to the text sentiment analyis API made in the previous backend workshop.

It's simple, but the idea is to give you tools to apply to your own projects!

## Workshop

### Setup

At the end of the day, `.html` files are simply text files, interpreted by the browser in a particular way. But, by convention, we name the HTML file for our website `index.html`, and fill it in with some boilerplate code.

We can add some content to the page within the `<body>`.

And take a look at our page by opening it in the browser.

### Adding input elements

We now add an:
- input textbox,
- button to request the analysis, and
- elements that will contain the returned analysis data


And we give them all unique `id`s that we will refer to later.

### Connecting the form to JavaScript

We then use JavaScript to save references to the input, button, and prediction elements, and temporarily log the text to the console to make sure everything is working.

Later, we will use the value of `text` when we call the API.

### Styling

But first, a little detour, because our site is looking pretty ugly at the moment. To keep the scope of this workshop reasonable, we won't be writing any CSS code directly. Instead, we will use a pre-made stylesheet. There are lots of options for this, and I'm personally a fan of [water.css](https://watercss.kognise.dev/). It doesn't require any changes to our HTML and automatically things will look pretty nice.

```html
...
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/water.css@2/out/dark.css">
...
```

Isn't that nicer?

### Calling the API

Since this workshop is **strictly about frontend**, we're using the API that was already made in the backend workshop (for those who followed that workshop, you will need CORS enabled). But we will still do a quick refresher of how it works at a high level.

#### The API format

The API endpoint is of the following format:

- The endpoint is `http://127.0.0.1:8000/sentiment` and accepts `POST` requests.
- It expects JSON bodies for those requests
- The request body is then be of the format `{"text": "i love my mom"}`
- The response will then look like `{"sentiment_description": "positive", "sentiment_score": 0.6369}`

#### The fetching code

We now make a function that uses the `fetch` API to asynchronously request the API.

## Hosting the frontend

I did not touch on deployment options here. At the moment, this server will only be accessible on your local machine. Hackathon pro-tip: that's fine!!! It's all about that demo ;)

Otherwise, it is quite easy to host a frontend with something like https://pages.github.com/. Just include your `index.html` in a repository and setup the Pages feature, and boom!