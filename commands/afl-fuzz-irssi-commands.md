---
data: afl-fuzz -i in -o out -m none -f fuzzc.txt Irssi
tags:
  - fuzzing
  - afl
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:30.993Z'
id: 534db891-b01b-4b3e-89dc-fefeeb4750d2
verified: false
validated: true
submitted: true
---
# AFL Fuzz Irssi Commands

## Command

```bash
afl-fuzz -i in -o out -m none -f fuzzc.txt Irssi
```

## Description

Fuzzes Irssi command processing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i in | Input | Yes |
| -o out | Output | Yes |
| -m none | No limit | Yes |
| -f fuzzc.txt | Commands file | Yes |
| Irssi | Target | Yes |

## Examples

### Basic Usage

```bash
afl-fuzz -i in -o out -m none -f fuzzc.txt Irssi
```

## Expected Output

Command handling crashes.

## Related

- [[commands/afl-fuzz-irssi-output]]
