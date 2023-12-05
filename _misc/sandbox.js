// # spotipy
// # current_user_saved_tracks_add

// var Spotify = require('spotify-web-api-js');
// var s = new Spotify();
// var spotifyApi = new SpotifyWebApi();

const express = require('express');
const CLIENT_ID = '1accfa9dc0004fedb5f3e8c6f35cab0d';
const CLIENT_SECRET = '43d193b74832409893a585a1feba5cfd';
const ACESS_TOKEN = 'BQDyd1JSKLkxuSOibg2RCvQ141F4QZNpEjaLuQIXcs1CIVGzBS5jSjbBpR_XBedg7uNB8xN2fU2Ng4c23rFslqQ5Er3g5TqtK7TTe8vYIfxiFi8BjwQ'

// Manual Authorization for Access Token
// curl - X POST "https://accounts.spotify.com/api/token" - H "Content-Type: application/x-www-form-urlencoded" - d "grant_type=client_credentials&client_id=1accfa9dc0004fedb5f3e8c6f35cab0d&client_secret=43d193b74832409893a585a1feba5cfd"
