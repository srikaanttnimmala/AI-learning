def format_flight_data(flight_data):
    formatted_data = []
    for flight in flight_data:
        formatted_data.append({
            "Flight Number": flight.get("flight_number"),
            "Departure": flight.get("departure"),
            "Arrival": flight.get("arrival"),
            "Price": f"${flight.get('price', 0):,.2f}",
            "Duration": flight.get("duration"),
        })
    return formatted_data

def validate_input(user_input):
    if not user_input or not isinstance(user_input, str):
        return False
    return True

def extract_flight_info(flight_string):
    # This function assumes the flight_string is formatted in a specific way
    parts = flight_string.split(',')
    if len(parts) < 3:
        return None
    return {
        "departure": parts[0].strip(),
        "arrival": parts[1].strip(),
        "date": parts[2].strip(),
    }