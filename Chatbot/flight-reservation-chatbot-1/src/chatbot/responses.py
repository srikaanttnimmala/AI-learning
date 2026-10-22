class ResponseManager:
    def __init__(self):
        self.responses = {
            "greeting": "Hello! How can I assist you with your flight reservation today?",
            "fare_query": "Could you please provide the destination and travel dates?",
            "booking_confirmation": "Your flight has been successfully booked! Thank you for choosing us.",
            "fallback": "I'm sorry, I didn't understand that. Can you please rephrase?"
        }

    def get_response(self, intent):
        return self.responses.get(intent, self.responses["fallback"])