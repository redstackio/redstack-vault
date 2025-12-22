---
type: command
executor: bash
data: |-
  userPassword
  surname
  name
  cn
  sn
  objectClass
  mail
  givenName
  commonName
output: null
platforms:
  - Linux
tags:
  - ldap
  - enumeration
verified: true
validated: true
---

# list-common-ldap-attributes

## Command

```bash
echo -e "userPassword\nsurname\nname\ncn\nsn\nobjectClass\nmail\ngivenName\ncommonName"
```

## Description

This command outputs a list of common default LDAP attributes that can be targeted in injection attacks to enumerate directory entries. Use it as a quick reference when crafting payloads to extract specific data types like passwords or emails.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | This is a static list; no parameters needed | No |

## Examples

### Basic Usage

```bash
list-common-ldap-attributes
```

### Advanced Usage

Pipe to a file for reference:

```bash
echo -e "userPassword\nsurname\nname\ncn\nsn\nobjectClass\nmail\ngivenName\ncommonName" > ldap-attributes.txt
```

## Expected Output

userPassword
surname
name
cn
sn
objectClass
mail
givenName
commonName

A plain text list of attributes, one per line.

## Related

- [[procedures/LDAP-Injection-with-Default-Attributes]]
