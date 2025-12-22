---
id: a18b7836-4684-41af-8005-d17585ffcefe
name: ldapsearch-anonymous-query-base-dn
type: command
executor: bash
data: 'ldapsearch -x -h $_TARGET_IP -b ''dc=$_ENTRY1,dc=$_ENTRY2'''
output: null
created_at: '2019-12-15T22:33:38.234260+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - ldap
  - enumeration
verified: true
validated: true
---

# ldapsearch-anonymous-query-base-dn

## Command

```bash
ldapsearch -x -h $_TARGET_IP -b 'dc=$_ENTRY1,dc=$_ENTRY2'
```

## Description

Performs an anonymous subtree search from the base DN to enumerate domain objects like users, organizational units, and other LDAP entries. This command uses simple authentication (-x) to query the LDAP server without credentials, which is useful for initial reconnaissance on exposed LDAP services.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -x | Use simple authentication (anonymous bind) | Yes |
| -h $_TARGET_IP | Target IP address or hostname of the LDAP server | Yes |
| -b 'dc=$_ENTRY1,dc=$_ENTRY2' | Base distinguished name (DN) for the search, e.g., 'dc=example,dc=com' where $_ENTRY1 and $_ENTRY2 are domain components | Yes |

## Examples

### Basic Usage

```bash
ldapsearch -x -h 10.10.10.10 -b 'dc=example,dc=com'
```

### Filter for Users

```bash
ldapsearch -x -h 10.10.10.10 -b 'dc=example,dc=com' '(objectClass=user)'
```

## Expected Output

LDIF (LDAP Data Interchange Format) entries listing domain objects, such as:

```
# extended LDIF
#
# LDAPv3
# base <dc=corporatehq,dc=com> with scope subtree
# filter: (objectclass=*)
# requesting: ALL
#

# corporatehq.com
 dn: dc=corporatehq,dc=com
 dc: corporatehq
 objectClass: top
 objectClass: domain

# passwd, corporatehq.com
 dn: ou=passwd,dc=corporatehq,dc=com
 ou: passwd
 objectClass: top
 objectClass: organizationalUnit

# bob, passwd, corporatehq.com
 dn: uid=bob8791,ou=passwd,dc=corporatehq,dc=com
 uid: bob
 cn: Bob
 objectClass: account
 objectClass: posixAccount
 objectClass: top
 userPassword:: e0JTREFVVEh9Ym9i 
 uidNumber: 5001
 gidNumber: 5001
 gecos: Bob
 homeDirectory: /home/bob
 loginShell: /bin/sh
```

This output includes user details like UIDs, passwords (hashed), and home directories if accessible anonymously.

## Related

- [[tools/ldapsearch]]
- [[procedures/Query-LDAP-and-Enumerate-Base-DN]]
