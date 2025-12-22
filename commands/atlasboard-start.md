---
data: atlasboard start
tags:
  - server
  - start
  - atlasboard
type: command
output: 'Server starts, typically on localhost:3000, with logs indicating readiness'
executor: bash
platforms:
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:30.334Z'
id: be595c1c-01ce-4e3b-8149-ed80a74754ac
verified: false
validated: true
submitted: true
---
# atlasboard-start

## Command

```bash
atlasboard start
```

## Description

Launches the Atlasboard server to host and serve the configured dashboard.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `start` | Subcommand to run the server | Yes |

## Examples

### Basic Usage

```bash
atlasboard start
```

### Advanced Usage

```bash
atlasboard start --port 8080
```

## Expected Output

Logs like 'Atlasboard server listening on port 3000'.

## Related

- [[commands/node-start-js]]
- [[procedures/Launch-Dashboard-and-Trigger-XSS]]
