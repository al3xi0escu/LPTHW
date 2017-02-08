#Put 100 in cars
cars = 100
#Make the space in the car 4.0
space_in_a_car = 4.0
#Make 30 drivers
drivers = 30
# Make 90 passengers
passengers = 90
#If there are no drivers the car doesn't drive
cars_not_driven = cars - drivers
#Cars with drivers drive
cars_driven = drivers
#Carpool capacity is cars driven and space in cars
carpool_capacity = cars_driven * space_in_a_car
#Averege passengers per cars
averege_passengers_per_car = passengers / cars_driven


# Write there are cars available
print "There are", cars, "cars available."
#Write There are only drivers available
print "There are only", drivers, "drivers available."
# Write there will be people today.
print "There will be", cars_not_driven, "empty cars today."
#Write we can transport people today
print "We can transport", carpool_capacity, "people today."
#Write we have to carpool today
print "We have", passengers, "to carpool today."
#Write we need about in each car
print "We need to put about", averege_passengers_per_car, "in each car."
