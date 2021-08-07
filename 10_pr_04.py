class Train:

    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("******************************")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train is {self.seats}")
        print("******************************")

    def getFareInfo(self):
        print(f"The price of the ticket is Rs {self.fare}")

    def bookTicket(self):
        if self.seats >0:
            print(f"Your Seats have been booked!!The available seats are {self.seats}")
            self.seats = self.seats - 1
        else:
            print(f"Your ticket can't be booked seats are full!!")

    def cancelTicket(self,seatNo):
        pass
    


godan = Train("Godan Express : 17012",800,2)
godan.getFareInfo()
godan.bookTicket()
godan.bookTicket()
godan.bookTicket()
godan.getStatus()
