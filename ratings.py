"""Restaurant rating lister."""

ratings_file = open('scores.txt')
print_ratings = {}

# put your code here
def restaurant_ratings(ratings_file, print_ratings):
    for rating in ratings_file:
        rating = rating.rstrip()
        rating = rating.split(':')
        rest_name = rating[0]
        rest_score = int(rating[1])
        print_ratings[rest_name] = rest_score
    print(print_ratings)
        
restaurant_ratings(ratings_file, print_ratings)