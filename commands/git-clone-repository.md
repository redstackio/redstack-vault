---
data: 'git clone https://github.com/oss-aimoto/tomcat-trailer.git'
tags:
  - setup
type: command
executor: bash
platforms:
  - Linux
id: c1666b08-5215-4f9c-9f98-346d545246a8
created_at: '2025-12-13T09:01:22.355Z'
updated_at: '2025-12-13T09:01:22.355Z'
verified: false
validated: true
submitted: true
---
# Git Clone Repository

## Command

```bash
git clone https://github.com/oss-aimoto/tomcat-trailer.git
```

## Description

Clones the GitHub repository containing the setup for demonstrating the Tomcat trailer vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://github.com/oss-aimoto/tomcat-trailer.git` | URL of the repository to clone | Yes |

## Examples

### Basic Usage

```bash
git clone https://github.com/oss-aimoto/tomcat-trailer.git
```

## Expected Output

Repository cloned to local directory.

## Related

- [[procedures/Setup-Vulnerable-Tomcat-Environment]]
