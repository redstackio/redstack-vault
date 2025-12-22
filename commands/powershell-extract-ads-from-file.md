---
id: c8efd62e-fc6d-4c71-8d9a-2c1149542636
name: powershell-extract-ads-from-file
type: command
executor: powershell
data: Get-Content -Path $_FILE -Stream $_ADS
output: |-
  PS C:\temp> Get-Content -Path normal.txt -Stream secret
  -----BEGIN OPENSSH PRIVATE KEY-----
  b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAlwAAAAdzc2gtcn
  NhAAAAAwEAAQAAAIEAtclXrtl7IGHL+fNLZ6FX4Tx+BRPJ7t4r9Y4vUrstEQ0b/hLxvpK9
  j/zwPGGOv/8ftZSFacXHFwae5pBWSWOV2Uv3GnvO6JW22u0iOOHHHbw31Qkb6SWMQD7TXd
  O3GeuMguGXvN7pK92T3ZccZ+KJgzlsWCBTkSMw21qQUzoQqZ0AAAIA/6UOO/+lDjsAAAAH
  c3NoLXJzYQAAAIEAtclXrtl7IGHL+fNLZ6FX4Tx+BRPJ7t4r9Y4vUrstEQ0b/hLxvpK9j/
  zwPGGOv/8ftZSFacXHFwae5pBWSWOV2Uv3GnvO6JW22u0iOOHHHbw31Qkb6SWMQD7TXdO3
  GeuMguGXvN7pK92T3ZccZ+KJgzlsWCBTkSMw21qQUzoQqZ0AAAADAQABAAAAgC2bV+48Dd
  Hv9za8PTzAk8WkYZFwh4bwImM2ytSctQ/EFDPIGPJQ6lIHiVX8u82beh8aJeaFgg9az97U
  c3FyFJPFSdbtyKTHKO5mpA+4epXaAMIZjZEEbbfhOqz3V5/oWTww55EWead4G8qjq1keOr
  /jjjxHK+LzJz5XqQu2v2EZAAAAQQCBxd1YEp9rM0LrPvbIrYlOWAJYlLQIXEp7XJMvtWY+
  0t0h4Qqr3jW392Yc6bRVB3Wey5neOqcDk8uUNCyoGWaVAAAAQQDhydJAVyLsslJx9cqKP4
  nIHOB9CRXrCsyWz0jJ8FQVbJG7suSIXH304dnLsmJjZ9iA3SdPRtMd5Y3s2zDoRW9TAAAA
  QQDOHEbGS6thnmbLad044iCSUSMIszeXkitF0tjgOhBaszmDwMETdoI5O/vE2AanxV3k9n
  PmoIeac1slqN/uyJVPAAAACXJvb3RAa2FsaQE=
  -----END OPENSSH PRIVATE KEY-----
created_at: '2019-11-22T18:04:45.284399+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - file-system
  - ads
  - extraction
verified: true
validated: true
---

# powershell-extract-ads-from-file

## Command

```powershell
Get-Content -Path $_FILE -Stream $_ADS
```

## Description

This PowerShell command retrieves the contents of an Alternate Data Stream (ADS) from a specified file on an NTFS volume. It is ideal for scripting and handling text-based hidden data like credentials or scripts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-Path $_FILE` | The path to the file containing the ADS (e.g., `normal.txt`) | Yes |
| `-Stream $_ADS` | The name of the ADS stream to extract (e.g., `secret`) | Yes |

## Examples

### Basic Usage

```powershell
Get-Content -Path normal.txt -Stream secret
```

### Advanced Usage

```powershell
Get-Content -Path C:\temp\file.txt -Stream hidden | Out-File extracted.txt
```

## Expected Output

```
PS C:\temp> Get-Content -Path normal.txt -Stream secret
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAlwAAAAdzc2gtcn
NhAAAAAwEAAQAAAIEAtclXrtl7IGHL+fNLZ6FX4Tx+BRPJ7t4r9Y4vUrstEQ0b/hLxvpK9
j/zwPGGOv/8ftZSFacXHFwae5pBWSWOV2Uv3GnvO6JW22u0iOOHHHbw31Qkb6SWMQD7TXd
O3GeuMguGXvN7pK92T3ZccZ+KJgzlsWCBTkSMw21qQUzoQqZ0AAAIA/6UOO/+lDjsAAAAH
c3NoLXJzYQAAAIEAtclXrtl7IGHL+fNLZ6FX4Tx+BRPJ7t4r9Y4vUrstEQ0b/hLxvpK9j/
zwPGGOv/8ftZSFacXHFwae5pBWSWOV2Uv3GnvO6JW22u0iOOHHHbw31Qkb6SWMQD7TXdO3
GeuMguGXvN7pK92T3ZccZ+KJgzlsWCBTkSMw21qQUzoQqZ0AAAADAQABAAAAgC2bV+48Dd
Hv9za8PTzAk8WkYZFwh4bwImM2ytSctQ/EFDPIGPJQ6lIHiVX8u82beh8aJeaFgg9az97U
c3FyFJPFSdbtyKTHKO5mpA+4epXaAMIZjZEEbbfhOqz3V5/oWTww55EWead4G8qjq1keOr
/jjjxHK+LzJz5XqQu2v2EZAAAAQQCBxd1YEp9rM0LrPvbIrYlOWAJYlLQIXEp7XJMvtWY+
0t0h4Qqr3jW392Yc6bRVB3Wey5neOqcDk8uUNCyoGWaVAAAAQQDhydJAVyLsslJx9cqKP4
nIHOB9CRXrCsyWz0jJ8FQVbJG7suSIXH304dnLsmJjZ9iA3SdPRtMd5Y3s2zDoRW9TAAAA
QQDOHEbGS6thnmbLad044iCSUSMIszeXkitF0tjgOhBaszmDwMETdoI5O/vE2AanxV3k9n
PmoIeac1slqN/uyJVPAAAACXJvb3RAa2FsaQE=
-----END OPENSSH PRIVATE KEY-----
```

The output displays the stream's contents, such as encoded keys or text.

## Related

- [[procedures/Extract-Alternate-Data-Stream-from-File]]
