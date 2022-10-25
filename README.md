# nft_info

Installation:
  1. Download the repository as you wish, suggested way -> git clone https://github.com/tuchaVshortah/nft_info.git
  2. cd into the directory where repository is located
  3. Install requirements

Usage:
  1. Start a local postgresql server (port 5432)
  2. cd into the directory where repository is located
  3. In the db.py file edit the POSTGRES_USER and POSTGRES_PASSWORD fields as you need (default values postgres:root)
  4. In your terminal run: python -u app.py
  5. Open a web browser
  6. Navigate to http://localhost:5000/
  7. At the search field on top enter your search, then click on the "Search" button on the right
  8. In the displayed menu select a search option (currently only one is supported -> "Search for a NFT token")
  9. Various details about found NFT tokens will be displayed
  10. You can hover your mouse on thumbnails -> this will show you a mini description of the token

Attention! Data is automatically saved in the database

Examples:
![Screenshot_20221025_165434](https://user-images.githubusercontent.com/71591558/197755310-1720ce80-509a-43b1-b5c5-9704597ba977.png)
![Screenshot_20221025_165615](https://user-images.githubusercontent.com/71591558/197755539-209eebfb-6c8d-42de-b606-7d5b70c39ad2.png)
![Screenshot_20221025_165718](https://user-images.githubusercontent.com/71591558/197755723-97bbb402-467c-476b-a396-050fae150166.png)
