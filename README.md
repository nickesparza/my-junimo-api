# my-junimo-api

# Summary: 
Finally, an app that makes resource and crafting management easy in Stardew Valley! This app allows you to manage the inventory of your character(s) and easily see if your inventory meets the requirements for crafting items (and larger projects!) inside Stardew Valley.

# Link to Client Side
https://github.com/alysvolatile/my-Junimo-Client

# Team:
Nick Esparza, Alys Cooper

# External API/Seed Data Used
* Twitter API (<a href='https://developer.twitter.com/en/products/twitter-api'>here</a<>>) to link to recent tweets from Stardew Valley developer ConcernedApe.
* Seed Data taken from the <a href='https://stardewvalleywiki.com/'>Stardew Valley Wiki</a>.

# ERDs
<img src='./my-junimo-helper-erd.png' max-width='800px'/>

# MVP MODELS (listed in ERD as well)
* User (for player) - name, platform
* Characters (one to many from user to characters; 'saves') (fully crudable) (user can have many saves)
    - Name
    - Farm Type
    - Pet Type
    - Pet Name
    - Pet image (if cat, choose cat images; if dog, choose dog images - are there pigs too?)
    - Love Interest/Spouse
    - Horse Name
    - Inventory to hold MATERIALS, plural (foreign key, would this be many to many?) (many characters can have inventory), amount in inventory (an array of dictionaries, referencing FK of materials and a number of those materials currently in inventory)
    - Total G
    - Year
* Material
    - material name
    - description
    - image
    - sale price yr 1
    - sale price yr 2+
    - link to wiki page
* Crafting Recipes 
    - name
    - required material array(?)
    - processor needed (eg. forge, kiln)
* STRETCH GOAL - Construction projects from Robin 
    - name
    - cost
    - required material array
    - previous requirements (big coop requires coop)

### USER route table

| Verb   | URI Pattern            | Controller#Action |
|--------|------------------------|-------------------|
| POST   | `/sign-in`             | `users#signin`    |
| PATCH  | `/change-password/`    | `users#changepw`  |
| DELETE | `/sign-out/`           | `users#signout`   |

### CHARACTER route table

| Verb   | URI Pattern            | Controller#Action |
|--------|------------------------|-------------------|
| GET    | `/view-all-characters` | `characters#view-all`   |
| GET    | `/view-character`        | `characters#view`   |
| POST   | `/create-character`      | `characters#create`    |
| PATCH  | `/edit-character/`       | `characters#edit`  |
| DELETE | `/delete-character/`     | `characters#delete`   |

### MATERIAL route table

| Verb   | URI Pattern            | Controller#Action |
|--------|------------------------|-------------------|
| GET    | `/view-material`        | `materials#view`   |
| GET    | `/view-all-materials`        | `materials#view-all`   |

### CRAFTING RECIPE route table

| Verb   | URI Pattern            | Controller#Action |
|--------|------------------------|-------------------|
| GET    | `/view-crafting-recipes`        | `crafting-recipes#view`   |
| GET    | `/view-all-crafting-recipes`        | `crafting-recipes#view-all`   |

### CONSTRUCTION BLUEPRINT route table

| Verb   | URI Pattern            | Controller#Action |
|--------|------------------------|-------------------|
| GET    | `/view-blueprint`        | `blueprints#view`   |
| GET    | `/view-all-blueprints`        | `blueprints#view-all`   |

