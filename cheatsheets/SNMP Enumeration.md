---
id: f3d5c96b-3d8e-4beb-8b4d-f52439840e57
name: SNMP Enumeration
type: cheatsheet
verified: true
created_at: '2019-09-17T00:51:24.080377+00:00'
updated_at: '2023-05-30T20:12:52.306352+00:00'
---

# SNMP Enumeration

**Status**: ✓ Verified

# Description

Query and enumerate the SNMP service.





Install snmp-mibs-downloader and configure it to make the output from snmpwalk easier to read





**Command** ([[Install snmp-mibs-downloader]]):

```bash
apt update && apt install snmp-mibs-downloader -y && sed -i '/mibs/s/^/#/g' /etc/snmp/snmp.conf
```









**Command** ([[Brute Force SNMP Community String]]):

```bash
onesixtyone -c $_WORDLIST $_TARGET_IP
```









**Command** ([[snmpwalk Enumerate SNMP Server]]):

```bash
snmpwalk -c $_COMMUNITY_STRING -v $_VERSION $_TARGET_IP
```









**Command** ([[snmp-check Enumerate SNMP Server]]):

```bash
snmp-check -c $_COMMUNITY_STRING -v $_VERSION $_TARGET_IP
```






