# NoFollowBack

> A Python-based Instagram follower analyzer to identify non-reciprocal following relationships

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![BeautifulSoup4](https://img.shields.io/badge/BeautifulSoup4-4.x-green.svg)](https://www.crummy.com/software/BeautifulSoup/)

## Overview

NoFollowBack is a lightweight Python utility that processes Instagram HTML exports to perform follower analysis. By comparing your followers list against accounts you follow, it generates comprehensive reports identifying non-reciprocal relationships, enabling data-driven social media management decisions.

## Key Features

- **HTML Parsing** - Processes Instagram data exports using BeautifulSoup4
- **Set Analysis** - Efficient comparison using Python set operations
- **Report Generation** - Clean, formatted markdown output
- **Alphabetical Sorting** - Organized, readable results
- **Local Processing** - All operations performed locally for privacy

## Requirements

- Python 3.6+
- BeautifulSoup4

## Installation

1. Clone this repository:
```bash
git clone https://github.com/robertocarrascoso/NoFollowBack.git
cd NoFollowBack
```

2. Install dependencies:
```bash
pip install beautifulsoup4
```

## How to Get Your Instagram Data

### Method: Save HTML from Browser (Recommended - Fast & Easy)

1. **Log in to Instagram** on your web browser (Chrome, Firefox, etc.)

2. **Get Followers List:**
   - Go to your profile
   - Click on **"Followers"**
   - Wait for the list to load completely (scroll down if needed)
   - Right-click on the page → **"Save As"** or **"Save Page As"**
   - Save the file as: `seguidores.html`

3. **Get Following List:**
   - Go to your profile
   - Click on **"Following"**
   - Wait for the list to load completely (scroll down if needed)
   - Right-click on the page → **"Save As"** or **"Save Page As"**
   - Save the file as: `siguiendo.html`

4. **Important Notes:**
   - Make sure to scroll through the entire list before saving so all usernames are loaded
   - Save both files in the same folder as the script
   - The file names must be exactly: `seguidores.html` and `siguiendo.html`

## Usage

1. Place your Instagram export files in the same directory as the script:
   - `seguidores.html` (your followers)
   - `siguiendo.html` (accounts you follow)

2. Run the script:
```bash
python analyze_followers.py
```

3. Check the generated `not_following_back.md` file for results

## Output

The script generates a `not_following_back.md` file containing:
- Total count of users who don't follow you back
- Alphabetically sorted list of usernames

Example output:
```markdown
# Users I Follow But Don't Follow Me Back

Total: 42 users

- username1
- username2
- username3
...
```

## Algorithm

The script follows a straightforward data processing pipeline:

1. **HTML Parsing** - Utilizes BeautifulSoup4 to parse Instagram HTML exports
2. **Username Extraction** - Regular expressions identify and extract Instagram usernames from profile links
3. **Set Comparison** - Performs set difference operation (following - followers)
4. **Filtering** - Excludes Instagram system paths (explore, direct, reels, etc.)
5. **Report Generation** - Outputs formatted markdown with alphabetically sorted results

## Privacy & Security

This tool prioritizes user privacy and data security:

- **Local Processing** - All operations are performed locally on your machine
- **No External Communication** - Zero data transmission to external servers
- **No Authentication Required** - Instagram credentials are never requested or stored
- **Read-Only Operations** - Script only reads HTML files without modification
- **Open Source** - Full transparency of code operations

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## License

MIT License - feel free to use and modify as needed.

## Disclaimer

This tool is for personal use only. Make sure to comply with Instagram's Terms of Service. The author is not responsible for any actions taken based on the script's output.

## Author

**Roberto Carrascoso**  
GitHub: [@robertocarrascoso](https://github.com/robertocarrascoso)

## Acknowledgments

Built with Python and BeautifulSoup4 for efficient social media management.

---

**Note:** Instagram's HTML export format may change over time. If the script stops working, please open an issue.
