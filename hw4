import csv

class Customer:
    def __init__(self, custId, custName, addr, city, state, zipcode): #This is a pretty standard init for the customer class, containing address, city, state, monthly spending, and a new attribute I added.
        self.custId = custId
        self.custName = custName
        self.addr = addr
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.memberLevel = BasicMember()
        self.monthlySpending = 0
        self.storesVisited = {}
        #I created the storesVisited attribute to track the customer's purchases at each store because
        #I thought it was valuable information from which I could find the store at which they shopped the most.
        #It will also tell us how many stores they shopped at and how much they spent at each once, which would be useful to a retailer.
    def changeLevel(self, level):
       """This method changes the membership level to gold or silver."""
       if level == 'gold':
           self.memberLevel = GoldMember()
       elif level == 'silver':
           self.memberLevel = SilverMember()
       else:
           self.memberLevel = BasicMember()

    def getDiscount(self):
        """This method return the discount amount for each customer."""
        return self.memberLevel.updateDiscount()

    def __updateSpending__(self, amount): #I made this method internal as I figured that users of these classes would not need the ability to adjust how the monthly spending is updated.
        """This method is an internal function that updates the amont of spending for each customer."""
        self.monthlySpending += amount

    def __updateFavoriteStore__(self, storeId, amount): #Similarily to the method above, I made this internal to the class as there is no need for the user of this class to be able to call or use this method.
        """This method is an internal function that creates a dict that shows the stores at which each customer has made purchases and the total amount."""
        if storeId in self.storesVisited.keys():
            self.storesVisited[storeId] += int(amount)
        else:
            self.storesVisited[storeId] = int(amount)

    def custInfoUpdate(self, storeId, amount):
        """This is the main method for updating customer information in the class."""
        self.__updateFavoriteStore__(storeId, amount)
        self.__updateSpending__(amount)

    def getFavoriteStore(self):
        """This method returns the store at which the customer has spent the most."""
        faveStore = sorted(self.storesVisited, key=self.storesVisited.get, reverse=True)
        return faveStore[0]

class BasicMember: #This class is the class for basic membership and returns the discount amount.
  def updateDiscount(self):
    return 0

class GoldMember(BasicMember): #This class is the class for gold membership and returns the discount amount.
  def updateDiscount(self):
    return 15

class SilverMember(BasicMember): #This class is the class for silver membership and returns the discount amount.
  def updateDiscount(self):
    return 5

class Store:
    def __init__(self, storeNum, storeAddr, storeCity, storeState, storeZipcode, storeMan):
        self.storeNum = storeNum
        self.storeAddr = storeAddr
        self.storeCity = storeCity
        self.storeState = storeState
        self.storeZipcode = storeZipcode
        self.storeMan = storeMan

    def getStoreMan(self):
        """This method returns the store manager."""
        return self.storeMan
def main():
    customers = [] #Create a list to store the instances of the customers.
    stores = [] #Create a list to store the instances of the stores.

    with open('customers.dat', 'r') as custfile: #Iterate through the list of customers. I used the csv module and gave each column its own name because it was easier to debug and align to the variables in the customer class than simply using the split method on each string.
        reader = csv.DictReader(custfile, fieldnames=['customer ID', 'name', 'address', 'city', 'state', 'zip code'])
        for row in reader:
            row['customer ID'] = Customer(row['customer ID'], row['name'], row['address'], row['city'], row['state'], row['zip code'])
            customers.append(row['customer ID'])

    with open('stores.dat', 'r') as storefile: #Iterate through the list of stores. I also used the same csv module here for the reasons I mentioned above: the split method is not easy to debug if your variables are misaligned.
        reader = csv.DictReader(storefile, fieldnames=['store number', 'store manager', 'address', 'city', 'state', 'zip code'])
        for row in reader:
            row['store number'] = Store(row['store number'], row['address'], row['city'], row['state'], row['zip code'], row['store manager'])
            stores.append(row['store number'])

    with open('transactions.dat', 'r') as transfile: #Iteratre through the list of stores using the csv module.
        reader = csv.DictReader(transfile, fieldnames=['transaction ID', 'transaction date', 'customer ID', 'store number', 'transaction amount'])
        for row in reader:
            cust = row['customer ID'] #Assign the customer ID to a variable so we can search through the list of customer instances.
            for item in customers:
                if cust in item.custId: #If the customer ID from the transactions is found in the customer instances, then update the customer information, which internally inside of the instance, updates both the montly spending and favorite stores.
                    item.custInfoUpdate(row['store number'], float(row['transaction amount']))

    for item in customers: #Iterate through the list of customers and change the level depending on their montly spending. I decided to leave this outside of the classes in case there was ever a decision to change the levels based on the amount spent.
        if item.monthlySpending >= 1200:
            item.changeLevel('gold')
            continue
        if item.monthlySpending >= 800:
            item.changeLevel('silver')
            continue

    with open('Final_Data.csv', 'w') as finaldatafile: #Create a new csv file using the csv module with the appropriate column headers.
        writer = csv.DictWriter(finaldatafile, fieldnames=['Customer Name', 'Address', 'City', 'State', 'Zip Code', 'Discount Amount', 'Favorite Store Manager'])
        writer.writeheader()
        for item in customers: #iterate through the customers and assign their discount level to a variable.
            discount = item.getDiscount()
            if discount == 0: continue #If the discount level is 0, we can ignore the customer since they're not getting a discount.
            fstore = item.getFavoriteStore() #Call the method to determine the store at which the customer has spent the most money and assign it to a variable.
            for store in stores: #Iterate through the list of stores and find the customer's favorite store.
                if fstore == store.storeNum: #Once we find the favorite store, write all of the customer information to the csv, including the store manager of that store, which is found through the store's class method.
                    writer.writerow({'Customer Name': item.custName,'Address':item.addr, 'City': item.city, 'State':item.state, 'Zip Code': item.zipcode, 'Discount Amount': item.getDiscount(), 'Favorite Store Manager':store.getStoreMan()})

if __name__ == '__main__':
    main()
