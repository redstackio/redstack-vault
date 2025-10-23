---
id: c0dec02b-b330-416c-a516-91b11052b8b2
name: snmpwalk
type: cheatsheet
verified: false
created_at: '2020-07-14T18:14:48.745571+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# snmpwalk



**Command** ([[gather snmp v1 information with standard community strings]]):

```bash
snmpwalk -v1 -c public target-ip
snmpwalk -v1 -c private target-ip
snmpwalk -v1 -c manager target-ip

```







**Command** ([[enumerate windows users]]):

```bash
snmpwalk -c public -v1 target-ip 1.3.6.1.4.1.77.1.2.25

```







**Command** ([[enumerate current windows processes]]):

```bash
snmpwalk -c public -v1 target-ip 1.3.6.1.2.1.25.4.2.1.2

```







**Command** ([[enumerate windows open tcp ports]]):

```bash
snmpwalk -c public -v1 target-ip 1.3.6.1.2.1.6.13.1.3

```







**Command** ([[enumerate installed software]]):

```bash
snmpwalk -c public -v1 target-ip 1.3.6.1.2.1.25.6.3.1.2

```






