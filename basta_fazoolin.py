# 1
class Menu:
    # 2
    def __init__(self, menu_name, menu_items, start_time, end_time):
        self.menu_name = menu_name
        self.menu_items = menu_items
        self.start_time = start_time
        self.end_time = end_time
    
    def __repr__(self):
        return "{} menu available from {} to {}".format(self.menu_name, self.start_time, self.end_time)
    
    # 9
    def calculate_bill(self, purchased_items):
        sum_total = 0

        for purchased_item in purchased_items:
            # print(purchased_item)
            if purchased_item in self.menu_items:
            #    print("Add: " + str(self.menu_items[purchased_item]))
               sum_total += self.menu_items[purchased_item]

        return sum_total

#########################################################################################
# 3
# Brunch Menu
brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 
                'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 
                'orange juice': 3.50} 

brunch_menu = Menu("Brunch", brunch_items, 1100, 1600)
# 8
print(brunch_menu)# Brunch menu available from 1100 to 1600
print("Menu: " + brunch_menu.menu_name)# => Menu: Brunch
# print(brunch_menu.menu_items)

#########################################################################################
# 4
# Early Bird Menu
early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 
                    'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 
                    'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}

early_bird_menu = Menu("Early Bird", early_bird_items, 1500, 1800)
print(early_bird_menu)# Early Bird menu available from 1500 to 1800
print("Name: " + early_bird_menu.menu_name)# Name: Early Bird
# print(early_bird_menu.menu_items)

#########################################################################################

# 5 Dinner menu
dinner_items = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 
                'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 
                'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}

dinner_menu = Menu("Dinner", dinner_items, 1700, 2300)
print(dinner_menu)# Dinner menu available from 1700 to 2300
print("Name: " + dinner_menu.menu_name) # Dinner
# print(dinner_menu.menu_items)
#########################################################################################

# 6 Kids menu
kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 
              'apple juice': 3.00}

kids_menu = Menu("Kids", kids_items, 1100, 2100)
print(kids_menu) # Kids menu available from 1100 to 2100
print("Name: " + kids_menu.menu_name)
# print(kids_menu.menu_items)
#########################################################################################

# 10
brunch_order = {'pancakes': 7.50, 'home fries': 4.50, 'coffee': 1.50}
print(brunch_menu.calculate_bill(brunch_order)) # => 13.5

# 11
early_bird_order = {'salumeria plate': 8.00, 'mushroom ravioli (vegan)': 13.50}
print(early_bird_menu.calculate_bill(early_bird_order)) # => 21.5

# 12, 13, 14, 15
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus 
  
  def __repr__(self):
     return "{}".format(self.address)
  
  def available_menus(self, time):
     available_menu = []
     
     for menu in self.menus:
        print(menu)
        if time >= menu.start_time and time <= menu.end_time:
           available_menu.append(menu)

     return available_menu

# menu list
menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

flagship_store  = Franchise("1232 West End Road", menus)
print(flagship_store)# 1232 West End Road
print(flagship_store.available_menus(1700))# [Brunch menu available from 1100 to 1600, Kids menu available from 1100 to 2100]

new_installment  = Franchise("12 East Mulberry Street", menus)
print(new_installment)# 12 East Mulberry Street
print(new_installment.available_menus(1900))# [Brunch menu available from 1100 to 1600, Kids menu available from 1100 to 2100]


# 19
class Business:
   # 20
   def __init__(self, business_name, franchises):
      self.business_name = business_name
      self.franchises = franchises

franchises = [flagship_store, new_installment] # franchises list

basta = Business("Basta Fazoolin\' with my Heart", franchises)

arepas_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepas_menu = Menu("Take a’ Arepa", arepas_items, 1000, 2000)

arepas_menus =[arepas_menu] 

arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menus)

arepas = Business("Take a' Arepa", [arepas_place])
print(arepas.franchises[0])
print(arepas.franchises[0].menus[0])