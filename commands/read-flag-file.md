---
data: cat flag.txt
tags:
  - shell
  - flag
type: command
output: |-
  Yay! Here is your flag:

  flag{cha1n1ng_bugs_f0r_fun_4nd_pr0f1t?_or_rep0rt_an_LF1}

  Go to https://hackerone.com/h1-5411-ctf and submit your writeup!
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.990Z'
id: 8293b572-44f4-4ef2-a6ac-c4e7c104a51b
verified: false
validated: true
submitted: true
---
# read-flag-file

## Command

```bash
cat flag.txt
```

## Description

Reads the flag file in the reverse shell session after RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Assumes in /app directory | No |

## Examples

### Basic Usage

```bash
cd /app && cat flag.txt
```

## Expected Output

Flag content: flag{cha1n1ng_bugs_f0r_fun_4nd_pr0f1t?_or_rep0rt_an_LF1}

## Related

- [[Related Procedure: Achieve-RCE-and-Read-Flag]]
