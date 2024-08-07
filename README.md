# Buildcopilotwith-cache-and-your-data
sample code to bulid your copilot and load your data inside and put question and answer in cache to save time
# Cosmsodbnosql-generative-AI-sampleAI

please find the architecture diagram 
 
![image](https://github.com/user-attachments/assets/5bfabda9-68a1-4706-8f3f-3f0205435d48)




## Features
- Vector search using Azure Cosmos DB for NoSQL
- Create embeddings using Azure OpenAI text-embedding
- Use cosmosdb Nosql as cache to save latency

## Requirements
- Tested only with Python 3.11
- Azure OpenAI account
- Azure Cosmos DB for NoSQL account

## Setup
- Create virtual environment: python -m venv .venv
- Activate virtual ennvironment: .venv\scripts\activate
- Install required libraries: pip install -r requirements.txt
- Replace keys with your own values in example.env

## Demo script
- Open "cosmosddbnosql.ipynb" python notebook
- Run the cells to create the database (with vector support), create the container and populate the Cosmos DB database with different data 
- The last cell launch Gradio UI 
- if you ingest the samples pdf and word  file, you can ask these questions :

"Groupama ? "
"Tell me about proposal for services ? "
