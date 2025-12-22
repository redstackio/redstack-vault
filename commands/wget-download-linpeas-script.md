---
id: new-uuid-1
name: wget-download-linpeas-script
type: command
executor: bash
data: >-
  wget
  "https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh"
  -O linpeas.sh
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - download
  - enumeration
verified: true
validated: true
---

# wget-download-linpeas-script

## Command

```bash
wget "https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh" -O linpeas.sh
```

## Description

Downloads the latest LinPEAS enumeration script from GitHub using wget, saving it as linpeas.sh for local execution in privilege escalation assessments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -O linpeas.sh | Output file name | Yes |
| URL | GitHub release URL for linpeas.sh | Built-in |

## Examples

### Basic Usage

```bash
wget "https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh" -O linpeas.sh
```

## Expected Output

--2023-10-01 12:00:00--  https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh
Resolving github.com (github.com)... 140.82.121.3
Connecting to github.com (github.com)|140.82.121.3|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://github.com/carlospolop/PEASS-ng/releases/download/vX.Y.Z/linpeas.sh [following]
--2023-10-01 12:00:01--  https://github.com/carlospolop/PEASS-ng/releases/download/vX.Y.Z/linpeas.sh
Length: 1234567 (1.2M) [text/x-shellscript]
Saving to: 'linpeas.sh'

linpeas.sh 100%[===================>]   1.20M  --.-KB/s    in 0.5s    

2023-10-01 12:00:02 (2.4 MB/s) - 'linpeas.sh' saved [1234567/1234567]

## Related

- [[procedures/Linux-Privilege-Escalation-Enumeration]]
- [[tools/linPEAS]]
