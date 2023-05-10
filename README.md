## twitter-gpt

Project scrapes tweets from a twitter account and creates vector embeddings for each tweet before inserting into Pinecone vector DB. This process all happens in a separate ipynb notebook not uploaded to this repo.

The app portion takes a question and is able to answer questions in natural language based on those tweets only.

Backend takes question as input, embeds it using OpenAI embedding model, runs a similarity search in Pinecone DB of user tweets, and answers question in natural language based on most relevant tweets. Talk to any digital profile!

Answers could improve by indexing more tweets from different accounts, but keeping it limited to one account, for now ;)


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




