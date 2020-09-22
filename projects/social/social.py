from numpy import random
from itertools import combinations


class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(num_users):
            self.add_user(i)

        # Get a list of possible friendship combinations
        combos = list(combinations(list(self.users.keys()), 2))

        # Shuffle list of friendship combinations
        random.shuffle(combos)

        # Store the number of friendships to create
        # Divide by 2 because each add_friendship() call will create two friendships
        num_friendships = int((num_users * avg_friendships) / 2)

        # A list of friendships, of length num_friendships
        resulting_friendships = combos[:num_friendships]

        # For each tuple friendship
        for friendship in resulting_friendships:

            # Add it to our social graph
            self.add_friendship(friendship[0], friendship[1])


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        # create a visited dict
        visited = {}  

        # create a queue
        queue = []

        # add our user_id to the queue
        queue.append(user_id)

        # add user_id to dict
        visited[user_id] = [user_id]

        # while items in our queue
        while queue:

            # pop off the user at the front of the queue
            current = queue.pop(0)

            # get user's friends
            friends = self.friendships[current]

            # for each friend
            for friend in friends:

                # if we haven't added friend to dictionary
                if friend not in visited:

                    # add friend to dict with its value being the path
                    # so far plus this latest node
                    visited[friend] = visited[current] + [friend]

                    # add the friend to the queue
                    queue.append(friend)

        # return the dict
        return visited, len(visited)

# 3. Questions
# Question 1: To create 100 users with an average of 10 friends each, 
# how many times would you need to call add_friendship()? Why?
# Answer 1: 500 times, because each time you call add_friendship() it 
# creates a friendship for two keys, as it's bidirectional and thus creates 
# two edges.

# Question 2: If you create 1000 users with an average of 5 random friends 
# each, what percentage of other users will be in a particular user's extended 
# social network? What is the average degree of separation between a user 
# and those in his/her extended network?
# Answer 2: About 99.5%. There is more room for error in this percentage with
# a smaller sample size like 10, where connections tend to vary between 8-10.

# 4. Stretch Goals
# A way to improve the friendship distribution model would be to account for 
# the fact that once you have one mutual friend you'll have a greater likelihood
# of having another mutual friend after that. So maybe begin with clusters of 
# connections/friend groups. 




# Plan for get_all_social_paths()
# create a queue
# create a visited dict
# queue up user-id
# add visited[user_id] = user_id to dict

# while queue
    # current = queue.dequeue()
    # get current's edges 
    # for each edge
        # if edge not in dict
            # create new dict key visited[edge] = [visited[current] + edge]
            # queue edge up


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000, 5)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
