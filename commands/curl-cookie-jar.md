---
data: curl --cookie-jar a google.com
tags:
  - exploitation
  - libcurl
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:24:19.211Z'
id: 659375eb-90ce-475c-9f5c-1c1085232cfa
verified: false
validated: true
submitted: true
---
# curl-cookie-jar

## Command

```bash
curl --cookie-jar a google.com
```

## Description

Fetches the specified URL (google.com) using curl and saves any received cookies to the file 'a' via libcurl's cookie jar feature, triggering the vulnerable fopen path in the presence of a TOCTOU race.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --cookie-jar | Target file path for saving cookies (e.g., a) | Yes |
| google.com | URL to fetch and extract cookies from | Yes |

## Examples

### Basic Usage

```bash
curl --cookie-jar a google.com
```

### With Verbose Output

```bash
curl -v --cookie-jar a google.com
```

## Expected Output

HTTP response from the server (e.g., HTML content); cookies written to 'a' or followed symlink (e.g., '# Netscape HTTP Cookie File' header). In normal cases, creates/overwrites 'a' as a regular file; in exploit, writes to unintended target.

## Related

- [[commands/ls-long]]
- [[procedures/Trigger-libcurl-Vulnerability-with-Cookie-Jar]]
