---
id: c73bfa44-ece9-4527-b555-ba10d4252691
name: Log4Shell Scanning Procedure
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:55:56.889303+00:00'
updated_at: '2023-04-06T03:55:56.904318+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]'
- '[[Subvert Trust Controls|T1553 - Subvert Trust Controls]]'
sub_techniques:
- '[[Code Signing|T1553.002 - Code Signing]]'
tags:
- '[[CVE-2021-44228 Log4Shell]]'
- '[[Scanning]]'
commands:
- '[[Log4j Scan with default parameters]]'
- '[[Log4j Scan with WAF Bypass]]'
---

# Log4Shell Scanning Procedure

## Summary

This procedure involves scanning a target system for the presence of the Log4Shell vulnerability (CVE-2021-44228) using the log4j-scan tool. The Log4Shell vulnerability is a remote code execution (RCE) vulnerability found in the Apache Log4j library, which is widely used in many software applicatio

## Description

# Description

This procedure involves scanning a target system for the presence of the Log4Shell vulnerability (CVE-2021-44228) using the log4j-scan tool. The Log4Shell vulnerability is a remote code execution (RCE) vulnerability found in the Apache Log4j library, which is widely used in many software applications. An attacker can exploit this vulnerability to execute arbitrary code on a target system, potentially leading to a full compromise of the system.

To scan for this vulnerability, the log4j-scan tool is used. This tool sends specially crafted requests to the target system and checks if the system is vulnerable. If the system is vulnerable, the tool will provide information on the vulnerability and the exploitability of the system. This procedure is useful for identifying vulnerable systems and prioritizing them for patching or further exploitation.

## Requirements

1. Access to the log4j-scan tool

1. Access to the target system

## Defense

1. Apply the latest security patches to the Apache Log4j library.

1. Restrict network access to the log4j-scan tool.

1. Implement network segmentation to limit the impact of a potential exploit.

## Objectives

1. Identify systems that are vulnerable to the Log4Shell vulnerability

# Instructions

1. To use the log4j-scan tool, run the following command:

```
python3 log4j-scan.py -u <target_url> [--options]
```

Where:
- `<target_url>` is the URL of the target system to scan.
- `--options` are optional arguments that can be used to customize the scan.

For example, to scan a target system with the default options, run:

```
python3 log4j-scan.py -u http://127.0.0.1:8080
```

**Code**: [[usage: log4j-scan.py [-h] [-u URL] [-l USEDLIST] []]

> - `-u URL`: The URL of the target system to scan.
- `--run-all-tests`: Run all tests, including the exploit test.
- `--waf-bypass`: Use WAF bypass techniques to bypass web application firewalls.
- `--wait-time WAIT_TIME`: The time to wait between requests, in seconds.
- `--dns-callback-provider DNS_CALLBACK_PROVIDER`: The DNS callback provider to use.
- `--custom-dns-callback-host CUSTOM_DNS_CALLBACK_HOST`: The custom DNS callback host to use.

**Command** ([[Log4j Scan with default parameters]]):

```bash
python3 log4j-scan.py -u http://127.0.0.1:8081 --run-all-test
```

**Command** ([[Log4j Scan with WAF Bypass]]):

```bash
python3 log4j-scan.py -u http://127.0.0.1:808 --waf-bypass
```

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Exploitation of Remote Services|T1210 - Exploitation of Remote Services]]
- [[Subvert Trust Controls|T1553 - Subvert Trust Controls]]

### Sub-Techniques

- [[Code Signing|T1553.002 - Code Signing]]

## Commands Used

- [[Log4j Scan with default parameters]]
- [[Log4j Scan with WAF Bypass]]

## Tags

- [[CVE-2021-44228 Log4Shell]]
- [[Scanning]]
