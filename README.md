# SMS2

# Sending SMS from Web

Web app that uses Nexmo API to send text messages. The The API is written in Python. It can be ran using Flask, a Python web framework.
## Running The Demo Locally
1. Install dependencies

$ npm install

2. Set up a config.py with Your Credentials

Sign up at Nexmo to get your own API keys and a virtual number.

Create config.py in /server. The file should include the credentials.

module.exports = {
  api_key: 'f321a...',
  api_secret: '18e9aad...',
  number: '14155551234'
};

Go to http://localhost and send text messages.
## 
Install Flask
```http
pip install Flask
```
2. Navigate to PWD
2. run server.py and lauch the Web app locally
# Project Title

## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_send` | `string` | **Required**. Your API key and secret |

#### Get item

```http
  GET /api/items/${id}
```
Takes a valid Phone number and returns a status code for error or completion.



| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Num`      | `string` | **Required**. Number to be sent |

###

