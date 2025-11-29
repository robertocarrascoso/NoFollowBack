from bs4 import BeautifulSoup
import re

# Read and parse seguidores.html (followers)
print("Reading seguidores.html...")
with open('seguidores.html', 'r', encoding='utf-8') as f:
    followers_html = f.read()

# Read and parse siguiendo.html (following)
print("Reading siguiendo.html...")
with open('siguiendo.html', 'r', encoding='utf-8') as f:
    following_html = f.read()

# Parse HTML
soup_followers = BeautifulSoup(followers_html, 'html.parser')
soup_following = BeautifulSoup(following_html, 'html.parser')

# Extract usernames (href links contain /username/)
def extract_users(soup):
    users = set()
    # Find all links containing usernames
    for link in soup.find_all('a', href=True):
        href = link['href']
        # Instagram profiles have format /username/ or https://www.instagram.com/username/
        match = re.search(r'instagram\.com/([^/]+)/?', href)
        if not match:
            match = re.search(r'^/([^/]+)/?$', href)

        if match:
            username = match.group(1)
            # Filter out non-user links (explore, direct, etc)
            if username not in ['explore', 'direct', 'reels', 'stories', 'accounts', '']:
                users.add(username)

    return users

print("Extracting users from followers...")
followers = extract_users(soup_followers)
print(f"Followers found: {len(followers)}")

print("Extracting users from following...")
following = extract_users(soup_following)
print(f"Following found: {len(following)}")

# Find people you follow but don't follow you back
not_following_back = following - followers
print(f"Users you follow but don't follow you back: {len(not_following_back)}")

# Sort alphabetically
not_following_back_list = sorted(not_following_back)

# Create markdown file
print("Creating not_following_back.md file...")
with open('not_following_back.md', 'w', encoding='utf-8') as f:
    f.write('# Users I Follow But Don\'t Follow Me Back\n\n')
    f.write(f'Total: {len(not_following_back_list)} users\n\n')
    for user in not_following_back_list:
        f.write(f'- {user}\n')

print("Process completed! File not_following_back.md created.")