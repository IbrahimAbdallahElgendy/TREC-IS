# TREC-IS

### Project Installation 
After cloning/downloading the project, create a secrets.py file inside the parent directory (TREC-IS) and store the twitter-API access keys and babelnet-key in it. Check the [section below](#how-to-get-the-access-keys) to know how to get the access keys. <br>

Given below is a sample of <b> secrets.py </b> file:

```
consumer_key='xxxx'
consumer_secret='xxxx'
access_token='xxxx'
access_token_secret='xxxx'
babelnet_key='xxxx'
```
##### Installing python packages 
Create a virtual environment for the project and install all the python packages using requirements.txt. 
```
cd TREC-IS/
virtualenv -p python3 envname
source envname/bin/activate 
pip install -r requirements.txt
```

#### How to get the access keys?
Check out the '<b> Creating a Twitter app </b>' section in [twitter's documentation for developers](https://developer.twitter.com/en/docs/basics/getting-started) to get the consumer keys and access tokens. 

For extracting Bag-of-Concepts features, you would require an access key from BabelNet. First create an [account on it](https://babelnet.org/register) and after logging in, fill the form as mentioned [here](http://babelfy.org/guide) to increase the daily limit. 
Add the unique API key as 'babelnet_key' in secrets.py and then you're ready to go.!  

##### Install the following dependencies before using the ```Feature_Extractor``` class: <br>
- [spacy](https://spacy.io/usage/models#section-install) :
```
pip install -U spacy 
python -m spacy download en
```
- [nltk](https://www.nltk.org/install.html) <br>
```pip install -U nltk ``` <br>
Enter python shell and then download all the nltk packages. 
```
>> import nltk
>> nltk.download( )

```
- [scikit-learn](http://scikit-learn.org/stable/install.html)
```
pip install -U scikit-learn
```
- [textblob](https://textblob.readthedocs.io/en/dev/)
```
pip install -U textblob
python -m textblob.download_corpora

```
- [embedding pre-trained model](https://www.dropbox.com/s/3jao9guquyvysve/glove.840B.300d.txt?dl=0)
``` 
download the glove pre-trained model into data/embeddings folder. 

```
