

from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
import os
import pandas as pd
from langchain.document_loaders import DataFrameLoader
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
import pinecone
import openai


load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
PINECONE_API_ENV = os.getenv('PINECONE_API_ENV')


# Create a Flask app instance
app = Flask(__name__, static_folder='static')
app.debug = True


# Define a route and its corresponding view function
@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        return render_template('base.html', question="", answer="")
    else:
        question = str(request.form['question'])
        return redirect(url_for("get_response", question=question))


@app.route('/<question>', methods=['GET', 'POST'])
def get_response(question):
    
    answer = get_embeddings(question)

    return render_template('base.html', question=question, answer=answer)


def get_embeddings(question):
    
    EMBEDDING_MODEL = "text-embedding-ada-002"

    pinecone.init(
        api_key = PINECONE_API_KEY,
        environment = PINECONE_API_ENV
    )
    index_name = 'theairace'

    index = pinecone.Index(index_name)

    embed_query = openai.Embedding.create(
        input=question,
        engine=EMBEDDING_MODEL
    )

    question_embeddings = embed_query['data'][0]['embedding']

    similarity_search = index.query(question_embeddings, top_k=5, include_metadata=True)

    top5 = []
    for sims in similarity_search['matches']:
        text = sims['metadata']['text']
        top5.append(text)

    df = pd.DataFrame(top5, columns=['text'])


    # Load OpenAI and question-answer chain from LangChain
    llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
    chain = load_qa_chain(llm, chain_type="stuff")

    loader = DataFrameLoader(df, page_content_column='text')
    docs = loader.load()

    # Answers the question based on the relevant docs passed in from Pinecone
    return chain.run(input_documents=docs, question=question)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)