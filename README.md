## Personality Analyzer
### This is for Human Resources or really anyone that wants to see the personality of a twitter user. This will give you the overall sentiment of a given twitter user.


![DEMO](twitter_personality.gif)

#### To use, simply run the below commands. (I used pipenv. Choose any virtual env that you like. However, you can just run the below)
```
pip3 install -U textblob  
python -m textblob.download_corpora
```
[See here for more details on textblob](https://textblob.readthedocs.io/en/dev)
```
pip3 install twint
```

#### Make sure to change the `Username` in `personality.py` to your target username.   
#### Then run: `python personality.py`.