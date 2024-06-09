# End-to-End NLP Text Summarizer

## Overview

This repository contains the code and resources for an end-to-end Natural Language Processing (NLP) text summarizer. The project focuses on summarizing longer pieces of text, such as articles or documents, into shorter, more concise versions while preserving key information and meaning.


## Project Structure

The project is structured as follows:

- `.github/`: Houses GitHub Actions workflows for automated testing and deployment.
- `config/`: Includes configuration files for setting up the summarization pipeline.
- `research/`: Contains Jupyter Notebooks used for research, experimentation, and model development.
- `src/`: Contains the source code for the text summarizer application.
    - `components/`: Source code for data ingestion, data transformation, data validation.
    - `config/`: Contains the configuration for scripts in `components/`.
    - `constants/`: Constants used in the project are defined here.
    - `logging/`: Contains the source code for custom logging.
    - `utils/`: Common functions used throughout the project are defined here.
    - `pipeline/`: Pipeline used for summarization.
- `Dockerfile`: Defines the Docker image configuration for containerizing the application.
- `main.py`: Contains the source code to run the scripts in `src/` directory.
- `requirements.txt`: File containing the necessary dependencies to run the project.
- `setup.py`: Specifies package metadata.
- `template.py`: Contains the soirce code to create the porject files in the specified structure.


<!---
## Getting Started

To get started with the project, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies using:
    ```bash
    pip install -r requirements.txt
    ```
3. Explore the source code in the `src/` directory to understand the text summarization pipeline.
4. Run the scripts in the `src/` directory for text summarization.

## Usage

- **Flask App:** 
    ```bash
    python app.py
--->
