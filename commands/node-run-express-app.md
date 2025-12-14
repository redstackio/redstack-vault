---
id: cmd-node-run-app
data: node app.js
tags:
  - node
  - server-run
type: command
output: 'Console log: ''Example app listening on port 8888!'' and server startup'
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:20.486Z'
verified: false
validated: true
submitted: true
---
# node-run-express-app

## Command

```bash
node app.js
```

## Description

Executes the Node.js script app.js to start an Express server using metascraper for vulnerable scraping. Use to host the /scrap endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| app.js | Script file with Express and metascraper code | Yes |

## Examples

### Basic Usage

```bash
node app.js
```

### Advanced Usage

```bash
node app.js --port 8888
```
(If app.js supports flags)

## Expected Output

'Example app listening on port 8888!' followed by scrape logs on access.

## Related

- [[Related Procedure: Run-Express-App-to-Host-Scraping-Endpoint]]
