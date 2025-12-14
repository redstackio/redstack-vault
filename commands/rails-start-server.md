---
id: cmd-rails-start
data: 'CMD ["./bin/rails", "server", "-b", "0.0.0.0", "-e", "production"]'
tags:
  - server
  - start
type: command
output: Server startup
executor: bash
platforms:
  - Docker
  - Ruby on Rails
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:25.725Z'
verified: false
validated: true
submitted: true
---
# rails-start-server

## Command

```dockerfile
CMD ["./bin/rails", "server", "-b", "0.0.0.0", "-e", "production"]
```

## Description

Default command to start Rails server in production, bound to all interfaces.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -b 0.0.0.0 | Bind address | Yes |
| -e production | Environment | Yes |

## Examples

### Basic Usage

As CMD in Dockerfile.

## Expected Output

Puma starting in single mode...

## Related

- [[commands/rails-precompile-assets]]
- [[procedures/Build-Sample-Vulnerable-Rails-Application-with-Docker]]
