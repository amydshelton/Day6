"Writing a script to spit out restaurant ratings in abc order"

f = open("scores.txt")

rest_dict = {}

for line in f:
    line = line.strip()
    entries = line.split(':')
    restaurant = entries[0]
    score = entries[1]
    rest_dict[restaurant] = score

print sorted(rest_dict)

for restaurant in sorted(rest_dict):

    print "Restaurant %s is rated at %r" % (restaurant, rest_dict[restaurant])