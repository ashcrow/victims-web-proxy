victims-web-proxy
=================

A proxy server application for the victi.ms web service

## Usage Scenarios

### Scenario One
* You have a multiple development enviornments behind the firewall using the victims-enforcer plugin for maven.
* You do not want to download updates from victi.ms server for each of these environments seperately.

In these scenarios, you can deploy the victims-web-proxy on a node on the network perimeter that on scheduled intervals check for and cache any updates from the victi.ms web service.

## Database Backend
THe proxy server uses an embedded nosql store to store each individual victims records received from the server for update and remove endpoints. The database choice is [CodernityDB](http://labs.codernity.com/codernitydb/). This is a pure python embedded nosql solution which allows for a no mess, no fuzz deployment.
