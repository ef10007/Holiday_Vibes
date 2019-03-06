# Project plan

[Presentation Resource](https://docs.google.com/presentation/d/1AvII3M6TztcOlt1fVw902jkoczVbgYWZzz-IWcQg1-Y/edit?usp=sharing)

---
```1. Collecting data```

We have first looked for suitable websites and analysed the web structure and found API key. 
The data will be serviced on-premises to implement a great velocity and decrease memory usage.

----

```2. Organising template```

There will be a few rendering template by using Flask. 

* Layout
This html file will be declaring a default HTML/CSS structure that consists of Head, body( Navbar), Footer, Script( JQuery).

* Main 
It will display main page including search and recommendation section. 

* Login
We are going to emphasise the advantage of signing up such as users can personalise their preferences ( weather conditions, the range of ticket prices, create own holiday schedule, etc.). Once the user has logged in, session cookies will be set to maintain the session of the user.

* About us
A brief introduction of associated developers and basic motto of the project.

* Register 
It will provide a registration form and the loaded data will be sent to DB. Username will be email and password will be hashed before store. Signing up with social media(Facebook, Google, Github, etc.) is going to be also implemented.

* Calendar
* My page
* Search



----

```3. DataBase (MySQL)```

* User
* Preference
* Recommendation

----

```4. Back-end```

* Ajax

----

```5. Front-end```

* Graphic Visualisation

A fluctuation of ticket price will be graphed by using interactive plot. The plot is going to be updated every day by setting up cron-tab.

* JQuery

By using functions such as hover, on click, an interactive user interface/experience will be implemented with showing details on selected day. Navbar on the top and 'My list' on the bottom-left/ sticky(float),  will be having toggle function. 

* MDBootstrap

---
```6. Copyright Issue```

* Weather - using API
* Flight -  inform them via email

----

```7. Language (optional)```

* Vue.js - Internationalisation 
----

```8. The ultimate purpose of the project```

* Providing a platform that users can search and save the result and being led to the payment page.

