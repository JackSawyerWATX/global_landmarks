# TODO: Declare a global list to keep track of visited landmarks
visited_landmarks=[]
# TODO: Define a function named log_landmark that takes two parameters: landmark and city
def log_landmark(landmark, city):
    # TODO: Add the landmark and its city to the global list in the format "landmark in city"
    global visited_landmarks
    visited_landmarks.append(f"{landmark}, {city}")

# TODO: Call the log_landmark function with examples e.g., "Eiffel Tower" and "Paris"
log_landmark("Eiffel Tower", "Paris")
log_landmark("Great Pyramids", "Giza")
log_landmark("Taj Mahal", "India")
# TODO: Print the list of visited landmarks
print(visited_landmarks)



