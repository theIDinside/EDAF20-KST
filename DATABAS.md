## Databas

Alla som lägger beställning måste vara registerade i databasen.
```
customers(_id_, customer, address, country)
```

##### CUSTOMERS
| id  | customer      | address      | country |
|:---:|:--------------|:-------------|:-------:|
| 1   | Finkakor AB   | Helsingborg  | SE      |
| 2   | Småbröd AB    | Malmö        | SE      |
| 3   | Kaffebröd AB  | Landskrona   | SE      |
| 4   | Bjudkakor AB  | Ystad        | SE      |
| 5   | Kalaskakor AB | Trelleborg   | SE      |
| 6   | Partykakor AB | Kristianstad | SE      |
| 7   | Gästkakor AB  | Hässleholm   | SE      |
| 8   | Skånekakor AB | Perstorp     | SE      |

Kolumnen **id** är *AUTO_INCREMENT* och motsvarar kundens **kundnummer**.

```
CREATE TABLE customers
(
    id INTEGER PRIMARY KEY,
    customer TEXT NOT NULL,
    address TEXT NOT NULL,
    country TEXT(2) NOT NULL
);
CREATE UNIQUE INDEX customers_customer_uindex ON customers (customer);
INSERT INTO "customers" (customer,address,country) VALUES
("Finkakor AB","Helsingborg","SE"),
("Småbröd AB","Malmö","SE"),
("Kaffebröd AB","Landskrona","SE"),
("Bjudkakor AB","Ystad","SE"),
("Kalaskakor AB","Trelleborg","SE"),
("Partykakor AB","Kristianstad","SE"),
("Gästkakor AB","Hässleholm","SE"),
("Skånekakor AB","Perstorp","SE");
```

---

Recept för en given produkt måste finnas i databasen, där man ser namn på råvaran, dess mängd som krevs för receptet.

```
products(_id_, product)
ingredients(_id_, ingredient)
units(_unit_, name)
recipes(productId [FK], ingredientId [FK], quantity, unit [FK])
```

 * **products.id** Unikt artikel-/produktnummer
 * **ingredients.id** Unikt råvaroidentifieringsnummer


##### PRODUCTS
| id  | product        |
|:---:|:---------------|
| 1   | Nut ring       |
| 2   | Nut cookie     |
| 3   | Amneris        |
| 4   | Tango          |
| 5   | Almond delight |
| 6   | Berlinger      |

```
CREATE TABLE products
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT NOT NULL
);
CREATE UNIQUE INDEX products_product_uindex ON products (product)
INSERT INTO "products" (product) VALUES
("Nut ring"),("Nut cookie"),("Amneris"),
("Tango"),("Almond delight"),("Berlinger");
```

##### INGREDIENTS
| id  | ingredient            |
|:---:|:----------------------|
| 1   | Flour                 |
| 2   | Butter                |
| 3   | Icing sugar           |
| 4   | Roasted, chopped nuts |
| 5   | Fine-ground nuts      |
| 6   | Ground, roasted nuts  |
| 7   | Bread crumbs          |
| 8   | Sugar                 |
| 9   | Egg whites            |
| 10  | Chocolate             |
| 11  | Marzipan              |
| 12  | Eggs                  |
| 13  | Potato starch         |
| 14  | Wheat flour           |
| 15  | Sodium bicarbonate    |
| 16  | Vanilla               |
| 17  | Chopped almonds       |
| 18  | Cinnamon              |
| 19  | Vanilla sugar         |

```
CREATE TABLE ingredients
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient TEXT NOT NULL
);
CREATE UNIQUE INDEX ingredients_ingredient_uindex ON ingredients (ingredient);
INSERT INTO "ingredients" (ingredient) VALUES
("Flour"),("Butter"),("Icing sugar"),("Roasted, chopped nuts"),
("Fine-ground nuts"),("Ground, roasted nuts"),("Bread crumbs"),
("Sugar"),("Egg whites"),("Chocolate"),("Marzipan"),("Eggs"),
("Potato starch"),("Wheat flour"),("Sodium bicarbonate"),
("Vanilla"),("Chopped almonds"),("Cinnamon"),("Vanilla sugar");
```

##### UNITS
| unit  | name       |
|:-----:|:-----------|
| kg    | kilogram   |
| hg    | hectogram  |
| dag   | decagram   |
| g     | gram       |
| dg    | decigram   |
| cg    | centigram  |
| mg    | milligram  |
| kL    | kiloliter  |
| hL    | hectoliter |
| daL   | decaliter  |
| L     | liter      |
| dL    | deciliter  |
| cL    | centiliter |
| mL    | milliliter |

```
CREATE TABLE units
(
    unit TEXT PRIMARY KEY NOT NULL,
    name TEXT NOT NULL
);
CREATE UNIQUE INDEX units_name_uindex ON units (name);
INSERT INTO "units" (unit, name) VALUES
("kg","kilogram"),("hg","hectogram"),("dag","decagram"),
("g","gram"),("dg","decigram"),("cg","centigram"),
("mg","milligram"),("kL","kiloliter"),("hL","hectoliter"),
("daL","decaliter"),("L","liter"),("dL","deciliter"),
("cL","centiliter"),("mL","milliliter");
```

##### RECIPES
| productId  | ingredientId | quantity | unit |
|:----------:|:------------:|:--------:|:----:|
| 1          | 1            | 450      | g    |
| 1          | 2            | 450      | g    |
| 1          | 3            | 190      | g    |
| 1          | 4            | 225      | g    |
| 2          | 5            | 750      | g    |
| 2          | 6            | 625      | g    |
| 2          | 7            | 125      | g    |
| 2          | 8            | 375      | g    |
| 2          | 9            | 3.5      | dL   |
| 2          | 10           | 50       | g    |
| 3          | 11           | 750      | g    |
| 3          | 2            | 250      | g    |
| 3          | 12           | 250      | g    |
| 3          | 13           | 25       | g    |
| 3          | 14           | 25       | g    |
| 4          | 2            | 200      | g    |
| 4          | 8            | 250      | g    |
| 4          | 1            | 300      | g    |
| 4          | 15           | 4        | g    |
| 4          | 16           | 2        | g    |
| 5          | 2            | 400      | g    |
| 5          | 8            | 270      | g    |
| 5          | 17           | 279      | g    |
| 5          | 1            | 400      | g    |
| 5          | 10           | 10       | g    |
| 6          | 1            | 350      | g    |
| 6          | 2            | 250      | g    |
| 6          | 3            | 100      | g    |
| 6          | 12           | 50       | g    |
| 6          | 19           | 5        | g    |
| 6          | 10           | 50       | g    |

```
CREATE TABLE recipes
(
    productId INTEGER NOT NULL,
    ingredientId INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit INTEGER NOT NULL,
    CONSTRAINT recipes_products_id_fk FOREIGN KEY (productId) REFERENCES products (id),
    CONSTRAINT recipes_ingredients_id_fk FOREIGN KEY (ingredientId) REFERENCES ingredients (id),
    CONSTRAINT recipes_units_unit_fk FOREIGN KEY (unit) REFERENCES units (unit)
);
INSERT INTO "recipes" (productId, ingredientId, quantity, unit) VALUES
("1","1","450","g"),("1","2","450","g"),("1","3","190","g"),("1","4","225","g"),
("2","5","750","g"),("2","6","625","g"),("2","7","125","g"),("2","8","375","g"),
("2","9","3,5","g"),("2","10","50","g"),("3","11","750","g"),("3","2","250","g"),
("3","12","250","g"),("3","13","25","g"),("3","14","25","g"),("4","2","200","g"),
("4","8","250","g"),("4","1","300","g"),("4","15","4","g"),("4","16","2","g"),
("5","2","400","g"),("5","8","270","g"),("5","17","279","g"),("5","1","400","g"),
("5","10","10","g"),("6","1","350","g"),("6","2","250","g"),("6","3","100","g"),
("6","12","50","g"),("6","19","5","g"),("6","10","50","g");
```
