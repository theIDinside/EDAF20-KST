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

---

Recept för en given produkt måste finnas i databasen, där man ser namn på råvaran, dess mängd som krevs för receptet.

```
products(_id_, product)
ingredients(_id_, ingredient)
units(_id_, unit)
recipes(productId [FK], ingredientId [FK], quantity, unitId [FK])
```

##### PRODUCTS
| id  | product        |
|:---:|:---------------|
| 1   | Nut ring       |
| 2   | Nut cookie     |
| 3   | Amneris        |
| 4   | Tango          |
| 5   | Almond delight |
| 6   | Berlinger      |

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

##### UNITS
| id  | unit |
|:---:|:----:|
| 1   | g    |
| 2   | dl   |

##### RECIPES
| productId  | ingredientId | quantity | unitId |
|:----------:|:------------:|:--------:|:------:|
| 1          | 1            | 450      | 1      |
| 1          | 2            | 450      | 1      |
| 1          | 3            | 190      | 1      |
| 1          | 4            | 225      | 1      |
| 2          | 5            | 750      | 1      |
| 2          | 6            | 625      | 1      |
| 2          | 7            | 125      | 1      |
| 2          | 8            | 375      | 1      |
| 2          | 9            | 3.5      | 2      |
| 2          | 10           | 3.5      | 1      |
| 3          | 11           | 750      | 1      |
| 3          | 2            | 250      | 1      |
| 3          | 12           | 250      | 1      |
| 3          | 13           | 25       | 1      |
| 3          | 14           | 25       | 1      |
| 4          | 2            | 200      | 1      |
| 4          | 8            | 250      | 1      |
| 4          | 1            | 300      | 1      |
| 4          | 15           | 4        | 1      |
| 4          | 16           | 2        | 1      |
| 5          | 2            | 400      | 1      |
| 5          | 8            | 270      | 1      |
| 5          | 17           | 279      | 1      |
| 5          | 1            | 400      | 1      |
| 5          | 10           | 10       | 1      |
| 6          | 1            | 350      | 1      |
| 6          | 2            | 250      | 1      |
| 6          | 3            | 100      | 1      |
| 6          | 12           | 50       | 1      |
| 6          | 19           | 5        | 1      |
| 6          | 10           | 50       | 1      |
