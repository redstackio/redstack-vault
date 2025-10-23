---
id: 060e8974-e12a-4161-b60e-72801321440f
name: LDAP Lookup & Auth
type: cheatsheet
verified: false
created_at: '2020-07-14T18:21:09.741959+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# LDAP Lookup & Auth

# Description

Search and Authenticate with LDAP using these tools.







**Command** ([[ldapsearch]]):

```bash
ldapsearch -x -h target-ip -b "dc=domain,dc=tld"

```







**Command** ([[User lookup by UID]]):

```bash
ldapsearch -x -h ldap.domain.com -b o=domain.com -s sub uid=jdoe| egrep "uid:|uidnumber:|gidnumber:|cn:|gecos:|description:|loginshell:|homedirectory:"

```







**Command** ([[User lookup by name]]):

```bash
ldapsearch -x -h ldap.domain.com -b o=domain.com -s sub '(&(sn=Tubberville)(givenname=James))'

```







**Command** ([[Set pass as self]]):

```bash
ldappasswd -H ldaps://ldap.domain.com:6361 -D 'cn=John Doe (jdoe),ou=hr,ou=users,o=domain.com' -S -W -A  

```







**Command** ([[Set pass as admin]]):

```bash
ldappasswd -H ldaps://ldap.domain.com:6361 -x -D 'cn=admin,ou=hr,ou=users,o=domain.com' -S -W 'uid=jdoe,ou=hr users,o=domain.com '   

```






