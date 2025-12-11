---
data: cat /tmp/file
tags:
  - file-read
type: command
executor: bash
platforms:
  - Linux
id: 4042f19d-c267-4ab9-8e5e-90fa78db91fc
created_at: '2025-12-11T03:47:47.570Z'
updated_at: '2025-12-11T03:47:47.570Z'
verified: false
validated: true
submitted: true
---
# cat-file-contents

## Command

```bash
cat /tmp/file
```

## Description

Displays the contents of a file to verify overwrite or injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `/tmp/file` | Path to file | Yes |

## Examples

### Basic Usage

```bash
cat /tmp/file
```

## Expected Output

commit f00f9538d29b176e9dfb2eb1bfe1eab190cad3d9
Author: Administrator <admin@example.com>
Date: Wed Jul 24 13:08:51 2019 +0000

 controlled content

## Related

- [[procedures/Verify-File-Overwrite]]
