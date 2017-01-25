cars = 100
#number of cars, defining variable
space_in_a_car = 4.0
# space in the car defined as 4 spaces
drivers = 30
# drivers total number
passengers = 90
# passengers total number
cars_not_driven = cars - drivers
# cars not driven defined as the difference between number of
##drivers and the number of cars
cars_driven = drivers
#the number of cars on the road equals the drivers
carpool_capacity = cars_driven * space_in_a_car
#carpool capacity defined as the empty space in the car * the number of cars on
##the road (or the drivers)
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
#prints out the number of cars
print "There are only", drivers, "drivers available."
#prints out the number of drivers
print "There will be", cars_not_driven, "empty cars today."
#runs the operation for cars_not_driven, and that's the number of empty cars
print "We can transport", carpool_capacity, "people today."
#shares the carpool capacity as defined above
print "We have", passengers, "to carpool today."
#number of passengers that need a ride
print "We need to put about", average_passengers_per_car, "in each car."
#messed up before when had ^ the first comma inside the "about," rather than
##having it as about",

##exercise explaining the following error
    #Traceback (most recent call last):
        #File "ex4.py", line 8 (in his program, line 17 in ours), in <module>
            #average_passengers_per_car = car_pool_capacity / passenger
    #NameError: name 'car_pool_capacity' is not defined
##My explanation:
    # in the operation car_pool_capacity / passenger --> passenger should be
    #'passengers' it's missing an s, there for it's not anything, and dividing by 0

    
