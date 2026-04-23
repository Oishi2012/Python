def notes(amount):
    notes=[1000,500,200,100,50,20,10,5,2,1]

    for note in notes:
        count=amount//note
        print(note,'taka notes=',count)

        amount=amount%note
money=int((input("Enter Money")))
notes(money)
