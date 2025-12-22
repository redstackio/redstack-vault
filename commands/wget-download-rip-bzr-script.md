---
id: fc1df270-c17e-45ce-bc3a-f5aedbe89d3a
name: wget-download-rip-bzr-script
type: command
executor: bash
data: 'wget https://raw.githubusercontent.com/kost/dvcs-ripper/master/rip-bzr.pl'
output: null
created_at: '2023-04-06T03:56:00.324827+00:00'
updated_at: '2023-04-10T20:33:54.895926+00:00'
platforms:
  - Linux
tags:
  - download
  - script-fetch
verified: true
validated: true
---

# wget-download-rip-bzr-script

## Command

```bash
wget https://raw.githubusercontent.com/kost/dvcs-ripper/master/rip-bzr.pl
```

## Description

This command uses wget to download the rip-bzr.pl Perl script from the dvcs-ripper GitHub repository. The script is used for extracting Bazaar repositories and is saved to the current working directory. Use this as the first step in preparing to rip insecure VCS repos.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Fixed GitHub raw URL for rip-bzr.pl | Yes (built-in) |

## Examples

### Basic Usage

```bash
wget https://raw.githubusercontent.com/kost/dvcs-ripper/master/rip-bzr.pl
```

### With Output Redirect

```bash
wget -O rip-bzr.pl https://raw.githubusercontent.com/kost/dvcs-ripper/master/rip-bzr.pl
```

## Expected Output

The command outputs progress like:

--2023-01-01 12:00:00--  https://raw.githubusercontent.com/kost/dvcs-ripper/master/rip-bzr.pl
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 12345 (12K) [text/plain]
Saving to: 'rip-bzr.pl'

rip-bzr.pl           100%[===================>]  12.05K  --.-KB/s    in 0.1s    

2023-01-01 12:00:01 (120 KB/s) - 'rip-bzr.pl' saved [12345/12345]

Success is indicated by the file being saved without errors.

## Related

- [[procedures/Extract-Source-Code-from-Bazaar-Repository-using-rip-bzr]]
- [[tools/dvcs-ripper]]
