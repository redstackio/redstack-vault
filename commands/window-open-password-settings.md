---
id: cmd-window-open-settings
data: 'window.open("https://imgur.com/account/settings/password","_blank")'
tags:
  - window
  - settings
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:06.798Z'
verified: false
validated: true
submitted: true
---
# window-open-password-settings

## Command

```javascript
window.open("https://imgur.com/account/settings/password","_blank")
```

## Description

Opens a new blank window to the Imgur password settings page for form access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | "https://imgur.com/account/settings/password" | Yes |
| target | "_blank" | Yes |

## Examples

### Basic Usage

```javascript
window.open("https://imgur.com/account/settings/password","_blank")
```

## Expected Output

New window loads the password change form.

## Related

- [[procedures/Perform-Account-Takeover-via-Form-Manipulation]]
