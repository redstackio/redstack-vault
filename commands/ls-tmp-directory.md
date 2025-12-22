---
data: ls /tmp/
tags:
  - verification
  - file-list
type: command
output: alexb-says-hi ks-script-esd4my7v ks-script-eusq_sc5
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:37.210Z'
id: 11d1eb8c-c89b-4e19-8ae2-c4edff3ca254
verified: false
validated: true
submitted: true
---
# ls-tmp-directory

## Command

```bash
ls /tmp/
```

## Description

Lists files in the /tmp directory to check for RCE artifacts like payload-written files.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /tmp/ | Target directory | Yes |

## Examples

### Basic Usage

```bash
ls /tmp/
```

### Advanced Usage

```bash
ls -la /tmp/
```

## Expected Output

List of files, e.g., 'alexb-says-hi ks-script-esd4my7v ks-script-eusq_sc5' indicating new RCE file.

## Related

- [[commands/cat-tmp-alexb-says-hi]]
- [[procedures/Verify-RCE-Execution-in-Tmp-Directory]]
