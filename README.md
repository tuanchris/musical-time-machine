# Time travel with Spotify Music

Find songs on the top 100 Billboard chart on any date, search those songs on Spotify, and create a personalize playlist.

## Instructions

### Clone the repository

```bash
git clone https://github.com/tuanchris/musical-time-machine.git
```

### Create environment (optional)

```bash
conda create -n musical-time-machine python=3.8
conda activate musical-time-machine
```

### Install required packages

```bash
pip install -r requirements.txt
```

### Create Spotify credentials

1. In order to create a playlist in Spotify you must have an account with Spotify. If you don't already have an account, you can sign up for a free one here: <http://spotify.com/signup/>

2. Once you've signed up/ signed in, go to the developer dashboard and create a new Spotify App:

    <https://developer.spotify.com/dashboard/>

3. Create a `.env` file with the following variables:

```env
SPOTIPY_CLIENT_ID=<Your Spotify Client ID>
SPOTIPY_CLIENT_SECRET=<Your Spotify Client Secret>
SPOTIPY_REDIRECT_URI='http://example.com'
```

### Run the app

```bash
python main.py
```

Enjoy the music :)
