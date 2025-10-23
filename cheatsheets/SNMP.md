---
id: 9f8a62b8-2b0b-40cc-85fb-acbdf070eb2a
name: SNMP
type: cheatsheet
verified: false
created_at: '2020-07-14T18:14:33.750081+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# SNMP



**Command** ([[Automated SMB Enumeration]]):

```bash
enum4linux -a $ip

```







**Command** ([[Scan SMB]]):

```bash
nbtscan -r $ip

```







**Command** ([[NMBLookup]]):

```bash
nmblookup -A $ip

```







**Code**: [[
use scanner/smb/smb_login
set rhosts $ip
set SMBU]]







**Code**: [[
use exploit/windows/smb/psexec
set rhost $ip
set ]]







**Code**: [[
use auxiliary/scanner/smb/smb_enumusers
set rhost]]







**Code**: [[
use auxiliary/scanner/smb/smb_version
set rhosts ]]







**Code**: [[
use auxiliary/scanner/smb/smb2
set rhost $ip
set ]]







**Code**: [[
smb-enum-users
smb-enum-shares
smb-os-discovery
s]]







**Command** ([[snmp enuemrate public]]):

```bash
snmpget -v 1 -c public $ip version

```







**Command** ([[SNMPWALK]]):

```bash
snmpwalk -v 1 -c public $ip
snmpbulkwalk -v 2 -c public $ip

```







**Command** ([[Specify MIB]]):

```bash
snmpwalk -c public -v $ip $mib

```







**Command** ([[brute force community strings]]):

```bash
onesixtyone -c communitystrings.txt -i ips.txt

```







**Code**: [[
1.3.6.1.4.1.77.1.2.25
]]







**Code**: [[
1.3.6.1.2.1.25.4.2.1.2
]]







**Code**: [[
1.3.6.1.2.1.6.13.1.3
]]







**Code**: [[
1.3.6.1.2.1.25.6.3.1.2
]]






