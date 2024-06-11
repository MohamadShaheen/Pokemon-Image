# Pokemon Images Project

This project represents a simple server that allows interaction with a database of Pokemon images. One can view, search, and filter Pokemon images through the terminal or the FastAPI interface.

## Features

- Search Pokemon image by name
- Search all Pokemons images name
- See Pokemon image by name
- Add new Pokemon image using external API
- Delete Pokemon image
- Update Pokemon image

## Technologies Used

- Python
- FastAPI
- Requests
- Pillow
- PyMongo

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/MohamadShaheen/Pokemon-Project.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Pokemon-Project
    ```
3. Create and activate a virtual environment:
    ```sh
    python -m venv env
    source env/Scripts/activate  # On Mac use `env\bin\activate`
    ```
4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Database Setup

1. Ensure pymongo is installed and running.
2. Create a new database scheme for the project (recommended: with the name `pokemonsdatabase`).
3. Create `.env` file for the project:
   ```
   DATABASE_HOST=[YOUR DATABASE HOST]
   DATABASE_PORT=[YOUR DATABASE PORT]
   DATABASE_NAME=[YOUR SCHEME NAME]
   DATABASE_COLLECTION=[YOUR COLLECTION NAME]
   SERVER_HOST=[YOUR SERVER HOST]
   SERVER_PORT=[YOUR SERVER PORT]
   ```
4. Update the `config.json` file:
   ```
   {
    "poke_api_URL": "https://pokeapi.co/api/v2/pokemon",
    "database_editor": 1,
    "create_database": 0
   }
   ```
5. Run the `database/create_database.py` to fill the database.

## Running the Application

1. Start the FastAPI server:
    ```sh
    uvicorn server:app --reload
    ```

## Testing

1. Not implemented yet.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## Contact

For any questions or inquiries, please contact [Mohamad Shaheen](https://github.com/MohamadShaheen).