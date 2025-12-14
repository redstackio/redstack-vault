---
data: gau wakatime.com > historical_urls.txt
tags:
  - reconnaissance
type: command
output: A list of historical URLs saved to historical_urls.txt
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.412Z'
id: 845160c5-5e38-4cbe-9694-ab0962e4eb20
verified: false
validated: true
submitted: true
---
# gau-fetch-historical-urls

## Command

```bash
gau wakatime.com > historical_urls.txt
```

## Description

This command uses the gau tool to fetch known URLs for the specified domain from public archives like the Wayback Machine and AlienVault, redirecting output to a file for review. It is useful for passive reconnaissance to uncover exposed endpoints or secrets.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `wakatime.com` | Target domain to query | Yes |
| `> historical_urls.txt` | Redirect output to file | No (but recommended for large outputs) |

## Examples

### Basic Usage

```bash
gau example.com
```

### Advanced Usage

```bash
gau wakatime.com | grep api_key
```

Pipes output directly to grep for filtering sensitive parameters.

## Expected Output

A plain text file or stdout listing URLs, e.g.,
https://wakatime.com/api/v1/users/current/summaries?start=today&end=today&api_key=waka_edf47c40-cabf-46e7-9f88-f1b44f00431f

## Related

- [[Related Procedure: Discover-Exposed-URLs-with-Gau]]
