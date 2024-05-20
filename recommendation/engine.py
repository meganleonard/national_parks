
## Recommendation Program ##


## Database Connection

from database_access import connect_to_database, fetch_national_parks
conn = connect_to_database('national_parks.db')
national_parks_data = fetch_national_parks(conn)
conn.close()

# Convert each tuple to a dictionary
national_parks_dicts = []
keys = ['fullName', 'description', 'latitude', 'longitude', 'states', 'directionsInfo', 'designation']

for park_tuple in national_parks_data:
    park_dict = dict(zip(keys, park_tuple))
    national_parks_dicts.append(park_dict)

# Now 'national_parks_dicts' will contain dictionaries instead of tuples
print(national_parks_dicts[0].keys())  # Check the keys of the first dictionary





## User Input ##

class ContentBasedRecommender:
    def __init__(self, data):
        self.data = data
    
    def generate_recommendations(self, user_preferences):
        # Generate recommendations based on user preferences
        recommendations = []
        for park in self.data:
            # Compute relevance score based on park attributes and user preferences
            relevance_score = self.compute_relevance_score(park, user_preferences)
            recommendations.append((park['fullName'], relevance_score))
        
        # Sort recommendations by relevance score in descending order
        recommendations.sort(key=lambda x: x[1], reverse=True)
        
        return recommendations
    
    def compute_relevance_score(self, park, user_preferences):
        # Placeholder logic to compute relevance score
        relevance_score = 0
        for activity in user_preferences['activities']:
            if activity in park['activities']:
                relevance_score += 1
        return relevance_score


class RecommenderSystem:
    def __init__(self, data):
        self.data = data
    
    def fetch_activities(self):
        # Fetch a list of unique activities available at national parks
        activities_set = set()
        for park in self.data:
            activities_set.update(park.get('activities', {}).keys())
        return sorted(list(activities_set))
    
    def get_user_preferences(self):
        # Ask the user for their preferences
        temperature_range = input("Enter the temperature range you want to experience (e.g., '50-80'): ")
        activities = input("Enter the activities you want to do (comma-separated): ")
        
        # Parse user input
        min_temperature, max_temperature = map(int, temperature_range.split('-'))
        activities = [activity.strip() for activity in activities.split(',')]
        
        return min_temperature, max_temperature, activities
    
    def generate_recommendations(self, user_preferences):
        # Generate recommendations for the user based on their preferences
        min_temperature, max_temperature, activities = user_preferences
        
        # Placeholder recommendation logic
        recommendations = []
        for park in self.data:
            relevance_score = self.compute_relevance_score(park, activities)
            if min_temperature <= park['temperature'] <= max_temperature:
                recommendations.append((park['fullName'], relevance_score))
        
        # Sort recommendations by relevance score in descending order
        recommendations.sort(key=lambda x: x[1], reverse=True)
        
        return recommendations
        
    def present_recommendations(self, recommendations):
        # Present recommendations to the user
        print("Recommended parks:")
        for park, relevance_score in recommendations:
            print(f"{park}: relevance score = {relevance_score}")

class ContentBasedRecommender:
    def __init__(self, data):
        self.data = data
    
    def generate_recommendations(self, user_preferences):
        # Generate recommendations based on user preferences
        recommendations = []
        for park in self.data:
            # Compute relevance score based on park attributes and user preferences
            relevance_score = self.compute_relevance_score(park, user_preferences)
            recommendations.append((park['fullName'], relevance_score))
        
        # Sort recommendations by relevance score in descending order
        recommendations.sort(key=lambda x: x[1], reverse=True)
        
        return recommendations
    
    def compute_relevance_score(self, park, user_preferences):
        # Placeholder logic to compute relevance score
        relevance_score = 0
        for activity in user_preferences['activities']:
            if activity in park['activities']:
                relevance_score += 1
        return relevance_score            


# Main code
if __name__ == "__main__":
    # Initialize the recommender system with data
    recommender_system = RecommenderSystem(national_parks_data)
    
    # Fetch a list of activities available at national parks
    activities = recommender_system.fetch_activities()
    print("Activities available at national parks:", activities)
    
    # Get user preferences
    min_temperature, max_temperature, user_activities = recommender_system.get_user_preferences()
    
    # Generate recommendations based on user preferences
    user_preferences = {'activities': user_activities}
    recommendations = recommender_system.generate_recommendations((min_temperature, max_temperature, user_activities))
    
    # Present recommendations to the user
    recommender_system.present_recommendations(recommendations)

