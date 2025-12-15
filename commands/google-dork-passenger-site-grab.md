---
data: 'passenger site:grab-attention.grabtaxi.com'
tags:
  - dorking
  - recon
type: command
output: >-
  Search results showing cached versions of the passenger.html page with partial
  auth_token exposed
executor: google
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:44.763Z'
id: 00ed43e6-23f1-41e5-bcc6-bc331cf719e4
verified: false
validated: true
submitted: true
---
# google-dork-passenger-site-grab

## Command

Search query:
```
passenger site:grab-attention.grabtaxi.com
```

## Description

This Google dork searches for pages containing the keyword 'passenger' limited to the grab-attention.grabtaxi.com domain, used to verify indexing and caching of sensitive endpoints exposing private Grab app data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| passenger | Keyword to match in page content | Yes |
| site:grab-attention.grabtaxi.com | Limits search to the specified domain | Yes |

## Examples

### Basic Usage

```
passenger site:grab-attention.grabtaxi.com
```

### Advanced Usage

Add filetype or other operators if needed, e.g., `passenger site:grab-attention.grabtaxi.com inurl:passenger.html`

## Expected Output

Search results including links to indexed pages, with cached snapshots showing partial auth_tokens and sensitive data like OTP pins from the passenger endpoint.

## Related

- [[commands/google-dork-allinurl-email-site-target]]
- [[procedures/Verify-Search-Engine-Indexing-with-Google-Dorks]]
