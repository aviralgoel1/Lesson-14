def hotel_cost(nights):
    return 140*nights


def plane_ride_cost(city):
    if city == "Dallas":
        return 500
    elif city == "New York":
        return 350
    elif city == "Miami":
        return 450
    elif city == "LA":
        return 600
    elif city == "Las Vegas":
        return 550

def rental_car_cost(days):
    if days>=7:
        return 40*days-50
    elif days>=3:
        return 40*days-20
    else:
        return 40*days


cardays=int(input("number of days for car rental "))
print ("car rental cost:", rental_car_cost(cardays))
city=input(("which city? dallas, new york, miami, LA, las vegas: "))
print ("flight cost: ",plane_ride_cost(city))
hotel= int(input("Nights in hotel? "))
print("hotel cost ",hotel_cost(hotel))
spending_money=int(input ("spending money: "))

def trip_cost (city, cardays, hotel, spending_money):
    return rental_car_cost(cardays)+hotel_cost(hotel)+plane_ride_cost(city)+spending_money

print("total trip cost: ", trip_cost (city, cardays, hotel, spending_money))