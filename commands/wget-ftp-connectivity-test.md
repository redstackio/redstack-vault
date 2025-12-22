---
type: command
executor: bash
data: 'wget --spider ftp://$_TARGET_IP/'
output: null
platforms:
  - Linux
  - Windows
tags:
  - exfiltration
  - ftp
  - recon
verified: true
validated: true
---

# wget-ftp-connectivity-test

## Command

```bash
wget --spider ftp://$_TARGET_IP/
```

## Description

This command tests connectivity to an FTP server by attempting a non-downloading spider crawl. It connects, logs in anonymously, and lists the root directory to verify accessibility without transferring data, ideal for pre-exfiltration reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address or hostname of the FTP server (e.g., 192.168.1.100) | Yes |

## Examples

### Basic Usage

```bash
wget --spider ftp://10.10.10.10/
```

### With Timeout

```bash
wget --spider --timeout=10 ftp://$_TARGET_IP/
```

## Expected Output

Description of what output to expect when the command runs successfully.

```
--2023-01-01 12:00:00--  ftp://10.10.10.10/
Connecting to 10.10.10.10:21... connected.
Logging in as anonymous ... Logged in!
==> SYST ... done.    ==> PWD ... done.
==> TYPE I ... done.  ==> CWD not needed.
==> PORT ... done.    ==> LIST ... done.

FINISHED --2023-01-01 12:00:01--
FTP: 1 retrievals, 0 bytes retrieved in 1s (0 bytes/s)
```

## Related

- [[procedures/Download-Files-Recursively-from-FTP]]
- [[commands/wget-recursive-ftp-download]]
