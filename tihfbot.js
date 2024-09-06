import WebSocket from "ws";

//Grab bot user id
const BOT_USER_ID = '';
//Grab O Authentication token. Needs scopes user:bot, user:read:chat, user:write:chat
const OAUTHTOKEN = '';
//Grab Client ID
const CLIENT_ID = '';

//Grab chat channel user id
const chat_channel_user_id = '';

//Used to start the websocket client
const EVENTSUB_WEBSOCKET_URL = 'wss://eventsub.wss.twitch.tv/ws';

var WebSocketSessionID;

(async () => {
    
    //Verifies if authentication is valid before proceeding with the program
    await getAuth();

    //If verification is correct, start the client.
    const websocketClient = startWebSocketClient();

}) ();

//Program will continue to run unless closed forcefully. TODO: Write a function for the CLI that closes the program.

