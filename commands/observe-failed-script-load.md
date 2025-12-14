---
data: >-
  Inspect network tab for
  http://joaxcar.com/assets/webpack/hello.4948f350.chunk.js
tags:
  - recon
  - network
type: command
output: 404 errors on redirected requests
executor: browser
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:19.808Z'
id: 397415b8-d070-43a0-823d-8daae2f73183
verified: false
validated: true
submitted: true
---
# observe-failed-script-load

## Command

Inspect DevTools Network tab after reload for failing URLs like:

```url
http://joaxcar.com/assets/webpack/hello.4948f350.chunk.js
```

## Description

Observes failed script imports in browser DevTools to validate <base> tag redirection in the GitLab XSS exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| path | Specific asset path to monitor | No |

## Examples

### Basic Usage

Open F12 > Network > Reload page > Filter 'JS'.

### Advanced Usage

Monitor for wiki-specific: https://joaxcar.com/assets/webpack/top_nav.c9763726.chunk.js

## Expected Output

List of 404s or failed requests to attacker domain mimicking GitLab paths.

## Related

- [[commands/configure-htaccess-rewrite]]
- [[procedures/Observe-Failed-Script-Loads-in-DevTools]]
