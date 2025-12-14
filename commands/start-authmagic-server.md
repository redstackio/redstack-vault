---
id: cmd-736522-authmagic-start
data: authmagic
tags:
  - server
  - start
type: command
output: 'Server running on http://localhost:3000'
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:10.826Z'
verified: false
validated: true
submitted: true
---
# start-authmagic-server

## Command

```bash
authmagic
```

## Description

Starts the authmagic example server, exposing the vulnerable /token endpoint on localhost:3000 for authentication testing.

## Parameters

None.

## Examples

### Basic Usage

```bash
authmagic
```

### Advanced Usage

```bash
authmagic --port 3001
```

## Expected Output

Console logs: 'Server running on http://localhost:3000'. App accessible in browser.

## Related

- [[procedures/Perform-Initial-User-Authentication]]
- [[procedures/Initialize-and-Install-Authmagic-Example-App]]
