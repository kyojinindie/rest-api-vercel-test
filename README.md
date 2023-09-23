# FastAPI API

This is a FastAPI-based API that provides health check and text generation functionality using OpenAI's GPT-3 model.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

- Python 3.x
- [FastAPI](https://fastapi.tiangolo.com/)
- [OpenAI Python](https://github.com/openai/openai-python)
- [pydantic](https://pydantic-docs.helpmanual.io/)

### Installation

1. Clone the repository:

```shell
$ git clone https://github.com/kyojinindie/rest-api-vercel-test.git
```

2. Install dependencies:

```shell
$ pip install -r requirements.txt
```

## Usage

- Run dev server:
```shell
$ uvicorn main:app --reload
```
## Testing

To test the functionality of the API endpoints, you can use the `test_main.http` file located in the project directory. This file contains a set of HTTP requests that can be executed using tools like Visual Studio Code's REST Client extension or cURL.

Follow the steps below to run the HTTP requests:

1. Open the `test_main.http` file in a code editor or REST Client extension.

2. Make sure your FastAPI development server is running.

3. For each request in the `test_main.http` file, send the request by clicking the "Send Request" button or using the appropriate command in the REST Client extension.

4. Check the response received from the API and verify that it matches the expected output.

These test requests can help you validate the functionality of your API endpoints and ensure they are working as intended. Feel free to modify the requests or add new ones to suit your testing needs.


## Endpoints

### Health Check

- **Endpoint**: `/health`
- **Method**: GET
- **Description**: The health check endpoint is a simple API endpoint that can be used to verify the status and availability of the API
- **Response**: 
```json
{"status": "ok"}
```


### Text Generation

- **Endpoint**: `/api/v1/text-davinci-003`
- **Method**: POST
- **Description**: An endpoint that generates text using OpenAI's GPT-3 model.
- **Request**:
  - **Headers**:
    - `OPENAI_API_KEY`: The API key for OpenAI.
  - **Body**:
```json
{
  "prompt": "who is Cristiano Ronaldo?"
}
```


## Contributing

- Welcome code contributions from the community through pull requests.

## License
- MIT License