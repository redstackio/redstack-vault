---
type: command
executor: command_prompt
data: 'more < $_FILE:$_ADS'
output: |-
  C:\temp>more < normal.txt:secret
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
created_at: '2019-11-22T18:04:45.282847+00:00'
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

# more-extract-ads-from-file

## Command

```command_prompt
more < $_FILE:$_ADS
```

## Description

This command extracts and displays the contents of an Alternate Data Stream (ADS) from a specified file using the `more` pager in Command Prompt. It is a simple way to view hidden stream data without additional tools.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `$_FILE` | The base file name containing the ADS (e.g., `normal.txt`) | Yes |
| `$_ADS` | The name of the ADS stream (e.g., `secret`) | Yes |

## Examples

### Basic Usage

```command_prompt
more < normal.txt:secret
```

### Advanced Usage

```command_prompt
more < C:\temp\file.txt:hidden > extracted.txt
```

## Expected Output

```
C:\temp>more < normal.txt:secret
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

The output shows the raw contents of the ADS stream.

## Related

- [[procedures/Extract-Alternate-Data-Stream-from-File]]
