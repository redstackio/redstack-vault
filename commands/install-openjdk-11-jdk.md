---
type: command
executor: bash
data: sudo apt-get install openjdk-11-jdk
output: null
created_at: '2023-04-06T03:56:16.220578+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - installation
  - java
  - debian
verified: true
validated: true
---

# install-openjdk-11-jdk

## Command

```bash
sudo apt-get install openjdk-11-jdk
```

## Description

Installs the OpenJDK 11 Java Development Kit on Debian-based Linux systems, required for running Java-based tools like Cobalt Strike.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `install` | Installs the specified package | Yes |
| `openjdk-11-jdk` | The OpenJDK 11 JDK package | Yes |

## Examples

### Basic Usage

```bash
sudo apt-get install openjdk-11-jdk
```

## Expected Output

Reading package lists... Done
Building dependency tree
... (installation progress)
Setting up openjdk-11-jdk (11.0.XX+YY) ...

## Related

- [[commands/set-java-alternatives-openjdk-11]]
- [[procedures/Cobalt-Strike-Team-Server-Installation-and-Execution]]
