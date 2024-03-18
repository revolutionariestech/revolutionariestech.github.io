## RevTech Website Project

Objective: create a professional-looking website to showcase our club

> Skills we might use... and will be helpful to know for your future classes:
- HTML/CSS
- Front-end web development
- Javascript/client-side functionality
- We _might_ use some SQL and database design to implement some features! TBD as of now
- Deploying a webpage to a public github page
- Waterfall software development

> Its important to start with the basics of HTML before getting into style. Here's a basic HTML template used for pretty much any website

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

> Introducing style...
CSS (Cascading Style Sheets) brings the HTML to life. It works through classes that can be applied to HTML tags

> `<div>` classes are the containers for CSS classes, and are super helpful to create layouts:
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

> Now do some research: <a href="https://www.w3schools.com/">w3schools</a> is a really good resource for HTML/CSS, and Javascript
