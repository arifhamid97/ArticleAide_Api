# ArticleAide Backend

## Overview

ArticleAide Backend is a FastAPI application designed to serve as a proxy API for the ArticleAide Chrome extension to OpenAi model. It is built with FastAPI and LangChain to handle API calls and manage interactions efficiently.

## Features

- **Proxy API Calls:** Handles API requests from the ArticleAide Chrome extension.
- **FastAPI:** Provides a fast and efficient web framework for building APIs.
- **LangChain Integration:** Utilizes LangChain for natural language processing and management.

## Installation

1. **Clone the Repository**

2. **Install the dependacy**
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate
   pip install -r requirements.txt
   ```
3. **Run the application**
   ```bash
   fastapi dev main.py
   ```
