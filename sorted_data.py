"Writing a script to spit out restaurant ratings in custom order (descending by rating)"

f = open("scores.txt")

rest_dict = {}

for line in f:
    line = line.strip()
    restaurant,score = line.split(':')
    # restaurant = entries[0]
    # score = entries[1]
    rest_dict[restaurant] = int(score)

my_key = rest_dict.get
# print sorted(rest_dict, key = my_key)

for restaurant in sorted(rest_dict, key = my_key, reverse =  True):

    print "Restaurant %s is rated at %r" % (restaurant, rest_dict[restaurant])