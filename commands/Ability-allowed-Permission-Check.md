---
data: >-
  Ability.allowed?(User.find(2), :delete_metrics_dashboard_annotation,
  Group.find(7))
tags:
  - ruby
  - permissions
type: command
output: 'true'
executor: ruby
platforms:
  - GitLab
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:20.409Z'
id: 6aecf6c2-a9ac-47e8-aedd-b140b8c31579
verified: false
validated: true
submitted: true
---
# Ability-allowed-Permission-Check

## Command

```ruby
Ability.allowed?(User.find(2), :delete_metrics_dashboard_annotation, Group.find(7))
```

## Description

IRB command to verify that a developer user has permission to 'delete' on a non-annotation object like a group, highlighting the broad permission check in DeleteService.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| User.find(2) | Developer user object (ID 2) | Yes |
| :delete_metrics_dashboard_annotation | Permission action | Yes |
| Group.find(7) | Target group object (ID 7) | Yes |

## Examples

### Basic Usage

```ruby
Ability.allowed?(User.find(2), :delete_metrics_dashboard_annotation, Group.find(7))
```

### Advanced Usage

Test on project:

```ruby
Ability.allowed?(User.find(2), :delete_metrics_dashboard_annotation, Project.find(5))
```

## Expected Output

true, indicating permission granted without type check.

## Related

- [[procedures/Exploit-deleteAnnotation-on-Group]]
- [[tools/IRB]]
