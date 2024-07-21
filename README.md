# RAG-system

# Intelligent QA System

Welcome to the **Intelligent QA System**! This application leverages modern language models and vector databases to provide intelligent question-answering capabilities. It uses various tools and technologies to handle and process queries effectively.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Dependencies](#dependencies)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Interactive Question Answering**: Ask questions and receive intelligent answers based on a pre-loaded vector database.
- **Language Model Integration**: Utilizes advanced language models like Google Generative AI and Hugging Face for high-quality responses.
- **Customizable Vector Database**: Manage and update the vector database as needed for tailored responses.

## Installation

To set up the **Intelligent QA System** on your local machine, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Adekunle-Habeeb/Intelligent-QA-System.git
   cd Intelligent-QA-System
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   Ensure that you have the correct version of Python and `pip` installed. Then, install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

   ```bash
   streamlit run main.py
   ```

## Usage

1. **Start the Application**

   After installation, start the application with Streamlit:

   ```bash
   streamlit run main.py
   ```

2. **Interact with the App**

   Open your web browser and navigate to `http://localhost:8501`. You will see the application interface where you can ask your questions.

3. **Provide Input**

   Use the input box to ask questions. The system will process your query and provide a response based on the data in the vector database.

## Configuration

The application uses a `.env` file for configuration settings. Create a `.env` file in the root directory with the following environment variables:

```env
GOOGLE_API_KEY=your_google_api_key
```

Replace `your_google_api_key` with your actual API key for Google services.

## Dependencies

The application requires the following dependencies:

- `langchain==0.2.8`
- `python-dotenv==1.0.0`
- `streamlit>=1.24.0`
- `tiktoken==0.4.0`
- `faiss-cpu==1.7.4`
- `protobuf>=3.20,<5`
- `langchain-google-genai==1.0.7`
- `google-generativeai==0.7.2`
- `google-ai-generativelanguage==0.6.6`
- `langchain-community==0.2.7`
- `transformers==4.37.2`
- `torch==2.3.0`
- `scipy==1.10.1`
- `numpy==1.23.4`
- `pandas==1.5.3`
- `sentence-transformers==2.2.2`
- `InstructorEmbedding==0.0.5`

## Troubleshooting

- **Dependency Conflicts**: If you encounter dependency conflicts, try adjusting the versions in `requirements.txt` or use `pip` to resolve conflicts manually.

- **Streamlit Frontend Issues**: If you experience frontend issues, try clearing your browser cache and refreshing the page. Ensure you are using a compatible version of Streamlit.

- **Import Errors**: Make sure all required packages are installed and up-to-date. Check the compatibility of the installed libraries.

## Contributing

Contributions are welcome! If you find a bug or have suggestions for improvements, please create an issue or submit a pull request on the [GitHub repository]([https://github.com/Adekunle-Habeeb/Intelligent-QA-System](https://github.com/Adekunle-Habeeb/RAG-system)).

