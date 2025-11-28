# LangChain Examples

This repository contains a collection of example notebooks and scripts demonstrating various functionalities of the LangChain library. It covers core concepts such as interacting with Large Language Models (LLMs), utilizing chat models, defining and loading prompt templates, managing conversational messages, and building agents. The examples showcase integrations with popular LLM providers like Google Gemini and OpenAI, as well as Hugging Face models, both online and locally. This resource is designed to help developers quickly understand and implement LangChain for building powerful AI applications.

## Run Instructions

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/tauhidhasan811/lang-chain
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd lang-chain
    ```
3.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```
4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Set up environment variables:**
    *   Create a `.env` file in the root directory.
    *   Add your API keys as required by the specific examples (e.g., `GOOGLE_API_KEY`, `OPENAI_API_KEY`).
6.  **Run the examples:**
    *   **For Jupyter Notebooks:**
        *   Install Jupyter Lab: `pip install jupyterlab`
        *   Launch Jupyter Lab: `jupyter lab`
        *   Open the desired `.ipynb` file in the Jupyter interface and run the cells.
    *   **For Python Scripts:**
        *   Execute directly using Python: `python <script_name.py>`

## Folder Structure

```
root
| ---> .gitignore
| ---> chatbot.ipynb
| ---> requirements.txt
| ---> 1. LLMs
|    | ---> 1 Model.ipynb
|    | ---> 1_llm_demon.py
| ---> 2. ChatModel
|    | ---> 2_caude.ipynb
|    | ---> 2_chatgoogle.ipynb
|    | ---> 4_chatHuggingFace.ipynb
|    | ---> 5_huggingface_hf_local.ipynb
| ---> 3. Prompts
|    | ---> 1_templete.ipynb
|    | ---> 2_load_temp.ipynb
|    | ---> 3_CHART_PROMPT_TEMPLETE.ipynb
| ---> 4. Message
|    | ---> message.ipynb
| ---> 5. Agent
|    | ---> 1_agent.ipynb
| ---> 6.output_parser
|    | ---> first.py
```

## File Descriptions

*   `.gitignore`: Specifies files and directories to be ignored by Git, such as environment configuration files and virtual environment directories.
*   `chatbot.ipynb`: Initializes a chatbot using Google's Gemini-2.5-Flash model, loading environment variables for API keys and setting up the chat model for conversational AI.
*   `requirements.txt`: Lists essential Python packages for LangChain development, including LLM integrations and environment management tools.
*   `1. LLMs/1 Model.ipynb`: Demonstrates the foundational use of the Langchain library for Large Language Models (LLMs) by importing the library and confirming its version.
*   `1. LLMs/1_llm_demon.py`: Shows how to use Langchain to interact with OpenAI's GPT-3.5 Turbo Instruct model, querying for the capital of India and printing the response.
*   `2. ChatModel/2_caude.ipynb`: A Jupyter Notebook designed for implementing and experimenting with a chat model, likely containing code for defining, training, and interacting with conversational AI.
*   `2. ChatModel/2_chatgoogle.ipynb`: Initializes a connection to Google's Gemini-2.5-Flash model using Langchain, loading environment variables and preparing the model for prompt invocation.
*   `2. ChatModel/4_chatHuggingFace.ipynb`: Demonstrates using Hugging Face models for conversational AI via `langchain-huggingface`, setting up a `ChatHuggingFace` pipeline.
*   `2. ChatModel/5_huggingface_hf_local.ipynb`: Illustrates integrating local Hugging Face models with Langchain for chat applications, including parsing LLM output for user and assistant responses.
*   `3. Prompts/1_templete.ipynb`: Defines a `PromptTemplate` for generating structured prompts to summarize research papers, allowing customization of title, style, and length.
*   `3. Prompts/2_load_temp.ipynb`: Demonstrates loading a pre-defined prompt template from a JSON file using Langchain and initializing a `ChatGoogleGenerativeAI` model.
*   `3. Prompts/3_CHART_PROMPT_TEMPLETE.ipynb`: Defines a `ChatMessagePromptTemplate` for structured conversational AI, creating system and human messages for organized interactions.
*   `4. Message/message.ipynb`: Initializes a conversation with a Google Gemini-2.5-flash AI model, loading environment variables and defining message types for structuring interactions.
*   `5. Agent/1_agent.ipynb`: Demonstrates the creation of a LangChain agent, showing an example that fails due to an undefined `read_email` function, highlighting a missing dependency.
*   `6.output_parser/first.py`: Uses Langchain and Hugging Face to interact with a language model, generating a detailed report on "black holes" and then summarizing it.

## Git URL

https://github.com/tauhidhasan811/lang-chain
