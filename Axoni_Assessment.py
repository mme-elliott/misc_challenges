# This is a coding assignment from another company as part of their technical review process. This was sent as a "take home" challenge.

### PLEASE NOTE: I created and tested this script with Python 3, running "python3 axoni_assessment.py" in terminal.
### I ran out of time before being able to return a list of shortest paths if there was more than one.

# Function to parse through flight_list and turn it into a dictionary to search through.
# Results are passed to another function, which are then returned to the main function for result.
def shortestPath(flight_list, desired_flight):
    # Write your code here
    # Break up flights_list into single lines based on the line break.
    flight_list = flight_list.splitlines()

    # Create new flight list without whitespace.
    flights = []

    # Remove whitespace.
    for x in range(len(flight_list)):
        if flight_list[x].strip():
            flights.append(flight_list[x].strip())

    # Create empty array.
    split_flights = []

    # Get rid of the connectors.
    for x in flights:
        split_flights.append(x.split(' -> '))

    # Split direct flight paths into tuples.
    flight_tuples = []
    for line in split_flights:
        for x in range(len(line)):
            start = line[x]

            # Make sure not to go out of bounds.
            if (x + 1) >= len(line):
                end = ""
            else:
                end = line[x + 1]

            # If end is not empty, then add it to the tuples list. Otherwise, leave it out - the flight doesn't have a next destination.
            if end:
                flight_tuples.append((start, end))


    # Create empty dictionary.
    flight_dict = {}

    # Populate dictionary with flight tuples.
    for flight in flight_tuples:
        start = flight[0]
        destination = flight[1]

        # If the key already exists in the dictionary, append the destination to the existing key.
        if start in flight_dict:
            flight_dict[start].append(destination)
        # Otherwise, create new key.
        else:
            flight_dict[start] = [destination]
        
    # Test if the desired path is a key in the dict - if it's not, there is no flight path.
    # Testing if origin flight exists as a key:
    if not desired_flight[0] in flight_dict:
        return None

    return findShortestFlight(flight_dict, desired_flight[0], desired_flight[1])
        
# Find the shortest flight path using the flight dict created above, starting origin and destination are what the user provided.
def findShortestFlight(flight_dict, origin, destination, path=[]):
    # Add origin flight to path
    path = path + [origin]

    # If the origin flight == destination flight, return the path
    if origin == destination:
        return path
    
    # If the origin flight isn't in the dictionary, return None.
    if not origin in flight_dict:
        return None
    
    # Create placeholder for shortest path.
    shortest_path = None

    # Go through flight keys in flight_dict
    for flight in flight_dict[origin]:
        # If the current flight isn't currently in the path, call function again.
        if flight not in path:
            new_path = findShortestFlight(flight_dict, flight, destination, path)

            # If new path was successfully populated, test if it's the shortest path.
            if new_path:
                if not shortest_path or len(new_path) < len(shortest_path):
                    shortest_path = new_path
    return shortest_path

# Main
if __name__ == '__main__':
    test_flights  =  """
    NY -> Iceland -> London -> Berlin
    NY -> Maine -> London
    Berlin -> Paris -> Amsterdam
    Paris -> London -> Egypt
    """

    # Get origin and destination from user, input() returns strings so no need to cast/verify.
    origin = input("Please enter origin: ")
    destination = input("Please enter destination: ")

    # Create array using input from user.
    flight = [origin, destination]

    # Find the shortest path given the user's flight
    result = shortestPath(test_flights, flight)

    print(result)
