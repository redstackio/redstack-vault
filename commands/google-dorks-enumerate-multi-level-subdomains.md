---
id: 5d2517d7-a95d-4f85-8a0b-7486c9a678a7
name: google-dorks-enumerate-multi-level-subdomains
type: command
executor: browser
data: 'site:*.*.domain.com'
output: null
created_at: '2023-04-06T03:56:25.426208+00:00'
updated_at: '2023-04-10T20:25:37.761328+00:00'
platforms:
  - Web
tags:
  - reconnaissance
  - subdomain-enumeration
verified: true
validated: true
---

# google-dorks-enumerate-multi-level-subdomains

## Command

Enter this query directly into the Google search bar:

```text
site:*.*.domain.com
```

## Description

This Google Dork discovers multi-level (nested) subdomains by searching for pages under structures like 'dev.api.domain.com'. Ideal for uncovering staging or internal environments during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| domain.com | The target domain (replace with actual) | Yes |

## Examples

### Basic Usage

```text
site:*.*.example.com
```

Returns results from subdomains like 'staging.dev.example.com'.

### Advanced Usage

Limit to specific paths:

```text
site:*.*.example.com inurl:admin
```

Focuses on admin areas in nested subdomains.

## Expected Output

Search results showing URLs with multi-level subdomains, e.g.:

- About 500 results
- test.sub.example.com/test
- dev.api.example.com/docs

Manually list unique nested subdomains.

## Related

- [[procedures/Subdomain-Enumeration-with-Google-Dorks]]
- [[commands/google-dorks-enumerate-subdomains]]
