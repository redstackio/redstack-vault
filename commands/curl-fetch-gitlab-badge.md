---
data: >-
  curl -s https://example.gitlab.com/test/cibadges/badges/master/pipeline.svg >
  pipeline.svg
tags:
  - recon
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.654Z'
id: 4d6f6d13-16ed-4fb6-ab80-aecf0567c627
verified: false
validated: true
submitted: true
---
# curl-fetch-gitlab-badge

## Command

```bash
curl -s https://example.gitlab.com/test/cibadges/badges/master/pipeline.svg > pipeline.svg
```

## Description

This command uses curl to silently fetch a GitLab pipeline badge SVG from a restricted project endpoint and saves it to a file for analysis, demonstrating unauthorized access to build status information.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, suppresses progress meter | Yes |
| `URL` | The badge endpoint URL (e.g., /badges/<branch>/pipeline.svg) | Yes |
| `> filename` | Redirect output to file | Yes |

## Examples

### Basic Usage

```bash
curl -s https://example.gitlab.com/test/cibadges/badges/master/pipeline.svg > pipeline.svg
```

### Advanced Usage

```bash
curl -s -H "User-Agent: Mozilla/5.0" https://example.gitlab.com/test/cibadges/badges/master/coverage.svg | grep -o 'coverage: [0-9.]*%'
```

## Expected Output

An SVG file containing embedded text like '<text class="status success">passed</text>' or coverage details, indicating successful disclosure without authentication.

## Related

- [[Related Procedure: Access-GitLab-Badge-Endpoint-Unauthorized]]
