---
data: >-
  curl -fSL "https://s3.amazonaws.com/rocketchatbuild/rocket.chat-develop.tgz"
  -o rocket.chat.tgz
tags:
  - download
  - s3
type: command
output: 'Binary tarball download, in PoC: 179 bytes with progress indicators'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:42.022Z'
id: 6392efe2-ba81-4bbe-81df-a9afb877a20f
verified: false
validated: true
submitted: true
---
# curl-download-rocket-chat-tarball

## Command

```bash
curl -fSL "https://s3.amazonaws.com/rocketchatbuild/rocket.chat-develop.tgz" -o rocket.chat.tgz
```

## Description

Downloads the Rocket.Chat tarball from the S3 bucket and saves it locally, exploited in supply chain attacks by serving malicious content.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-f` | Fail silently on server errors | Yes |
| `-S` | Show errors on client errors | Yes |
| `-L` | Follow redirects | Yes |
| URL | The S3 URL for the tarball | Yes |
| `-o` | Output file name | Yes |

## Examples

### Basic Usage

```bash
curl -fSL "https://s3.amazonaws.com/rocketchatbuild/rocket.chat-develop.tgz" -o rocket.chat.tgz
```

### Advanced Usage

```bash
curl -fSL -v "https://s3.amazonaws.com/rocketchatbuild/rocket.chat-develop.tgz" -o rocket.chat.tgz
```

## Expected Output

Progress bar or direct binary download; success indicated by file creation with expected size (e.g., 179 bytes for PoC).

## Related

- [[Related Procedure: Download-and-Extract-Malicious-Tarball]]
