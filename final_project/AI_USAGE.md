# Final Project

## What did I ask
[Q1: I had inputted the guidelines for the Final Project and asked AI to summarize in depth what the project asked for?

Q2: Does my project strucuture match what the Professor wants for this project?

Q3: Will this application deploy to Render?

Q4: It says import "flask" could not be resolved in my terminal. Can you explain why this is happening?

Q5: Although the API key is not working right now, can I deploy to Render still so my application works?
]

## What did AI generate?
[A1: Final Project Overview

This is your capstone project and is worth 25% of your course grade.

You need to build something meaningful in Python—something you could realistically put in a portfolio. Unlike the mini-projects, you choose:

what problem to solve
how to solve it
how ambitious to make it

Using AI tools like ChatGPT, Anthropic’s Claude, or GitHub Copilot is encouraged, but you’re responsible for decisions and understanding the work.

Important Dates
Proposal due: 4/17
Submit proposal.md in your GitHub repo
Gallery Walk (demo day): 4/28
Present your project in class
Peer review due: 4/30
Review 2 classmates’ repos using GitHub Issues
Final submission: 5/1
Final code + README + AI_USAGE.md complete

Proposal (proposal.md)

Short and focused—include:

What are you building?
Why are you building it?
MVP (minimum version) vs stretch goals
What don’t you know yet?
APIs?
libraries?
concepts?

Required For Final Submission

Your repo must include:

✅ Working Python application
✅ Solves a real problem / useful purpose
✅ README.md explaining:

what it does
how to run it
setup/API keys

✅ AI_USAGE.md explaining how you used AI

✅ Regular commits over time (not one giant last-minute upload)

✅ No secrets committed (use .env + .gitignore)

AI Usage Requirement (important)

You must document significant AI use in AI_USAGE.md.

For each use, record:

What you asked
What AI generated
What you did with it
What you learned

Example:

Prompt:

“Help me build a Flask login system”

AI generated:
boilerplate Flask code

What you did:
modified authentication flow, added validation

What you learned:
how Flask routes / sessions work

This documentation is part of your grade.

Peer Review (10% of project grade)

Review 2 classmates’ projects on GitHub and open Issues with:

Is README clear?
Can project run?
Is code readable?
Does it work?
Is AI_USAGE meaningful?
One thing impressive
One specific suggestion

Feedback needs to be specific, not “nice project.”

What Your Professor Actually Cares About Most

Not “how fancy” it is.

What matters:

Did you understand what you built?
Did you grow as a programmer?

A simple project you deeply understand > a complicated project you can’t explain.

A2: Yes — the structure mostly matches what your professor wants.

You currently have: app.py, requirements.txt, templates, static.

That is good for a Flask app, but for the final project you should add the required assignment files:
app.py, README.md, proposal.md, AI_USAGE.md, requirements.txt, .gitignore, templates, static.

The missing pieces to make it fully assignment-ready are:
README.md
Explain what the app does, how to install it, and how to run it.
proposal.md
Put your final proposal there.
AI_USAGE.md
Document how you used ChatGPT.
No API keys or secrets
Since the MVP has no APIs yet, you are safe.
So yes: the app structure is correct, but add the documentation files before submission.

A3: Yes — this app will deploy cleanly to Render with very minor changes.

Right now you’re running:
if __name__ = "__main__":
    app.run(debug=True)

That works locally, but for Render we should make it production-ready.

1) Update app.py
Replace the bottom of your file with:
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

2) Update requirements.txt
Put: Flask and gunicorn

3) Add render.yaml

4) Push to Github

5) Deploy on Render
On Render:
New +
Web Service
Connect GitHub repo
Deploy
Then you get a working website.

My recommendation:

Build MVP locally first → test → deploy to Render → then add stretch goals.

A4: That means your code editor (probably Visual Studio Code) cannot find the Flask package in your Python environment.

Your code is fine — Flask just isn’t installed in the interpreter VS Code is using.

Open terminal inside helloflask/ and run: pip install lask or python -m pip install flask

You should see: Successfully installed flask ...

Then verify by running: python -c "import flask; print(flask.__version__)"

You should get a version number.

A5: Yes — you can deploy now, and I actually recommend doing it now.

Your core app works without weather because your code probably already handles API failure gracefully.

Deploy checklist - Your project root should look like:
app.py, requirements.txt, render.yaml, .gitignore, .env, templates, static

1) .gitignore
Make sure:
.env
venv/
__pycache__/
*.pyc
This keeps your API key off GitHub.

2) requirements.txt
Make sure: 
Flask, gunicorn, requests, python-dotenv

3) render.yaml
services:
  - type: web
    name: makemytrip
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app

4) Push to GitHub

5) Deploy on Render
New Web Service
Connect GitHub repo
Render auto-detects render.yaml
Deploy

6) Add environment variable in Render
Dashboard → Environment → Add: WEATHER_API_KEY = your_key
Even if it still isn’t active, set it now.

Once OpenWeather activates it, your deployed site should begin showing weather automatically without code changes.

After this: deploy!
]

## What did I do with it?
[For this project, I used Chat GPT to help me outline my files, understand how to properly deploy and use Flask, APIs, and customize my project to ensure that it was unique and matched what was asked for by the Professor. During this time, I tried my best to keep my main ambitions that this project will deploy successfully. Initially, I was having some issues with deploying on Render because I was not putting in the right information. AI helped me deploy this application successfully and enabled me on some clarity on APIs. Even if my API key isn't working now since I created a new one for authentication, it will work in a few hours due to the API key being added to this project and being enabled.]

## What have I learned?
[Throughout my time in this course and composition of the final project, I learned how to turn an idea into a working product. Using AI was a helpful tool in the completion of my learning and project completion because it helped me understand where my errors were, helped me learn more about the web, technology, and APIs, and enabled me to continously learn from my mistakes. AI is not a completor, it is an essential tool for cross referencing the work I have been doing. Furthermore, I have also been fond of the importance that static and template folders have when deploying a web application. These are serious metrics to ensure your app is easy to use and user-friendly. App.py is an essential aspect of ensuring your application runs smoothly for the public.]