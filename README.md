## RevTech Website Project

**Please Skim through this short guide for info on HTML/CSS and Git!**

> Project Objective: create a professional-looking website to showcase our club

Skills we might use... and will be helpful to know for your future classes:
- HTML/CSS
- Front-end web development
- Javascript/client-side functionality
- We _might_ use some SQL and database design to implement some features! TBD as of now
- Deploying a webpage to a public github page using GitHub Pages
- Waterfall software development


## Getting Started

Have a look at the `index.html` file for examples on how to use the various HTML tags. For the first couple of weeks, this is what we hope you can accomplish in your delegated `.html` files.


**Testing your `.html` file:**
> To test your files easily without having to push to github, simply open a new browser tab, and press cntrl-o (control letter o), or File->Open File, or google how your system can open a file in a browser. Navigate to your `.html` file and open it, and it should be rendered in your browser tab. 


**Possible (optional) deliverables for next meeting, Monday 03/25:**
> Get started if you can, but its better to prioritize your classwork. 

As stated in the discord announcement, I am hoping to start with html basics this week. In the `website-project` thread on discord, vote for which of the 3 .html file you would like to work on:
- about_us.html
- projects.html
- socials.html

and you can get started on one of them if you have the time.

I am hoping to get the content of each page done (where you can design the page and implement any features as you see fit), using basic html tags. You can choose to do some basic CSS styling on your file, but please know that it may need to be changed or overriden when we develop an integrated style across the whole website later.

You can also push your work to github if you would like, but be careful because if you change some files other than the one that you're working on, it may unintentionally override someone elses work.

> Again, **no pressure** on getting anything done; if you haven't even started by Monday next week, that's ok too.
> DM @Amartya or @Ian N. if you have any questions.

## HTML/CSS Tips and Tricks

Its important to start with the basics of HTML before getting into style. Here's a basic HTML template used for pretty much any website

~~~
<!DOCTYPE html>
<html>
    <head>
        <!-- This sets the default displayed characters to UTF-8 -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>My Webpage</title>

        <!-- This links the style sheet (CSS), defined in a .css file -->
        <link rel="stylesheet" href="/static/style.css">
    </head>

    <body>
        <p>Hello, World!</p>
    </body>
</html>
~~~

_Introducing style..._

CSS (Cascading Style Sheets) brings the HTML to life. It works through classes that can be applied to HTML tags. `<div>` classes are the containers for CSS classes, and are super helpful to create layouts:
~~~
<div class="myClass">Hello, World!</div>
~~~

Then, in CSS, you can define `myClass` with style:
~~~
.myClass {
    color: black;
    font-size: 12pt;
}
~~~

> Now do some research! <a href="https://www.w3schools.com/">w3schools</a> is a really good resource for HTML/CSS, and Javascript. Researching how to do the syntax for a specific programming language is a really good skill to learn early, because your classes will not always tell you everything you need to know about a certain language. Knowing how to research syntax effieciently to get a job done will get you through a lot of tough team projects down the line.


## Committing and Pushing your Work:

To get your files on the public github repo, you need to first `stage` the files you want to add, `commit` the changes, then `push` them.

When you are ready to publish your work, use the commands in the terminal to stage:
~~~
git add <file_name>
~~~
You **must** be already in a git repo to use this command.

or, to add all files to the stage, do:
~~~
git add *
~~~

To check the status of the staged files, use:
~~~
git status
~~~
this is a quick way to check what files you are going to commit, to make sure you didn't miss any.

**ONLY** when you're ready to publish your work for certain, use:
~~~
git commit -m "add a commit message!"
~~~
It's really important to have descriptive commit messages, so others know what you are changing to the repo.

Now finally, to push your changes upstream, use:
~~~
git push
~~~

## Pulling Code from a Git Upstream

To pull existing code from the public online repo to your local storage, do the command:
~~~
git pull origin main
~~~
or simply
~~~
git pull
~~~

**Important Note about git pull:**
Make sure that your local directory doesn't have an newer version of the same file before git pulling, or the pull will fail (let's say, if you modified index.html, and then tried to pull an older version from github). If this happens, do either of these:
- First copy any changes you have made to the affected file, and save it somewhere safe (if you have the git VSCode extension, changes should be highlighted right in the IDE). Then, run the command `git reset --hard origin`. _This will wipe all changes on your local device, so make sure you have saved all your changes to somewhere safe beforehand. Trust me I learned the hard way..._ Then, do `git pull origin main` again.
- Ping @Amartya or @Ian N. on Discord so one of us to help resolve your merge conflict


## Any Questions??

DM @Amartya or @Ian N. on discord if you need any help.
