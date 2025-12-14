---
id: cmd-add-hosts-entry
data: echo "198.211.125.160 poc.fogbugz.com" | sudo tee -a /etc/hosts
tags:
  - network
  - redirect
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.230Z'
verified: false
validated: true
submitted: true
---
# Add Hosts Entry for Subdomain Redirect

## Command

```bash
echo "198.211.125.160 poc.fogbugz.com" | sudo tee -a /etc/hosts
```

## Description

This command appends a line to /etc/hosts to redirect poc.fogbugz.com to IP 198.211.125.160, simulating subdomain control for SSRF PoC on GitLab.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| IP (198.211.125.160) | Target VPS IP | Yes |
| domain (poc.fogbugz.com) | Subdomain to redirect | Yes |

## Examples

### Basic Usage

```bash
echo "198.211.125.160 poc.fogbugz.com" | sudo tee -a /etc/hosts
```

### Advanced Usage

For multiple entries:
```bash
echo "198.211.125.160 another.sub.com" | sudo tee -a /etc/hosts
echo "10.0.0.1 internal.local" | sudo tee -a /etc/hosts
```

## Expected Output

The command outputs the added line (e.g., '198.211.125.160 poc.fogbugz.com') with no errors if sudo succeeds. Verify with 'grep poc.fogbugz.com /etc/hosts'.

## Related

- [[Related Procedure|procedures/Simulate-FogBugz-Subdomain-Control-via-Hosts-File]]
