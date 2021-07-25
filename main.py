locations = {0:  {"desc": "your sitting in front of a coumputer learning python",
                  "exits":{},
                  "namedExits":{}},
             1:  {"desc":"you standing at the end of a road before a small brice building",
                  "exits": {"W": 2,"E":3,"N":5,"S":4,"Q":0},
                  "namedExits": {"2":2,"3":3,"5":5,"4":4}},
             2:  {"desc": "your at the top of a hill",
                  "exits": {"N":5, "Q":0},
                  "namedExits":{"5":5}},
             3:  {"desc":"your inside a building , well house for small stream ",
                  "exits":{"W":1, "Q":0},
                  "namedExits":{"1":1}},
             4:  {"desc": "your in a vally beside a stream",
                  "exits":{"N":1, "W":2,"Q":0},
                  "namedExits": {"1":1,"2":2}},
             5:  {"desc":"you are in the forest",
                  "exits":{"W":2, "S":1,"Q":0},
                  "namedExits":{"2":2,"1":1}}
             }


vocabulary = {"QUIT":"Q",
              "NORTH": "N",
              "SOUTH":"S",
              "EAST":"E",
              "WEST":"W",
              "ROAD":"1",
              "HILL":"2",
              "BUILDING":"3",
              "VALLY":"4",
              "FOREST":"5"}

loc = 1
while True:
    avaliableExits = " , ".join(locations[loc]["exits"].keys())

    print(locations[loc]["desc"])

    if loc  ==0:
        break
    else:
        allExits = locations[loc]["exits"].copy()
        allExits.update(locations[loc]["namedExits"])

    direction = input("Available exits are " + avaliableExits + " ").upper()
    print()
    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break
    if direction in allExits:
         loc = allExits[direction]
    else:
        print("you can not go to that direction ")