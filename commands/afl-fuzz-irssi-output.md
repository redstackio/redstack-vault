---
data: afl-fuzz -i in -o out -m none -f fuzzp.txt Irssi
tags:
  - fuzzing
  - afl
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:30.997Z'
id: ae82c58c-2ed7-4ce5-8c8a-4bc6e323ffdf
verified: false
validated: true
submitted: true
---
# AFL Fuzz Irssi Output

## Command

```bash
afl-fuzz -i in -o out -m none -f fuzzp.txt Irssi
```

## Description

Fuzzes Irssi output parsing via Perl script.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i in | Input dir | Yes |
| -o out | Output dir | Yes |
| -m none | No mem limit | Yes |
| -f fuzzp.txt | Input file | Yes |
| Irssi | Target | Yes |

## Examples

### Basic Usage

```bash
afl-fuzz -i in -o out -m none -f fuzzp.txt Irssi
```

## Expected Output

Crashes on OOB reads.

## Related

- [[commands/afl-fuzz-irssi-commands]]
