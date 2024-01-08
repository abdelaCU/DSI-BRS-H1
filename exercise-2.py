import requests
import json

# GitHub API endpoint for searching repositories
url_1 = 'https://api.github.com/search/repositories'
url_2 = 'https://api.github.com/search/users'

# Search query parameters for the top 20 most starred repositories
params_1 = {'q': 'stars:>1', 'sort': 'stars', 'order': 'desc'}

# Search query parametries for the top 20 most followed users
params_2 = {'q': 'followers:>1', 'sort': 'followers', 'order': 'desc'}


# Send request to GitHub
r1 = requests.get(url_1, params=params_1)
r2 = requests.get(url_2, params=params_2)

# Parse the JSON data
json_data1 = r1.json()
json_data2 = r2.json()

# Print the names of the top 20 most starred repositories
print("=======================================================================================")
print("Top 20 Most Starred Repositories:")
print("=======================================================================================")
for index, repo in enumerate(json_data1['items'][:20]):
    print(f"{index + 1}. {repo['full_name']} - Stars: {repo['stargazers_count']}")
print("=======================================================================================\n")    
    

print("========================================================================================")
# Print the names of the top 20 most followed users
print("Top 20 Most Followed Users:")
print("=========================================================================================")
for index, user in enumerate(json_data2.get('items', [])[:20]):
   # Access 'login' and 'followers' directly
   print(f"{index + 1}. {user.get('login', 'N/A')}")
    