---
data: rails -v
tags:
  - setup
  - verification
type: command
output: 'Rails version information, e.g., Rails 6.1.4'
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:27.446Z'
id: c236a53b-d68f-4d3d-9432-70b4bbe94f62
verified: false
validated: true
submitted: true
---
# rails-version-check

## Command

```bash
rails -v
```

## Description

Verifies the Rails version before app creation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -v | Version flag | Yes |

## Examples

### Basic Usage

```bash
rails -v
```

## Expected Output

Rails version details.

## Related

- [[commands/ruby-version-check]]
