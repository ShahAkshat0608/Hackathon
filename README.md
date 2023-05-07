# Hackathon
The code defines various routes that handle different HTTP requests. Here is a brief summary of what each route does:

The main() function renders the main.html template.

The loginpage() function renders the loginpage.html template.

The signup() function renders the signup.html template.

The login() function is called when the user tries to log in by submitting a form. It gets the username and password from the submitted form, queries the database to check if the user exists, and if the user is found in the database, it sets a session variable with the user ID and redirects to the home page. If the user is not found, it redirects to the loginpage with an error message.

The home() function renders the home.html template and displays the name of the user if the user is logged in. It retrieves the user ID from the session and queries the database to get the name of the user.

The insert() function is called when the user tries to sign up by submitting a form. It gets the user data from the submitted form, inserts it into the database, sets a session variable with the user ID, and redirects to the home page.

The get_matches() function is called when the user navigates to the matches page. It gets the user ID from the session, retrieves the list of liked users from the database, iterates through each user that the user has liked and checks if the user has been liked by that user as well. If there is a mutual like, it adds that user to the list of matches. It updates the matches column in the database with the list of matches and renders the matches.html template with the list of matches.

The showroommates() function is called when the user navigates to the browse page. It gets the user ID from the session, retrieves the list of liked and disliked users from the database, and gets the list of all users in the database. It then filters out the users that the current user has already liked or disliked, and renders the browse.html template with the filtered list of users.

The signup.html file contains an HTML document that serves as a sign-up page for a roommate-matching service. The page has a background gradient color, sticky navigation bar with a logo and links to Home, Matches, and Browse pages. The sign-up form is centered on the page and includes fields for the user's name, email, password, and a submit button. The page also includes a footer with links to the service's social media pages. Styling is achieved through CSS, including the use of imported fonts and a custom gradient animation. The page also includes a Font Awesome script for icon usage.
The login.html is HTML, CSS, and JavaScript code for a web page with a login form and a gradient background. It uses external libraries for font awesome icons and jQuery. The page consists of a navigation bar, a login form, and a footer. The form contains input fields for username and password and a submit button. The page also has a section for displaying user data in the form of name and age, contained in div elements with a specific class name and styling. The footer contains a link to the website owner's social media pages. The page is responsive and adjusts its layout based on screen size.

The main.html file is a web page written in HTML, CSS, and JavaScript. It is designed to display the main page of a roommate matching web application. The page has a sticky navigation bar with a logo, links to other pages, and buttons to log in or sign up. The background is a colorful gradient animation. The main body of the page displays an image, a subtext, and the buttons to log in or sign up. The footer of the page has a link to the website's terms and conditions.


The login.html is the HTML and CSS code for a login page with a gradient background. The page has a navigation bar at the top, which contains a logo and three navigation links.

The navigation bar is positioned as "sticky" using CSS and remains at the top of the screen even when the user scrolls down the page.

The login form is centered using CSS and has fields for entering a username and password. The form has a "submit" button that the user can click to submit their login information.

At the bottom of the page, there is a fixed footer with a link to a separate page.

The page uses Google Fonts and Font Awesome for styling.



The home.html file contains HTML, CSS, and JavaScript code for a webpage that serves as the home page of a website.

The page features a gradient background, a sticky navigation bar with a logo and links to other pages, a form for user input, and a footer with links to social media accounts.

The navigation bar has links to other pages of the website and a search bar. The form has fields for a username and password, and a submit button.

The CSS code in the file defines the layout and styling of the page, including the font family and size, the background color, and the positioning of various elements. The JavaScript code includes a script tag that imports the Font Awesome icon library.

Overall, home.html provides a visually appealing and functional home page for a website.


The browse.html file is an HTML document that presents a webpage with a navigation menu, a search form, and a footer. It includes external libraries and stylesheets, including jQuery and Font Awesome.

The header section contains metadata and links to external libraries and stylesheets. It includes a font awesome script, a jQuery library script, and a title for the page. Additionally, there is CSS styling for the background gradient, the navigation bar, and the search form.

The main content of the page is contained within the body tag. The body contains a navigation bar, a search form, and a container for the search results. The navigation bar contains a logo and links to other pages. The search form has a text input and a submit button, which allows users to search for items on the website. The search results are hidden in a container div with a class of "my-divs".

The footer contains links to other pages and is fixed to the bottom of the screen.

Overall, this file provides a basic template for a website with a navigation bar, a search feature, and a footer. The CSS styling and JavaScript functionality can be modified to suit the needs of a specific website.


The "matches.html" file contains the HTML, CSS, and JavaScript code for a webpage that displays the matches for a roommate-finding application called "Tinder for Roommates". The page has a navigation bar at the top with links to the home, matches, and browse pages. The body of the page contains a form for searching for matches. The footer at the bottom of the page contains a link to the "About Us" page. The page has a colorful gradient background, a bold logo, and uses the "Delicious Handrawn" and "Public Sans" fonts. The "fontawesome" library is also imported for displaying icons. The form is styled using CSS with rounded corners and box shadow. The page is responsive and has a sticky navigation bar.