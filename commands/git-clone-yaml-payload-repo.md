---
id: 37064acd-75dd-4b96-9809-864f176e8a2b
type: command
executor: bash
data: 'git clone https://github.com/artsploit/yaml-payload.git'
output: null
platforms:
  - Linux
  - macOS
tags:
  - git
  - clone
  - payload
created_at: '2023-04-06T03:55:59.656617+00:00'
updated_at: '2023-04-10T20:22:30.128005+00:00'
verified: true
validated: true
---

# git-clone-yaml-payload-repo

## Command

```bash
git clone https://github.com/artsploit/yaml-payload.git
```

## Description

Clones the yaml-payload GitHub repository containing Java source code for a SnakeYAML deserialization gadget used in RCE exploits against Spring Boot applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| https://github.com/artsploit/yaml-payload.git | Repository URL | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/artsploit/yaml-payload.git
```

### With Specific Directory

```bash
git clone https://github.com/artsploit/yaml-payload.git ./custom-dir
```

## Expected Output

Cloning into 'yaml-payload'...
remote: Enumerating objects: 10, done.
remote: Counting objects: 100% (10/10), done.
remote: Compressing objects: 100% (8/8), done.
Receiving objects: 100% (10/10), done.

## Related

- [[procedures/Remote-Code-Execution-via-Spring-Boot-Actuator-Env]]
