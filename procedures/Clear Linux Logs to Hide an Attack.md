---
id: 8d872b76-6a70-43c1-9bde-f73005534fb5
name: Clear Linux Logs to Hide an Attack
type: procedure
verified: true
submitted: true
created_at: '2019-10-31T21:16:30.160944+00:00'
updated_at: '2023-05-26T00:50:59.787324+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Indicator Removal on Host|T1070 - Indicator Removal on Host]]'
platforms:
- Linux
tags:
- '[[audit]]'
- '[[Incident Response]]'
- '[[Operating Systems]]'
---

# Clear Linux Logs to Hide an Attack

**Status**: ✓ Verified

## Summary

After exploiting a system, it may be necessary to clear log files to hide the presence and actions of an attacker. While clearing common log files can help conceal the  attack, it should be noted that many systems are monitored specifically for instances where log files are cleared, and may stand o

## Description

# Description

After exploiting a system, it may be necessary to clear log files to hide the presence and actions of an attacker. While clearing common log files can help conceal the  attack, it should be noted that many systems are monitored specifically for instances where log files are cleared, and may stand out in SIEM/IPS logs.

# Instructions

Erase the contents of .bash_history for all users using these one liner commands:

**Code**: [[for FILE in $(find /home /root -name '.bash_histor]]

Erase the contents of auth.log

**Code**: [[for FILE in $(find /var/log -name "auth.log" 2>/de]]

## Platforms

- Linux

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Indicator Removal on Host|T1070 - Indicator Removal on Host]]

## Tags

- [[audit]]
- [[Incident Response]]
- [[Operating Systems]]
