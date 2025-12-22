---
type: command
executor: bash
data: 'wget https://raw.githubusercontent.com/kost/dvcs-ripper/master/rip-hg.pl'
tags:
  - download
  - tool-acquisition
platforms:
  - Linux
verified: true
validated: true
---

# Download rip-hg.pl Script

## Command

```bash
wget https://raw.githubusercontent.com/kost/dvcs-ripper/master/rip-hg.pl
```

## Description

This command fetches the rip-hg.pl Perl script from the dvcs-ripper GitHub repository using wget. It is used as the first step in preparing to extract Mercurial repositories, ensuring the tool is available locally before execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://raw.githubusercontent.com/kost/dvcs-ripper/master/rip-hg.pl | Direct URL to the script | Yes |

## Examples

### Basic Usage

```bash
wget https://raw.githubusercontent.com/kost/dvcs-ripper/master/rip-hg.pl
```

### Advanced Usage

```bash
wget -O rip-hg.pl https://raw.githubusercontent.com/kost/dvcs-ripper/master/rip-hg.pl && chmod +x rip-hg.pl
```

## Expected Output

The command outputs a progress indicator like:

--2023-01-01 12:00:00--  https://raw.githubusercontent.com/kost/dvcs-ripper/master/rip-hg.pl
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 12345 (12K) [text/plain]
Saving to: 'rip-hg.pl'

rip-hg.pl 100%[===================>]  12.05K  --.-KB/s    in 0.1s

2023-01-01 12:00:01 (120 KB/s) - 'rip-hg.pl' saved [12345/12345]

## Related

- [[procedures/mercurial-source-code-extraction-with-rip-hg-pl]]
- [[commands/run-dvcs-ripper-docker-container]]
