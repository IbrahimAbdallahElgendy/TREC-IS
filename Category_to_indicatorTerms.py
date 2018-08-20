from Preprocessing import Preprocessing
from secrets import consumer_key, consumer_secret, access_token, access_token_secret
import collections
from collections import Counter

tweetsPrp = Preprocessing(trec_path='/data/TRECIS-CTIT-H-Training.json', tweets_dir='data/tweets')

tweetsPrp.consumer_key=consumer_key
tweetsPrp.consumer_secret=consumer_secret
tweetsPrp.access_token=access_token
tweetsPrp.access_token_secret=access_token_secret

training_Data = tweetsPrp.load_training_data()

map_type = collections.defaultdict(list)

for _, tweet in training_Data.items():
    for term in tweet.indicatorTerms:
        map_type[tweet.categories[0]].append(term)

for key in map_type:
    indicatorTerms = map_type[key]
    counts = Counter(indicatorTerms)
    print(key , ' ', counts)