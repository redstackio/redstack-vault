---
data: bin/rails routes
tags:
  - setup
  - routes
type: command
output: >-
  Shows Active Storage routes like
  /rails/active_storage/disk/:encoded_key/*filename
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.335Z'
id: 6289eb33-0532-40c9-a19e-74d94ea517b8
verified: false
validated: true
submitted: true
---
# list-rails-routes

## Command

```bash
bin/rails routes
```

## Description

List all routes in the Rails application to confirm Active Storage endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Standard list | No |

## Examples

### Basic Usage

```bash
bin/rails routes
```

## Expected Output

Shows Active Storage routes like /rails/active_storage/disk/:encoded_key/*filename

## Related

- [[commands/bundle-install]]
