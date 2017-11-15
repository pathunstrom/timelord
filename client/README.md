# Timelord Client

A terminal client for Timelord.

## API

## Design

Client process:

1. Parse command.
2. Ping server.
3. On failed ping, launch server.
4. Ping until success.
5. Send command.
6. Print data.
