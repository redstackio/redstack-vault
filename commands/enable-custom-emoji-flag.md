---
data: 'Feature.enable(:custom_emoji)'
tags:
  - gitlab
  - feature-flag
type: command
output: 'true'
executor: ruby
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:03.655Z'
id: fc82c3de-9dbd-4d21-97c1-1b9ec6af3118
verified: false
validated: true
submitted: true
---
# enable-custom-emoji-flag

## Command

```ruby
Feature.enable(:custom_emoji)
```

## Description

This Ruby command, executed in the GitLab Rails console, enables the custom emoji feature flag, activating the vulnerable functionality for XSS exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `:custom_emoji` | The symbol for the custom emoji feature flag | Yes |

## Examples

### Basic Usage

```ruby
Feature.enable(:custom_emoji)
```

### Advanced Usage

In console: First run `gitlab-rails console`, then the command.

## Expected Output

`=> true` - Indicates successful enablement of the flag.

## Related

- [[Related Procedure: Enable-Custom-Emoji-Feature-Flag-in-GitLab]]
