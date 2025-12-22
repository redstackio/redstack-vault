---
id: 65761bdb-8ecb-438a-b600-63f0b4f8ca5f
name: google-dorks-search-urls-with-ampersand
type: command
executor: browser
data: 'site:domain.com inurl:''&'''
output: null
created_at: '2023-04-06T03:56:25.425986+00:00'
updated_at: '2023-04-10T20:25:37.761328+00:00'
platforms:
  - Web
tags:
  - reconnaissance
  - vulnerability-scanning
verified: true
validated: true
---

# google-dorks-search-urls-with-ampersand

## Command

Enter this query directly into the Google search bar:

```text
site:domain.com inurl:'&'
```

## Description

This Google Dork finds URLs on the target domain containing ampersands ('&'), which often indicate query parameters that could be vulnerable to injection attacks or parameter pollution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| domain.com | The target domain | Yes |
| inurl:'&' | Searches for '&' in URL path | Yes |

## Examples

### Basic Usage

```text
site:example.com inurl:'&'
```

Identifies dynamic URLs.

### Advanced Usage

With specific params:

```text
site:example.com inurl:'&id='
```

Targets ID parameters.

## Expected Output

URLs like:

- example.com/search?q=term&id=123

Inspect for manipulation opportunities.

## Related

- [[procedures/Subdomain-Enumeration-with-Google-Dorks]]
- [[commands/google-dorks-search-admin-login-urls]]
