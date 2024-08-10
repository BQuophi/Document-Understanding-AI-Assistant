# Document-Understanding AI Assistant Web App

## Overview

This project implements an interactive AI assistant capable of understanding and answering questions about content from PDF or TXT files. The assistant leverages LangChain for language processing, FAISS for efficient similarity search, and Anthropic's Claude 3 language model for document comprehension. The user interface is built with Streamlit, providing an intuitive web-based interaction experience.

## Features

- **Document Processing**: Extracts and preprocesses content from PDF and TXT files.
- **AI-Powered Question Answering**: Utilizes one of the Claude models to provide context-aware responses based on document content.
- **Vector Search**: Implements FAISS for efficient retrieval of relevant document sections.
- **Interactive UI**: Streamlit-based web interface for easy file upload and question asking.
- **Feedback Mechanism**: Allows users to rate answers and provide improvement suggestions.

## Technology Stack

- **Python**: Core programming language
- **LangChain**: Framework for developing applications with language models
- **Anthropic's Claude 3**: Large language model for natural language understanding and generation
- **FAISS**: Vector database for similarity search
- **Streamlit**: Web application framework for the user interface
- **PyPDF**: Library for extracting text from PDF files

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/document-understanding-ai-assistant.git
   cd document-understanding-ai-assistant
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your Anthropic API key:
   - Create a `.streamlit/secrets.toml` file in the project root
   - Add your API key: `anthropic_api_key = "your-api-key-here"`

5. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## Usage

1. Open the Streamlit app in your web browser (typically at `http://localhost:8501`).
2. Upload a PDF or TXT file using the file uploader.
3. Once the file is processed, you can either select a predefined question or type your own.
4. The AI assistant will provide an answer based on the document content.
5. Rate the answer's helpfulness and provide feedback if desired.

## Project Structure

- `app.py`: Main application file containing the Streamlit UI and core logic
- `requirements.txt`: List of Python dependencies
- `.streamlit/secrets.toml`: Configuration file for storing the Anthropic API key (not included in repository)

## How It Works

1. **Document Processing**: The app uses PyPDF to extract text from PDF files or reads TXT files directly.
2. **Text Embedding**: The extracted text is split into chunks and embedded using HuggingFace embeddings.
3. **Vector Storage**: FAISS is used to store and index the text embeddings for efficient retrieval.
4. **Question Answering**: When a user asks a question, the app retrieves relevant text chunks using FAISS and passes them to the Claude model along with the question.
5. **Response Generation**: Claude generates a response based on the retrieved context and the question.
6. **Feedback Loop**: Users can provide feedback on the responses, which can be used for future improvements.

## Future Improvements

- Implement more advanced document preprocessing techniques
- Add support for more file formats (e.g., DOCX, HTML)
- Enhance the feedback mechanism to actively improve the model's responses

## Contributing

Contributions to improve the project are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

[MIT License](LICENSE)
