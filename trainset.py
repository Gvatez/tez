import json
from nltk_utils import tokenize,stemming,bag_of_words



with open("intents.json",'r') as f:
    intents = json.load(f)

all_words = []
tags = []
xy = []

for intend in intents['intents']:
    tag = intend["tag"]
    tags.append(tag)
    for patterns in intend['patterns']:
        w = tokenize(patterns)
        all_words.extend(w)
        xy.append((w,tag))

spl_char = ['?',',','.','!']

all_words = [stemming(w) for w in all_words if w not in spl_char]
all_words = sorted(set(all_words))
tags = sorted(set(tags))
print(all_words)
print(xy)
print(tags)

x_train = []
y_train = []

for (pattern_set, tag) in xy:
    bag = bag_of_words(pattern_set,all_words)
    x_train.append(bag)

    label = tags.index(tag)
    y_train.append(label)

x_train = np.array(x_train)
y_train = np.array(y_train)

