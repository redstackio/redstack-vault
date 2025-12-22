---
data: '::Feature.enable(:bulk_import_projects)'
tags:
  - gitlab
type: command
executor: ruby
platforms:
  - Linux
id: 1bccc9d3-212b-47f4-92dc-3e7ac22d2c5e
created_at: '2025-12-11T03:48:06.003Z'
updated_at: '2025-12-11T03:48:06.003Z'
verified: false
validated: true
submitted: true
---
# enable-feature-flag

## Command

```ruby
::Feature.enable(:bulk_import_projects)
```

## Description

Enables a specific feature flag in GitLab Rails console.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `:bulk_import_projects` | Feature name | Yes |

## Examples

### Basic Usage

```ruby
::Feature.enable(:bulk_import_projects)
```

## Expected Output

true

## Related

- [[commands/gitlab-rails-console]]
