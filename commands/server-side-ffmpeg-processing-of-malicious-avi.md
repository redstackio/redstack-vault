---
type: command
executor: bash
data: ffmpeg -i $_INPUT_AVI $_OUTPUT_MP4
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - ffmpeg
  - processing
  - exploits
verified: true
validated: true
---

# Server-Side FFmpeg Processing of Malicious AVI

## Command

```bash
ffmpeg -i $_INPUT_AVI $_OUTPUT_MP4
```

## Description

Processes an input AVI file using FFmpeg to convert it to MP4 format. When the AVI contains a malicious embedded HLS playlist, this triggers the vulnerability, causing FFmpeg to read the referenced local file during manifest parsing and stream setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i $_INPUT_AVI | Input file path (the malicious AVI) | Yes |
| $_OUTPUT_MP4 | Output MP4 file path | Yes |

## Examples

### Basic Usage

```bash
ffmpeg -i file_read.avi output.mp4
```

### Advanced Usage

```bash
ffmpeg -i file_read.avi -c copy output.mp4
```

## Expected Output

FFmpeg outputs progress logs like "[avi @ 0x...]" and may show HLS fetching attempts. Successful processing generates $_OUTPUT_MP4, but the file read occurs internally. Errors like "Invalid data found" may appear if the file isn't media, but the read still happens.

## Related

- [[procedures/Exploit-FFmpeg-HLS-Vulnerability-via-Malicious-AVI-for-Arbitrary-File-Read]]
- [[tools/FFmpeg]]
