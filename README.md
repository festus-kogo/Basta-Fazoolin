### Basta Fazoolin'

You’ve started a position as the lead programmer for the family-style Italian restaurant Basta Fazoolin’ with My Heart. The restaurant has been doing fantastically and seen a lot of growth lately. You’ve been hired to keep things organized.

### Making the Menus

**1.** At *Basta Fazoolin’ with my Heart* our motto is simple: when you’re here with family, that’s great! We have four different menus: brunch, early-bird, dinner, and kids.

Create a `Menu` class .

**2.** Give `Menu` a constructor with the five parameters `self`, `name`, `items`, `start_time`, and `end_time`.

3. Let’s create our first menu: `brunch`. Brunch is served from 11am to 4pm. The following items are sold during brunch:

```
{
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
```

**4.** Let’s create our second menu item `early_bird`. Early-bird Dinners are served from 3pm to 6pm. The following items are available during the early-bird menu:

```
{
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
```

**5.** Let’s create our third menu, `dinner`. Dinner is served from 5pm to 11pm. The following items are available for dinner:

```
{
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
```

**6.** And let’s create our last menu, `kids`. The kids menu is available from 11am until 9pm. The following items are available on the kids menu.

```
{
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
```

**7.** Give our `Menu` class a string representation method that will tell you the `name` of the menu. Also, indicate in this representation when the menu is available.

**8.** Try out our string representation. If you call `print(brunch)` it should print out something like the following:

**9.** Give `Menu` a method `.calculate_bill()` that has two parameters: `self`, and `purchased_items`, a list of the names of purchased items.

Have `calculate_bill` return the total price of a purchase consisting of all the items in `purchased_items`.

**10.** Test out `Menu.calculate_bill()`. We have a breakfast order for one order of pancakes, one order of home fries, and one coffee. Pass that into `brunch.calculate_bill()` and print out the price.

**11.** What about an early-bird purchase? Our last guests ordered the salumeria plate and the vegan mushroom ravioli. Calculate the bill with `.calculate_bill()`.

### Creating the Franchises


