---
id: 3cb3ecaf-63f0-4a4c-85a0-ee194fac5a34
name: DNS-Rebinding-to-Localhost
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:57.659791+00:00'
updated_at: '2024-10-01T00:00:00+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - dns-rebinding
  - localhost
  - protection-bypasses
commands:
  - '[[commands/dig-dns-lookup-for-rebinding-domain]]'
platforms:
  - Web
  - Network
tools: []
validated: true
---

# DNS-Rebinding-to-Localhost

## Summary

DNS rebinding to localhost is a technique that circumvents network security controls and browser same-origin policies by dynamically altering DNS resolutions for the same domain. An attacker controls a domain whose DNS responses initially point to the attacker's server (with a very short TTL, such as 0 or 1 second) and subsequently resolve to 127.0.0.1, allowing client-side JavaScript on a malicious webpage to access local services on the victim's machine that would otherwise be inaccessible from external sources. This is commonly used to bypass localhost filters, access internal APIs, or exfiltrate sensitive data from local applications.

## Description

In a DNS rebinding attack targeting localhost, the attacker hosts a malicious webpage under a controlled domain (e.g., rebind.attacker.com). When the victim visits this page, JavaScript embedded in the page initiates network requests (e.g., via fetch() or XMLHttpRequest) to the same domain. The attacker's DNS server is configured to respond to the initial DNS query with the attacker's public IP address and a minimal TTL, causing the browser to re-query DNS almost immediately for subsequent requests. The second DNS response then maps the domain to 127.0.0.1 (localhost), enabling the JavaScript to interact with local ports or services (e.g., a development server on localhost:3000) as if the request originated from the same origin. This bypasses protections like firewall rules blocking external access to loopback interfaces or browser policies restricting cross-origin requests to localhost. The technique requires precise control over DNS responses, often distinguishing initial from follow-up queries based on client IP, query timing, or other heuristics. It is effective against web applications with exposed local endpoints and is a known vector for attacking router admin panels, cloud metadata services, or internal tools.

## Requirements

1. Control over a domain name and a customizable DNS server capable of dynamic responses (e.g., using BIND, PowerDNS, or a custom script).
2. A web server to host the malicious HTML/JavaScript payload.
3. Network access to send tailored DNS responses to the victim (e.g., via authoritative DNS or poisoning in certain setups).
4. Knowledge of the target's local service port (e.g., 8080 for a vulnerable local app).
5. Victim's browser must support JavaScript and not have strict DNS caching or rebinding protections enabled.

## Defense

Defensive measures and detection strategies:

- Implement browser-level protections like DNS rebinding mitigations in modern browsers (e.g., Chrome's private network access checks) or use extensions that enforce strict origin policies.
- Configure DNS resolvers to ignore or block responses with extremely low TTL values (e.g., TTL < 10 seconds) and monitor for rapid re-queries from the same client.
- Deploy firewalls or network ACLs to prevent external connections to localhost interfaces and local ports.
- Use Content Security Policy (CSP) headers on web applications to restrict fetch origins and block unexpected internal requests.
- Monitor DNS traffic for anomalies, such as multiple resolutions for the same domain in quick succession or resolutions to private IPs like 127.0.0.1 from public queries.
- Enable logging for local services and alert on unexpected access from browser contexts.

## Objectives

1. Bypass DNS-based filters or same-origin policy restrictions to access localhost services from a remote webpage.
2. Interact with or exfiltrate data from internal local applications, such as admin interfaces or metadata endpoints.
3. Achieve initial access or lateral movement by exploiting locally bound services that are not internet-exposed.
4. Demonstrate or test rebinding protections in a controlled environment.

## Instructions

### Step 1: Register and Prepare the Rebinding Domain

**Context**: Select a domain you control and configure your DNS server as authoritative for it. This allows you to manipulate responses dynamically. Why: The domain serves as the pivot point between external and local resolutions, enabling the rebind without alerting the victim.

No specific command is needed here; use your DNS provider's panel or server configuration to set the NS records pointing to your server. Ensure the server can track client queries (e.g., by IP) to differentiate initial and rebinding responses.

### Step 2: Configure DNS Server for Dynamic Responses

**Context**: Set up the DNS server to handle queries intelligently. For the first query from a client, respond with your server's public IP (A record) and TTL=1. For immediate follow-up queries from the same client, respond with 127.0.0.1 (A record) and a longer TTL (e.g., 300). Why: The short initial TTL forces a quick re-query, allowing the switch to localhost without the browser caching the external IP too long.

This step typically involves editing zone files or scripting the DNS responses (e.g., using a Python DNS server library like dnslib). Test the configuration locally before deployment. If using a CNAME as in the example, ensure it ultimately points to localhost for rebinding.

### Step 3: Create and Host the Malicious Webpage

**Context**: Develop an HTML page with JavaScript that triggers multiple requests to the rebinding domain, targeting a specific local port. Why: The JavaScript exploits the rebinding to make cross-origin requests appear same-origin, accessing localhost resources.

Create a file named index.html:

```html
<!DOCTYPE html>
<html>
<head><title>Rebind Test</title></head>
<body>
<script>
  // Initial load happens here from attacker's IP
  fetch('http://$_REBIND_DOMAIN:$_LOCAL_PORT/endpoint')
    .then(response => response.text())
    .then(data => console.log('Rebound data:', data))
    .catch(err => console.error('Error:', err));
</script>
</body>
</html>
```

Host this on your web server (e.g., using Python: `python3 -m http.server 80`). Replace $_REBIND_DOMAIN with your domain and $_LOCAL_PORT with the target's local service port (e.g., 8080).

### Step 4: Test DNS Resolution for Rebinding

**Context**: Verify the DNS setup by simulating queries to ensure the resolution behaves as expected (initially external, then local). Why: This confirms the TTL manipulation and record switching before targeting a victim, preventing misconfigurations.

**Command** ([[commands/dig-dns-lookup-for-rebinding-domain]]):
```bash
dig $_REBIND_DOMAIN +noall +answer
```

> This performs a focused DNS query to retrieve only the answer section, helping inspect the record type (A or CNAME) and value without verbose output. Run it multiple times quickly to simulate re-queries and confirm the switch to localhost.

### Step 5: Deploy and Monitor the Attack

**Context**: Direct the victim to visit the malicious page and observe the rebinding in action. Why: This executes the full technique, allowing interaction with the local service; monitor network traffic to confirm the IP switch and data flow.

Lure the victim via phishing or social engineering to http://$_REBIND_DOMAIN. Use tools like Wireshark on the victim side (if testing) to capture DNS queries and confirm the rebind. If successful, the JavaScript will receive responses from the local service. Decision point: If the rebind fails (e.g., due to browser protections), try alternative ports or encodings; otherwise, proceed to exfiltrate or exploit the accessed service.

**Expected Output**: Browser console logs showing data fetched from the local endpoint (e.g., sensitive config or API response). Network traces reveal DNS responses switching from attacker's IP to 127.0.0.1 within seconds.
