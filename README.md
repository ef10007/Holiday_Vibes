# Project plan and daily note

[Presentation Resource - Strategy](https://docs.google.com/presentation/d/1AvII3M6TztcOlt1fVw902jkoczVbgYWZzz-IWcQg1-Y/edit?usp=sharing)

---
```1. Collecting data```

We first looked for suitable websites and analysed the web structure. 
The data will be serviced on-premises to implement a high velocity and decrease memory usage.

----

```2. Organising HTML file```

There will be a few rendering templates by using Flask. 

* Layout
This HTML file will be declaring a default HTML/CSS structure that consists of Head, body( Navbar), Footer, Script( JQuery).

* Main 
It will display the main page including search and recommendation section. 

* Login
We are going to emphasise the advantage of signing up such as users can personalise their preferences ( weather conditions, the range of ticket prices, create their holiday schedule, etc.). Once the user has logged in, session cookies will be set to maintain the session of the user.

* About us
A brief introduction of associated developers and the basic motto of the project.

* Register 
It will provide a registration form, and the loaded data will be sent to DB. The username will be email and password will be hashed before the store. Signing up with social media(Facebook, Google, Github, etc.) is going to be also implemented.

* Calendar

We will display the calendar each month as a default value that also the user can select a specific period.
 Each cell of it has anchor tag leads to the search HTML displaying related information.

* My page

The users can pick their journey and store them in a list. 

* Search

The input data will be split by space( .split(' ') ) and filtered with if/else phrases. Or perhaps we will be using text mining.

----

```3. DataBase (MySQL)```

* User (email, passwd, username( default value is email address), region( nullable)..) # password store by using MDA256, password function

* Preference (temperature, country, the purpose of holidays, price range)

* Recommendation - ML, CRM(Customer-relationship management)

----

```4. Network communication (Server side) ```

* Ajax( Asynchronous JavaScript And XML )

Each data on the graph(calendar) that hovered/clicked by the user will be displayed, and by using ajax and D3.js, we will implement this. 


* Flask with python

Regarding the capacity of the server issue, we are going to use GCP(Google Cloud Platform) to remove the presence of servers that require redundant power supplies. By using a macro, we are going to simplify the python code.
(8th.Mar.2019: Creating GCP accoun for SQL)

----

```5. Client-side```

* Graphics Visualisation

A fluctuation of the ticket price will be graphed by using the interactive plot(D3.js). The plot is going to be updated every day by setting up a crontab.

* JQuery

By using functions such as hover, on click, an interactive user interface/experience will be implemented by showing details on the selected day. Navbar on the top and 'My list' on the bottom-left/ sticky(float), will be having toggle function. 

* MDBootstrap

MDB supports basic template that we will develop the webpage from.  

(7th.Mar.2019 : We have downloaded two zip files from [fullcalendar](https://fullcalendar.io/), calendar and full calendar folder and we first encountered **werkzeug.routing.BuildError** as the folders have not been moved to the static folder that Flask automatically adds a static view that takes a path relative to the flask/static directory and serves it.  
This endpoint error has been resolved by directing the right path of each static file.)

---
```6. Copyright Issue- Risk point```

* Weather - using API
#flask module 

* Flight -  inform them via email 

(8th.Mar.2019 : The 'country_code' list is going to be saved as 'city_code'. We narrowed the range of city choices that are from each continent - Asia, Africa, North America, South America, Europe and Australia.)

----

```7. Language (optional)```

* Vue.js - Internationalisation 
----

```8. The ultimate purpose of the project```

