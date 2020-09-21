# PokerGames
 A simple program that can take two 5-card poker hands, classify each hand, and determine which hand would win

<img alt="Run" src="./assets/demo2.png">
<img alt="Unit Test" src="./assets/demo1.png">


## Technologies
- [Python](https://www.python.org/downloads/release/python-380/)
- [API](http://deckofcardsapi.com/)
- Might need to install these python libraries "requests", "collections", "unittest" for Python 3 (these are should be included in the standard library).

## Getting Started
Clone this repository
```
$ git clone git@github.com:cxchan1/netbook.git
```
Install node modules, [Yarn](https://yarnpkg.com/en/) is highly recommended.
```
$ cd netbook/netbook-client/ && yarn install
```
Run netbook front end:
```
$ yarn start
```
Run netbook server side, [Golang](https://golang.org/doc/install):
```
$ cd netbook/netbook-server/ && go run main.go
```
## Hints:
- Make sure you start the front end first before you run the server side. Otherwise, front-end and back-end won't talk to each other because of Node.js (localhost only)
- (WARNING) Currently, there is no database on the server side yet so right now there is no way to save your data on the application.
