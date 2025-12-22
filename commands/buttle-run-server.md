---
data: ./node_modules/buttle/bin/buttle -p 8080
tags:
  - server
  - buttle
type: command
output: Listening on port 8080
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:30.828Z'
id: 90bbfc31-a1fd-49e8-b072-ca3b11096abf
verified: false
validated: true
submitted: true
---
# buttle-run-server

## Command

```bash
./node_modules/buttle/bin/buttle -p 8080
```

## Description

Starts the buttle static file server, serving the current directory with vulnerable HTML directory listings. The -p flag specifies the port for local hosting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-p` | Port to listen on | Yes |
| `8080` | Specific port number | Yes |

## Examples

### Basic Usage

```bash
./node_modules/buttle/bin/buttle -p 8080
```

### Advanced Usage

```bash
./node_modules/buttle/bin/buttle -p 3000
```

## Expected Output

Server listening on http://localhost:8080, ready to serve files.

## Related

- [[Related Procedure]]
