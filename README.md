# Quiz App API

This API is designed to support a Quiz application, where users can take quizzes on various topics, and administrators can create and manage quizzes.

## Features
- Users can take quizzes on various topics and receive a score based on their answers
- Administrators can create quizzes, add questions to quizzes, and manage quizzes
- Quizzes are stored in a database and can be retrieved via the API

## Endpoints

The API supports the following endpoints:

- `GET /tracks`: Get all tracks
- `GET /topics/:id`: Retrieve a topic based on a track id
- `GET /questions/:id`: Retrieve a question based on a topic id
- `GET /options/:id`: Retrieve options for a question based on a question id
- `GET /answer/:id`: Retrieve the correct answer for a question based on a question id

## Postman Documentation

The API is documented using Postman. You can view the documentation [here](https://documenter.getpostman.com/view/19647041/2s935snMYs).


## Technology Stack

This API is built using Django and Django Rest Framework on the server-side, and uses a PostgreSQL database for storage.

## Getting Started

To get started with the Quiz App API, follow these steps:

1. Clone this repository to your local machine
2. Install the required dependencies by running `pip install -r requirements.txt`
3. Start the server by running `python manage.py runserver` (Make sure you are in the directory where manage.py is located)

## Contributing

If you are interested in contributing to this project, please fork the repository and create a pull request with your changes.

## License

This project is licensed under the [MIT License](LICENSE).
