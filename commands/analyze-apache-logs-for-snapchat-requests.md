---
data: cat /var/log/apache2/access.log | grep -v server-status | grep snapchat -i
tags:
  - logs
  - analysis
  - apache
type: command
output: >-
  Log entries showing GET requests from Snapchat apps, e.g., '23.235.39.33 - -
  [02/Aug/2016:18:28:25 +0000] "GET
  /bq/story_blob?story_id=fRaYutXlQBosonUmKavo1uA&t=2&mt=0 HTTP/1.1" 404 453 "-"
  "Snapchat/9.21.1.1 (iPad2,5; iOS 9.1; gzip)"'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:38:49.720Z'
id: 4e27bd2b-038a-4a89-abb4-d1d425ac6244
verified: false
validated: true
submitted: true
---
# Analyze Apache Logs for Snapchat Requests

## Command

```bash
cat /var/log/apache2/access.log | grep -v server-status | grep snapchat -i
```

## Description

This command filters the Apache access log to exclude server-status entries and identify requests from Snapchat clients by searching for 'snapchat' in user-agent strings, useful for confirming exploitation impact during a subdomain takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/var/log/apache2/access.log` | Path to the Apache access log file | Yes |
| `-v server-status` | Excludes lines matching 'server-status' | Yes |
| `grep snapchat -i` | Searches for 'snapchat' ignoring case | Yes |

## Examples

### Basic Usage

```bash
cat /var/log/apache2/access.log | grep -v server-status | grep snapchat -i
```

### Advanced Usage

```bash
cat /var/log/apache2/access.log | grep -v server-status | grep snapchat -i | tail -n 10
```

## Expected Output

Log entries showing GET requests from Snapchat apps, e.g., '23.235.39.33 - - [02/Aug/2016:18:28:25 +0000] "GET /bq/story_blob?story_id=fRaYutXlQBosonUmKavo1uA&t=2&mt=0 HTTP/1.1" 404 453 "-" "Snapchat/9.21.1.1 (iPad2,5; iOS 9.1; gzip)"'

## Related

- [[Related Procedure: Set Up Apache Server on Taken Over Subdomain]]
