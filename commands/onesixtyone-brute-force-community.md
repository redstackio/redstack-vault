---
type: command
executor: bash
data: onesixtyone -c $_WORDLIST $_TARGET_IP
output: >-
  root@kali:~/Documents# onesixtyone -c wordlist.txt 10.10.10.10

  Scanning 1 hosts, 4603 communities

  10.10.10.10 [public] Linux Host 4.4.0-75-generic #96~14.04.1-Ubuntu SMP Thu
  Apr 20 11:06:56 UTC 2017 i686
platforms:
  - Linux
  - Windows
tags:
  - brute-force
  - snmp
  - discovery
verified: true
validated: true
---

# Onesixtyone-Brute-Force-Community

## Command

```bash
onesixtyone -c $_WORDLIST $_TARGET_IP
```

## Description

This command uses the onesixtyone tool to brute-force SNMP community strings on a target IP address by testing entries from a specified wordlist. It sends parallel UDP queries to port 161 and outputs successful matches along with any retrieved SNMP data, aiding in network reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -c | Path to the wordlist file containing community strings (one per line) | Yes |
| $_WORDLIST | The actual file path for the community wordlist (e.g., /path/to/wordlist.txt) | Yes |
| $_TARGET_IP | IP address or hostname of the target device running SNMP | Yes |

## Examples

### Basic Usage

```bash
onesixtyone -c /usr/share/wordlists/snmp.txt 192.168.1.100
```

### Advanced Usage

```bash
onesixtyone -c custom_communities.txt -w 10.10.10.10:161
```

> The -w option can specify a custom timeout or port if needed, but defaults to UDP 161.

## Expected Output

Description of what output to expect when the command runs successfully.

```
root@kali:~/Documents# onesixtyone -c wordlist.txt 10.10.10.10
Scanning 1 hosts, 4603 communities
10.10.10.10 [public] Linux Host 4.4.0-75-generic #96~14.04.1-Ubuntu SMP Thu Apr 20 11:06:56 UTC 2017 i686
```

A successful run shows the scanning progress and details any valid community strings found, including SNMP responses like system description. Failed attempts produce no match output.

## Related

- [[procedures/Brute-Force-SNMP-Community-String]]
- [[tools/onesixtyone]]
