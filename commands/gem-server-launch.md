---
id: cmd-uuid-3
data: gem server
tags:
  - gem-server
type: command
output: null
executor: bash
platforms:
  - Ruby
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:46.990Z'
verified: false
validated: true
submitted: true
---
# gem-server-launch

## Command

```bash
gem server
```

## Description

Starts the built-in RubyGems HTTP server to browse and view documentation for installed gems, rendering metadata like homepage links that can trigger stored XSS if malicious.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | Uses default port 8808; optional -p for port | No |

## Examples

### Basic Usage

```bash
gem server
```

### Advanced Usage

```bash
gem server -p 8080
```

## Expected Output

Server running at http://0.0.0.0:8808

The server listens and serves the gem index until stopped (Ctrl+C).

## Related

- [[procedures/Launch-RubyGems-Server]]
- [[commands/gem-install-securitytest]]
