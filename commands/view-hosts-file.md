---
data: cat /etc/hosts
tags:
  - discovery
  - system-info
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:15.418Z'
id: 44713f4c-b658-4232-b3f5-779d870e3f0a
verified: false
validated: true
submitted: true
---
# View Hosts File

## Command

```bash
cat /etc/hosts
```

## Description

Displays the contents of the /etc/hosts file to identify server affiliations and domains.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```bash
cat /etc/hosts
```

## Expected Output

Entries including 127.0.0.1 localhost, [redacted] app.semrush.net [redacted], confirming Semrush domain.

## Related

- [[Related Procedure]]
