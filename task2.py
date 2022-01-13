# putting variables kilometer and miles.
km = []
miles = []
while True:
    # taking input from users.
    s = input("Enter the reading:")
    if s == "":
        break
        # taking float input from 2.
    speed = float(s[1:])
    # append(adds a single item to the existing list.) take speed in miles and km in list.
    miles.append(speed) if s[0].lower() == "u" else km.append(speed)
    # making newlist and creating copy of existing list.
newlst = miles.copy()
# converting kilometer into miles.
miles += [i*0.621371 for i in km]
# converting miles into kilometer.
km += [i*1.60934 for i in newlst]
# if length of kilometer is not equals to zero.
if len(km) != 0:
    # taking maximum kilometer and maximum miles.
    print("max:{:.2f}km,{:.2f}miles".format(max(km), max(miles)))
    # taking maximum minimum and minimum miles.
    print("min:{:.2f}km,{:.2f}miles".format(min(km), min(miles)))
    # first sum kilometer and miles and then divide it by length of kilometer and miles.
    # .format accessed the value of s and store it inside string placeholder.
    print("average:{:.2f}km,{:.2f}miles".format(sum(km)/len(km), sum(miles)/len(miles)))
    print("{} of readings were made".format(len(km)))

# if user input no values
else:
    print("no reading entered")
