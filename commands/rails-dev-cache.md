---
data: 'rails dev:cache'
tags:
  - caching
type: command
output: config/environments/development.rb updated with page_cache_directory
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.417Z'
id: 3bbd99c8-7899-4544-a91f-85e186f34541
verified: false
validated: true
submitted: true
---
# rails-dev-cache

## Command

```bash
rails dev:cache
```

## Description

Enables page caching in development environment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Targets development.rb | No |

## Examples

### Basic Usage

```bash
rails dev:cache
```

## Expected Output

Caching config added.

## Related

- [[commands/rails-server-start]]
