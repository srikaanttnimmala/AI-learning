# Flight Reservation Chatbot

This project is a flight reservation chatbot built using Streamlit. The chatbot is designed to assist users in finding and booking flights through a conversational interface.

## Project Structure

```
flight-reservation-chatbot
├── src
│   ├── app.py               # Entry point of the Streamlit application
│   ├── chatbot
│   │   ├── __init__.py      # Initializes the chatbot module
│   │   ├── intents.py       # Manages user intents
│   │   └── responses.py     # Manages chatbot responses
│   └── utils
│       ├── __init__.py      # Initializes the utils module
│       └── helpers.py       # Contains helper functions
├── requirements.txt          # Lists project dependencies
├── .streamlit
│   └── config.toml          # Configuration settings for Streamlit
└── README.md                 # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd flight-reservation-chatbot
   ```

2. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```
   streamlit run src/app.py
   ```

## Usage

Once the application is running, you can interact with the chatbot through the Streamlit interface. The chatbot will assist you in searching for flights, providing information about available options, and guiding you through the booking process.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.