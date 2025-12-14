---
id: cmd-feature-enable-bulk-import
data: '::Feature.enable(:bulk_import_projects)'
tags:
  - feature-flag
  - gitlab
type: command
output: Feature enabled confirmation
executor: ruby
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.593Z'
verified: false
validated: true
submitted: true
---
# feature-enable-bulk-import

## Command

```ruby
::Feature.enable(:bulk_import_projects)
```

## Description

Enables the bulk_import_projects feature flag in GitLab's Rails console, activating the vulnerable BulkImports functionality for project imports.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ::Feature.enable | Method to toggle flag | Yes |
| :bulk_import_projects | Specific flag name | Yes |

## Examples

### Basic Usage

```ruby
::Feature.enable(:bulk_import_projects)
```

### Advanced Usage

Check status: `::Feature.enabled?(:bulk_import_projects)` returns true.

## Expected Output

No output or simple confirmation; flag is now active.

## Related

- [[commands/gitlab-rails-console]]
