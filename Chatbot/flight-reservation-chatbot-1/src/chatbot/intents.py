class Intents:
    def __init__(self, intents_file):
        self.intents_file = intents_file
        self.intents = self.load_intents()

    def load_intents(self):
        import json
        with open(self.intents_file, 'r') as file:
            return json.load(file)

    def get_intent(self, user_input):
        for intent in self.intents['intents']:
            if user_input in intent['patterns']:
                return intent['tag']
        return None

    def get_response(self, intent_tag):
        for intent in self.intents['intents']:
            if intent['tag'] == intent_tag:
                return intent['responses']
        return None