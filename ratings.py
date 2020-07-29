"""Restaurant rating lister."""

ratings_file = open('scores.txt')
print_ratings = {}

# put your code here
def restaurant_ratings(ratings_file, print_ratings, user_ratings):
    for rating in ratings_file:
        rating = rating.rstrip()
        rating = rating.split(':')
        rest_name = rating[0]
        rest_score = int(rating[1])
        print_ratings[rest_name] = rest_score
        
        print_ratings.add(user_ratings)
        
        
        
        print_ratings_items = print_ratings.items()
        sorted_print_ratings_items = sorted(print_ratings_items)
        
        
        
    # print(sorted_print_ratings_items)
        
    for item in sorted_print_ratings_items:
        print(f"{item[0]} is rated at {item[1]}.")
        
    return sorted_print_ratings_items
    
restaurant_ratings(ratings_file, print_ratings, user_ratings())

def user_ratings():
    user_ratings= {}
    user_rest = input('Add A Resturant? >')
    user_score = int(input('Add a Score? > '))
    user_ratings[user_rest] = user_score
    return (user_ratings)

user_ratings()



