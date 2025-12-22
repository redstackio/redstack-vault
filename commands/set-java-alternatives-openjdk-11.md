---
type: command
executor: bash
data: sudo update-java-alternatives -s java-1.11.0-openjdk-amd64
output: null
created_at: '2023-04-06T03:56:16.220734+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - java
  - configuration
  - debian
verified: true
validated: true
---

# set-java-alternatives-openjdk-11

## Command

```bash
sudo update-java-alternatives -s java-1.11.0-openjdk-amd64
```

## Description

Sets OpenJDK 11 as the default Java version using the alternatives system on Debian-based Linux, ensuring compatibility for Java applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Selects the specified alternative | Yes |
| `java-1.11.0-openjdk-amd64` | The OpenJDK 11 AMD64 set | Yes |

## Examples

### Basic Usage

```bash
sudo update-java-alternatives -s java-1.11.0-openjdk-amd64
```

## Expected Output

update-alternatives: using /usr/lib/jvm/java-1.11.0-openjdk-amd64 to provide /usr/bin/java (java) in manual mode
... (similar for javac, etc.)

## Related

- [[commands/install-openjdk-11-jdk]]
- [[procedures/Cobalt-Strike-Team-Server-Installation-and-Execution]]
