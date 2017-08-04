# Twitter Wipe
Deletes all your tweets, retweets and favorites.

# Usage
1. Make sure your have Python 2 installed by running this in console:

        python --version

2. Install required python library:
    
        pip install python-twitter
    
3. Download twitterwipe script:

        git clone https://github.com/brunocassol/twitterwipe
        cd twitterwipe
    
4. Create a temporary twitter app:

- Open https://apps.twitter.com
- Sign up with your account.
- Create a new app. The details can be bogus, your app will be private.
- Make sure the app has read/write permission and click [Regenerate My Access Token and Token Secret] button. **This step is easy to miss**.

5. Edit the downloaded twitterwipe.py file:

- Open `twitterwipe.py` with your favorite text editor

        code twitterwipe.py

- Copy these values from your created Twitter app and paste into `INSERT_HERE` placeholders in twitterwipe.py:

        consumer_key='INSERT_HERE',
        consumer_secret='INSERT_HERE',
        access_token_key='INSERT_HERE',
        access_token_secret='INSERT_HERE'

6. Run the script:

        python twitterwipe.py

# Credits
Based on: https://github.com/olivierthereaux/oldtweets/blob/master/oldtweets.py
