---
data: 'RAILS_ENV=production rails assets:precompile'
tags:
  - rails
  - production
type: command
output: Asset precompilation output
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:16.301Z'
id: d2a9fd58-5f6f-4c4a-8d0e-6fdb98c0f552
verified: false
validated: true
submitted: true
---
# rails-assets-precompile

## Command

```bash
RAILS_ENV=production rails assets:precompile
```

## Description

Precompiles assets for production environment in Rails.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| RAILS_ENV | Set to production | Yes |

## Examples

### Basic Usage

```bash
RAILS_ENV=production rails assets:precompile
```

## Expected Output

Asset precompilation output.

## Related

- [[commands/rails-server-production]]
