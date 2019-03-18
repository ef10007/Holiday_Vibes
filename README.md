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
(10.Mar.2019: Skyscanner Widget has been loaded on the right-top card.)

* Login
We are going to emphasise the advantage of signing up such as users can personalise their preferences ( weather conditions, the range of ticket prices, create their holiday schedule, etc.). Once the user has logged in, session cookies will be set to maintain the session of the user.

* About us
A brief introduction of associated developers and the basic motto of the project.

* Register 
It will provide a registration form, and the loaded data will be sent to DB. The username will be email and password will be hashed before the store. Signing up with social media(Facebook, Google, Github, etc.) is going to be also implemented.

* Calendar

We will display the calendar each month as a default value that also the user can select a specific period.
Each cell of it has anchor tag leads to the search HTML displaying related information.

(8th.Mar.2019 : script tag isn't working.)

* My page

The users can pick their journey and store them in a list. 

* Search

The input data will be split by space( .split(' ') ) and filtered with if/else phrases. Or perhaps we will be using text mining.

----

```3. DataBase (MySQL)```

(11th.Mar.2019: Organise Tables and Columns. The ticket table added as a few information will be stored for producing graphs.)

* User (id(Integer),
        email(String),
        passwd(String), 
        username( default value is email address),
        fblog(String)
        ) - password store by using MDA256, password function

* Country (id(Integer), 
           countrycd(String),
           countryname(String)
           )
           
* Airport (countrycode(String), 
           cityname(String),
           airportcode(String)
           )

* Preference (uid(Integer),
              temperature(Integer), 
              city(String), 
              purpose(String),
              price range(Integer))

* Ticket (cityname(String), + option
          date(String),
          price(Integer),
          crondt(String)) - Direct Flights Only
          
* Weather (cityname(String),
           date(String),
           mintemp(Integer),
           maxtemp(Integer),
           main(Integer),
           crondt(String)) # The Unix epoch is the time 00:00:00 UTC on 1 January 1970.
      

* Recommendation - ML, CRM(Customer-relationship management) sending email feature will be added

(8th.Mar.2019: Planning of creating GCP account for SQL)

(14th.Mar.2019: We created another GCP account for SQL and successfully connected with MySQLWorkbench. We created table 'Airport' and inserted values straight from the URL. The connection details such as username and password have been exported in bash profile so that we can import them using os module. )

(18th.Mar.2019: We created table 'Country' and inserted values from JSON file.)

----

```4. Network communication (Server side) ```

* Ajax( Asynchronous JavaScript And XML )

Each data on the graph(calendar) that hovered/clicked by the user will be displayed, and by using ajax and D3.js, we will implement this. 


* Flask with python

Regarding the capacity of the server issue, we are going to use GCP(Google Cloud Platform) to remove the presence of servers that require redundant power supplies. By using a macro, we are going to simplify the python code.

----

```5. Client-side```

* Graphics Visualisation

A fluctuation of the ticket price will be graphed by using the interactive plot(D3.js). The plot is going to be updated every day by setting up a crontab.

* JQuery

By using functions such as hover, on click, an interactive user interface/experience will be implemented by showing details on the selected day. Navbar on the top and 'My list' on the bottom-left/ sticky(float), will be having toggle function. 
(17th.Mar.2019: Also will consider to use 'Handlebars' and Vue.js)

* MDBootstrap

MDB supports basic template that we will develop the webpage from.  

(7th.Mar.2019 : We have downloaded two zip files from [fullcalendar](https://fullcalendar.io/), calendar and full calendar folder and we first encountered **werkzeug.routing.BuildError** as the folders have not been moved to the static folder that Flask automatically adds a static view that takes a path relative to the flask/static directory and serves it.  
This endpoint error has been resolved by directing the right path of each static file.)

(11th.Mar.2019: We will no longer use the calendar template as it has a limited feature that cannot fully accomplish what we are going to display. Hence, with a bit of study, we are going to create our own calendar page. )

---
```6. Copyright Issue- Risk point```

* Weather - using API
 making it as a single module 
 
 (13.Mar.2019: We got an API key from [openweather.org](https://openweathermap.org) and requested weather information with city ID which can be found on the website as a JSON file. As a result, from what we have received, we figured out that the temperature is in K(Kelvin) so we have to subtract its value(273.15) to get it in Celcius.  We are going to store them as raw data for now and process the temperature value in server side before sending it to the screen. )
 ```
 sample data = 
 {'clouds': {'all': 88},
 'dt': 1552510800,
 'dt_txt': '2019-03-13 21:00:00',
 'main': {'grnd_level': 1008.37,
          'humidity': 97,
          'pressure': 1014.49,
          'sea_level': 1014.49,
          'temp': 294.774,
          'temp_kf': 0,
          'temp_max': 294.774,
          'temp_min': 294.774},
 'rain': {'3h': 0.345},
 'sys': {'pod': 'd'},
 'weather': [{'description': 'light rain',
              'icon': '10d',
              'id': 500,
              'main': 'Rain'}],
 'wind': {'deg': 61.5019, 'speed': 2.38}})
 ```

* Flight -  inform them via email 

(8th.Mar.2019 : PLAN - The 'city_code' list is going to be saved as JSON (key=city name, value= city code). Selenium is going to automatically collect the city codes.)

(10.Mar.2019 : The site has blocked my IP. Affiliate section found instead. Going to select a few cities have distinctive temperature and distances.)

(12.Mar.2019 : The country codes have been successfully saved as a JSON file.  However, attempting to get the city codes failed and we received dictionary = {['Redirect-to']: some code,  ['Reason']: blocked} instead. We have realised that we were disobeying the 'Market principle' as the ticket website is currently on service showing ticket prices depending on the city name. We altered the plan that we will use IATA (International Air Transport Association) code and generate dummy data that has been engineered to be realistic. The IATA codes have been collected from [flightsfrom](https://www.flightsfrom.com/) and saved as a JSON file.)

----

```7. Language (optional)```

* Vue.js - Internationalisation 
----

```8. The ultimate purpose of the project```

