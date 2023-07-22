## twitter-gpt

Project scrapes tweets from a twitter account and creates vector embeddings for each tweet before inserting into Pinecone vector DB. This process all happens in a separate ipynb notebook not uploaded to this repo.

The app portion takes a question and is able to answer questions in natural language based on those tweets only.

Backend takes question as input, embeds it using OpenAI embedding model, runs a similarity search in Pinecone DB of user tweets, and answers question in natural language based on most relevant tweets. Talk to any digital profile!

Answers could improve by indexing more tweets from different accounts, but keeping it limited to one account, for now.

### Improvements
• Could use metadata in Pinecone - When tweet was tweeted, tweed id, tweet id of the original tweet it's replying to, etc.
• Metadata for segmentation - Partition data by the account it's tweeted by, that way you can search based on account, not by all the tweets in DB
• Always save data that you pull into a raw format, so you don't have to keep calling API and pushing API rate limits


## Requirements

• pipenv

```bash
brew install pipenv
```

### Run this project
```bash
pipenv install
```

```bash
python3 -m flask run
```




