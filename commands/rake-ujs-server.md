---
data: 'rake ujs:server'
tags:
  - rake
  - server
type: command
executor: bash
platforms:
  - Linux
id: 1dcfda7e-56c0-48c0-8e07-002ed61cd36e
created_at: '2025-12-13T09:01:16.864Z'
updated_at: '2025-12-13T09:01:16.864Z'
verified: false
validated: true
submitted: true
---
# rake-ujs-server

## Command

```bash
rake ujs:server
```

## Description

Starts the UJS test server using Rake, launching Puma on port 4567.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `ujs:server` | Rake task to run the server | Yes |

## Examples

### Basic Usage

```bash
rake ujs:server
```

## Expected Output

Server startup messages, e.g., Puma starting... Listening on tcp://127.0.0.1:4567.

## Related

- [[procedures/Start-UJS-Test-Server]]
- [[tools/rake]]
- [[tools/Puma]]
