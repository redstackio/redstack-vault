---
data: ./bin/rails server -b 0.0.0.0 -e production
tags:
  - rails
  - server
type: command
output: Server startup logs
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:16.291Z'
id: 9641ba35-9f9e-4ed0-bed4-0545bc22cfb1
verified: false
validated: true
submitted: true
---
# rails-server-production

## Command

```bash
./bin/rails server -b 0.0.0.0 -e production
```

## Description

Starts the Rails server in production mode bound to all interfaces.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -b | Bind address 0.0.0.0 | Yes |
| -e | Environment production | Yes |

## Examples

### Basic Usage

```bash
./bin/rails server -b 0.0.0.0 -e production
```

## Expected Output

Server startup logs, listening on 3000.

## Related

- [[commands/docker-run-railspoc]]
