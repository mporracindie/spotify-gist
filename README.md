# spotify-gist
🎧 Get your last weeks listening report from Spotify in a GitHub Gist.

<p align='center'>
  <img src="https://github.com/mporracindie/spotify-gist/blob/main/spotify-gist-preview.png">
  <h3 align="center">spotify-gist</h3>
  <p align="center">Update a gist to contain your monthly plays on Spotify</p>
</p>

---
> 📌✨ For more pinned-gist projects like this one, check out: https://github.com/matchai/awesome-pinned-gists

## ✨ Inspiration
This code was heavily inspired by [@jacc music-box](https://github.com/jacc/music-box).

## 🎒 Prep Work
1. Create a new public GitHub Gist (https://gist.github.com/)
2. Create a Spotify Application (https://developer.spotify.com/dashboard/)
  - Add your own user to the app under `users and access`
  - Add `http://localhost` as valoid Redirect URIs under `edit settings`
3. Copy the `Client ID` and `Client Secret`
4. Create a github personal access token [here](https://github.com/settings/tokens) with gist permissions 

## 🖥 Project Setup
1. Download this repo (or just copy the contents of [this file](https://github.com/mporracindie/spotify-gist/blob/main/gist_spotify.py)
2. Run `pip install spotipy, PyGithub`
3. Export all the needed env variables and run the file

## 🤫 Environment Secrets
- **GIST_ID:** The ID portion from your gist url `https://gist.github.com/<github username>/`**`6d5f84419863089a167387da62dd7081`**.
- **GITHUB_ACCESS_TOKEN:** The GitHub token generated above.
- **SPOTIPY_CLIENT_ID:** The client id you got while creating the Spotify app.
- **SPOTIPY_CLIENT_SECRET:** The client secret you got while creating the Spotify app.
