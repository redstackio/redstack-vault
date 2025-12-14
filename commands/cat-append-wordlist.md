---
id: cmd-007
data: cat rockyou.txt | head -1000 >> usernames.txt
tags:
  - wordlist
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.901Z'
verified: false
validated: true
submitted: true
---
# cat-append-wordlist

## Command

```bash
cat rockyou.txt | head -1000 >> usernames.txt
```

## Description

Appends the first 1000 lines from a wordlist to the usernames.txt file for enumeration testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| rockyou.txt | Source wordlist | Yes |
| head -1000 | Limit lines | No |
| >> usernames.txt | Append target | Yes |

## Examples

### Basic Usage

```bash
cat rockyou.txt | head -1000 >> usernames.txt
```

## Expected Output

No output; file grows with appended usernames.

## Related

- [[procedures/Prepare-Username-List-for-Enumeration]]
