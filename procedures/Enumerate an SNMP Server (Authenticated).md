---
id: 1248f0ea-519b-4543-87df-32fe3daef4b0
name: Enumerate an SNMP Server (Authenticated)
type: procedure
verified: true
submitted: true
created_at: '2020-02-21T05:35:28.317618+00:00'
updated_at: '2023-05-26T00:45:53.991866+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
platforms:
- Linux
- Windows
tags:
- '[[data exposure]]'
- '[[Enumeration]]'
- '[[Network]]'
commands:
- '[[snmp-check Enumerate SNMP Server]]'
- '[[snmpwalk Enumerate SNMP Server]]'
---

# Enumerate an SNMP Server (Authenticated)

**Status**: ✓ Verified

## Summary

Enumerate SNMP with a valid community string. 

## Description

# Description

Enumerate SNMP with a valid community string.



# Instructions

Optional: Install mibs downloader to improve readability





**Code**: [[apt update && apt install snmp-mibs-downloader -y ]]





Note: If no results are returned when querying SMNP with the following commands, it may be attempting to use the wrong version. If so, try another versions (1, 2c, 3).

SNMP





**Command** ([[snmpwalk Enumerate SNMP Server]]):

```bash
snmpwalk -c $_COMMUNITY_STRING -v $_VERSION $_TARGET_IP
```











**Command** ([[snmp-check Enumerate SNMP Server]]):

```bash
snmp-check -c $_COMMUNITY_STRING -v $_VERSION $_TARGET_IP
```





SNMP can be queried directly for specific information using the OID of the intended result. A list of valid OID can be found: [here](http://oid-info.com/)

## Platforms

- Linux
- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]

## Commands Used

- [[snmp-check Enumerate SNMP Server]]
- [[snmpwalk Enumerate SNMP Server]]

## Tags

- [[data exposure]]
- [[Enumeration]]
- [[Network]]


