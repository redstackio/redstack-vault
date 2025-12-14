---
id: cmd-precompile-assets
data: 'RUN RAILS_ENV=production rails assets:precompile'
tags:
  - assets
  - build
type: command
output: Precompilation logs
executor: bash
platforms:
  - Docker
  - Ruby on Rails
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:25.729Z'
verified: false
validated: true
submitted: true
---
# rails-precompile-assets

## Command

```dockerfile
RUN RAILS_ENV=production rails assets:precompile
```

## Description

Precompiles Rails assets in production mode during Docker build.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| RAILS_ENV=production | Set environment | Yes |

## Examples

### Basic Usage

In Dockerfile as above.

## Expected Output

Asset precompilation completed.

## Related

- [[commands/rails-start-server]]
- [[procedures/Build-Sample-Vulnerable-Rails-Application-with-Docker]]
