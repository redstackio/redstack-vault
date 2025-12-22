---
id: e34e7752-99ff-412b-8947-191b2547f249
name: ldapsearch-query-root-dse-anonymous
type: command
executor: bash
data: ldapsearch -x -h $_TARGET_IP -s base
output: |-
  # extended LDIF
  #
  # LDAPv3
  # base <> (default) with scope baseObject
  # filter: (objectclass=*)
  # requesting: ALL
  #

  dn:
  domainFunctionality: 7
  forestFunctionality: 7
  domainControllerFunctionality: 7
  rootDomainNamingContext: DC=MEGABANK,DC=LOCAL
  ldapServiceName: MEGABANK.LOCAL:DC01@MEGABANK.LOCAL
  isGlobalCatalogReady: TRUE
  supportedSASLMechanisms: GSSAPI
  ...
created_at: '2020-03-24T19:57:21.478052+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - ldap
  - enumeration
verified: true
validated: true
---

# ldapsearch-query-root-dse-anonymous

## Command

```bash
ldapsearch -x -h $_TARGET_IP -s base
```

## Description

Queries the LDAP root DSE anonymously to retrieve server configuration, including the domain naming context for further enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -x | Use simple authentication (anonymous) | Yes |
| -h $_TARGET_IP | Target LDAP server IP | Yes |
| -s base | Search scope limited to base object | Yes |

## Examples

### Basic Usage

```bash
ldapsearch -x -h 10.10.10.10 -s base
```

### With Output Filtering

```bash
ldapsearch -x -h 10.10.10.10 -s base | grep rootDomainNamingContext
```

## Expected Output

Description: LDIF format with attributes like rootDomainNamingContext: DC=example,DC=com indicating the base DN.

## Related

- [[procedures/Query-LDAP-and-Enumerate-Base-DN]]
- [[tools/OpenLDAP-Utils]]
