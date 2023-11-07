#!/usr/bin/node
//script that prints all the characters of a Star Wars movie:

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url + process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body).characters;

    for (const i in data) {
      request(data[i], (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
