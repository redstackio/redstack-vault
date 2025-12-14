---
id: cmd-open-password-window
data: 'window.open("https://imgur.com/account/settings/password ","_blank")'
tags:
  - window-open
  - settings-access
type: command
output: New window with settings page
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:13.016Z'
verified: false
validated: true
submitted: true
---
# Window Open Password Settings

## Command

```javascript
window.open("https://imgur.com/account/settings/password ","_blank")
```

## Description

Opens Imgur password settings in new tab for form access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | Settings URL | Yes |
| target | _blank | Yes |

## Examples

### Basic Usage

```javascript
// From XSS
```

## Expected Output

New tab loads page.

## Related

- [[Related Procedure: Perform Account Takeover]]
