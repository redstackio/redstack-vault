---
id: e34e7752-99ff-412b-8947-191b2547f249
name: Query LDAP Root DSE with Anonymous Bind
type: command
executor: bash
data: ldapsearch -x -h $_TARGET_IP -s base
output: 'root@kali:~# ldapsearch -x -h 10.10.10.10 -s base

  # extended LDIF

  #

  # LDAPv3

  # base <> (default) with scope baseObject

  # filter: (objectclass=*)

  # requesting: ALL

  #

  #

  dn:

  domainFunctionality: 7

  forestFunctionality: 7

  domainControllerFunctionality: 7

  rootDomainNamingContext: DC=MEGABANK,DC=LOCAL

  ldapServiceName: MEGABANK.LOCAL:DC01@MEGABANK.LOCAL

  isGlobalCatalogReady: TRUE

  supportedSASLMechanisms: GSSAP

  ...'
created_at: '2020-03-24T19:57:21.478052+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Query LDAP Root DSE with Anonymous Bind

```bash
ldapsearch -x -h $_TARGET_IP -s base
```

## Expected Output

```
root@kali:~# ldapsearch -x -h 10.10.10.10 -s base
# extended LDIF
#
# LDAPv3
# base <> (default) with scope baseObject
# filter: (objectclass=*)
# requesting: ALL
#

#
dn:
domainFunctionality: 7
forestFunctionality: 7
domainControllerFunctionality: 7
rootDomainNamingContext: DC=MEGABANK,DC=LOCAL
ldapServiceName: MEGABANK.LOCAL:DC01@MEGABANK.LOCAL
isGlobalCatalogReady: TRUE
supportedSASLMechanisms: GSSAP
...
```
