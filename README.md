# Course Embeddings API

This repository contains a Flask RESTful API for handling course information and their embeddings. The embeddings are generated using the `sentence-transformers` library and stored in a CSV file. The API provides endpoints to retrieve course information and their embeddings.

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Course Embeddings API allows users to generate embeddings for a list of course names and retrieve them via a RESTful API. The embeddings are generated using pre-trained models from the `sentence-transformers` library.

## Setup

### Prerequisites

- Python 3.6 or higher
- `pip` (Python package installer)


### Usage
After running the Flask app, you can access the API at http://localhost:5000.

### Example
To retrieve the list of courses and their embeddings, send a GET request to http://localhost:5000/courses.

bash
Copy code
curl http://localhost:5000/courses
API Endpoints
GET /
Returns a welcome message.

### Response
json
Copy code
{
    "message": "Hello, welcome to your course embeddings API!"
}
GET /courses
Returns the list of courses and their embeddings.

### Response
json
Copy code
[
    {
        "name": "LEARN SCRATCH PROGRAMMING",
        "embedding": [embedding_vector]
    },
    {
        "name": "LEARN CLOUD COMPUTING BASICS-AWS",
        "embedding": [embedding_vector]
    },
    ...
]
### Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes or enhancements.

### License
This project is licensed under the MIT License.
