---
id: uuid-feature-enable
data: 'Feature.enable(:vue_issuables_list)'
tags:
  - feature-flag
  - ruby
type: command
output: 'Confirmation that the feature is enabled (e.g., true or success message)'
executor: ruby
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:24.481Z'
verified: false
validated: true
submitted: true
---
# feature-enable-vue-issuables-list

## Command

```ruby
Feature.enable(:vue_issuables_list)
```

## Description

Enables the specified feature flag in GitLab's feature management system via Rails console, activating the Vue-based issue list.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `:vue_issuables_list` | Name of the feature flag | Yes |

## Examples

### Basic Usage

```ruby
Feature.enable(:vue_issuables_list)
```

### Advanced Usage

Disable instead:

```ruby
Feature.disable(:vue_issuables_list)
```

## Expected Output

Returns true if enabled successfully.

## Related

- [[Related Procedure: Enable-Vue-Issuables-List-Feature-Flag]]
