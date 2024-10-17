class itemz:

    def __init__(self, name, price, qty):

        self.name = name

        self.price = price

        self.qty = qty

        self.category = "general"

        self.env_fee = 0

    def gettotal(self):

        return self.price * self.qty

    def gettmostprices(self):

        return self.price * self.qty * 0.6

# class to shop


class shoppincart:

    def __init__(self):

        self.items = []

        self.taxrate = 0.08

        self.memberdiscount = 0.05

        self.bigspenderdiscount = 10

        self.coupondiscount = 0.15

        self.currency = "USD"

    def additem(self, item):

        # discount added here

        self.items.append(item)

    def calculatesubtotal(self):

        # to do: fix this in the future i guess

        subtotal = 0

        for item in self.items:

            subtotal += item.getTotal()

        return subtotal

    def applydiscounts(self, subtotal, ismember):

        if ismember == "yes":

            subtotal = subtotal - (subtotal * self.memberdiscount)

        if subtotal > 100:

            subtotal = subtotal - self.bigspenderdiscount

        return subtotal

    def calculatetotal(self, ismember, hascoupon):

        # why i need this? @user

        subtotal = self.calculatesubtotal()

        subtotal = self.applydiscounts(subtotal, ismember)

        total = subtotal + (subtotal * self.taxrate)

        if hascoupon == "YES":

            total = total - (total * self.coupondiscount)

        return total


def main():

    cart = shoppincart()

    item1 = itemz("Apple", 1.5, 10)

    item2 = itemz("Banana", 0.5, 5)

    item3 = itemz("Laptop", "1000", 1)

    item3.category = "electronics"

    cart.additem(item1)

    cart.additem(item2)

    cart.additem(item3)

    ismember = True

    hascoupon = "YES"

    total = cart.calculateTotal(ismember, hascoupon)

    if total < 0:

        print("Error in calculation!")

    else:

        print("The total price is: $" + str(int(total)))


if __name__ == "__main__":

    main()
