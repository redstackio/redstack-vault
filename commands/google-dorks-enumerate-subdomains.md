---
id: a5cd7333-6dda-4dfc-be29-33cdccee3dee
name: google-dorks-enumerate-subdomains
type: command
executor: browser
data: 'site:*.domain.com -www'
output: null
created_at: '2023-04-06T03:56:25.425856+00:00'
updated_at: '2023-04-10T20:25:37.761328+00:00'
platforms:
  - Web
tags:
  - reconnaissance
  - subdomain-enumeration
verified: true
validated: true
---

# google-dorks-enumerate-subdomains

## Command

Enter this query directly into the Google search bar:

```text
site:*.domain.com -www
```

## Description

This Google Dork enumerates first-level subdomains of a target domain by searching for indexed pages, excluding the 'www' subdomain to avoid noise. Use during passive reconnaissance to map the target's web footprint without direct interaction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| domain.com | The target domain (replace with actual, e.g., example.com) | Yes |
| -www | Excludes results from www subdomain | No (but recommended for focus) |

## Examples

### Basic Usage

```text
site:*.example.com -www
```

Searches for subdomains like 'api.example.com' or 'mail.example.com'.

### Advanced Usage

Combine with other operators:

```text
site:*.example.com -www -inurl:(login | admin)
```

Excludes common paths to refine results.

## Expected Output

Google returns a list of search results with URLs grouped by subdomain, e.g.:

- About 1,230 results (0.45 seconds)
- mail.example.com/path1
- api.example.com/api/docs

Extract unique subdomains manually or via browser dev tools.

## Related

- [[procedures/Subdomain-Enumeration-with-Google-Dorks]]
- [[commands/google-dorks-enumerate-multi-level-subdomains]]
