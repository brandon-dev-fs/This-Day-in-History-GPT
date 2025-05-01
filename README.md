# This Day in History GPT

Generate summaries of the news for any particular day.  
![Powered by NY Times Branding](/src/assets/images/poweredby_nytimes_65a.png)

## Overview

This is a basic python console application that utilizes the NY Times Archieve API and OpenAI or Anthropic Models to generate a summarization of the days headlines on a specific date between 1855 and 2020.

### Requirements

- [Python Version 3.13](https://www.python.org/downloads/)
- [NY Times API Key](https://developer.nytimes.com/get-started) | Free
- [Anthropic API Key](https://docs.anthropic.com/en/api/getting-started) | [API Pricing](https://www.anthropic.com/pricing#api)
- or [OpenAI API Key](https://platform.openai.com/docs/api-reference/introduction) | [API Pricing](https://openai.com/api/pricing/)

### Getting Started

Clone the repository

Add a `.env` file with the following keys  
`ANTHROPIC_API_KEY={antropic_api_key}`  
`ANTHROPIC_MODEL={antropic_model}`  
`OPENAI_API_KEY={openai_api_key}`  
`OPENAI_MODEL={openai_model}`  
`NYT_API_KEY={nytimes_api_key}`

Add an empty directory `output` under `src`

Create a virtual enviornment `python -m venv venv`

Activate your virtual enviornment `venv\Scripts\activate.bat`

Install Packages `pip install -r requirements.txt`

To run the code, from the base directory run `python -m src\__main__.py`
