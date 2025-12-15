---
id: cmd-slack-api-files-info
data: >-
  curl -H "Authorization: Bearer YOUR_SLACK_TOKEN"
  "https://slack.com/api/files.info?file={FILE_ID}"
tags:
  - api
  - slack
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:15.106Z'
verified: false
validated: true
submitted: true
---
# slack-api-files-info

## Command

```bash
curl -H "Authorization: Bearer YOUR_SLACK_TOKEN" "https://slack.com/api/files.info?file={FILE_ID}"
```

## Description

Queries Slack API to retrieve file details, including url_private for private files like Post JSON.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Authorization | Bearer token for auth | Yes |
| file | File ID from Slack | Yes |

## Examples

### Basic Usage

```bash
curl -H "Authorization: Bearer xoxb-123" "https://slack.com/api/files.info?file=F123"
```

### Advanced Usage

Parse JSON for url_private.

```bash
curl ... | jq '.file.url_private'
```

## Expected Output

JSON response with file info, e.g., {"url_private": "https://files.slack.com/files-pri/..."}.

## Related

- [[procedures/Create-Slack-Post-and-Retrieve-JSON]]
