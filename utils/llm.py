from langchain_community.llms import HuggingFaceTextGenInference
from dotenv import load_dotenv
import os
from langchain_huggingface import HuggingFaceEndpoint
from langchain_community.llms import Ollama

# Load environment variables
# load_dotenv()
load_dotenv(dotenv_path='./.env.dev', override=True)

hf_token = os.getenv('hf_token')
llm = HuggingFaceTextGenInference(
    inference_server_url="https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct",
    server_kwargs={
        "headers": {
            "Authorization": f"Bearer {hf_token}",
            "Content-Type": "application/json",
        }
    },
    streaming=True,
    max_new_tokens=512
)

# llm = Ollama(
#     model="llama3"
# )