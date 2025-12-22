---
id: a1efe8b2-fb7a-439a-91a7-2b2586a6da71
name: URL-Scheme-SSRF-via-Dictionary-Attack
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:37.820400+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/Dict]]'
  - '[[tags/Server-Side Request Forgery]]'
  - '[[tags/SSRF exploitation via URL Scheme]]'
  - ssrf
  - url-scheme
  - dictionary-attack
commands:
  - '[[commands/curl-send-ssrf-dict-url]]'
platforms:
  - Web
tools: []
validated: true
---

# URL-Scheme-SSRF-via-Dictionary-Attack

## Summary

This procedure exploits a Server-Side Request Forgery (SSRF) vulnerability in a web application by abusing URL schemes, specifically the Dictionary (dict://) protocol, through a dictionary-based brute-force approach to identify and trigger vulnerable endpoints. It allows attackers to force the server to make unauthorized requests to internal or external resources, potentially bypassing firewalls and accessing sensitive data like metadata services or internal APIs.

## Description

URL Scheme SSRF involves manipulating input fields in a web application that accept URLs, tricking the server into interpreting and fetching from attacker-controlled schemes like dict://, gopher://, or file://. In this dictionary attack variant, the attacker systematically tests multiple URL variations using a wordlist to discover which parameters or endpoints are vulnerable to SSRF. This is particularly effective against applications that parse URLs without proper validation, such as those handling redirects, image fetches, or API callbacks. The attack targets public-facing web apps and can lead to internal network reconnaissance, data exfiltration, or remote code execution if chained with other vulnerabilities. It assumes the target is a web server (e.g., PHP-based like the example ssrf.php) that processes user-supplied URLs server-side. Success relies on the server's ability to resolve and connect to the specified scheme, often evading WAFs since dict:// mimics legitimate dictionary lookups.

## Requirements

1. Network access to the vulnerable web application (public-facing endpoint).
2. Knowledge of the application's URL structure and input parameters that accept URLs (e.g., via reconnaissance or source code review).
3. A wordlist or dictionary of potential URL variations, parameters, or payloads (e.g., common dict:// formats targeting internal hosts).
4. Tools like curl or Burp Suite for sending HTTP requests; a listener (e.g., netcat) on the attacker's side if exfiltrating responses.
5. Basic understanding of URL encoding and protocol handlers on the target server (e.g., PHP's file_get_contents() or curl functions).

## Defense

- Implement strict URL validation and whitelisting to allow only trusted schemes (e.g., http/https) and domains.
- Use a Web Application Firewall (WAF) to detect anomalous URL patterns, such as non-standard schemes like dict:// or high request volumes indicative of dictionary attacks.
- Disable unnecessary URL protocol handlers on the server (e.g., restrict curl or fopen to safe schemes).
- Monitor server logs for outbound connections to unexpected ports/protocols and implement network segmentation to limit internal access from web servers.
- Rate-limit input fields and employ CAPTCHA or behavioral analysis to thwart automated dictionary attacks.

## Objectives

1. Identify vulnerable URL parameters in the target application through brute-force testing.
2. Force the server to make requests to attacker-controlled or internal resources via the dict:// scheme.
3. Exfiltrate sensitive data, such as internal metadata or service responses, by capturing server-side fetches.
4. Achieve initial access or reconnaissance on internal networks by bypassing external-facing restrictions.

## Instructions

### Step 1: Prepare Dictionary Wordlist

**Context**: Create or obtain a wordlist of potential dict:// URL variations to test against the target. This includes different hosts, ports, words, databases, and authentication strings to cover common SSRF payloads targeting internal services.

Focus on payloads that probe for open ports or extract data, such as dict://127.0.0.1:11211/d:word:database:1 for Memcached or similar.

### Step 2: Test SSRF Vulnerability with Dictionary Attack

**Context**: Use a tool to automate sending requests with dictionary payloads to the vulnerable endpoint (e.g., ssrf.php?url=). Monitor responses for signs of SSRF success, such as delays indicating internal connections or leaked data in error messages.

**Command** ([[commands/curl-send-ssrf-dict-url]]):
```bash
curl -X POST "http://target.com/ssrf.php" -d "url=dict://$_USER;$_AUTH@$_HOST:$_PORT/d:$_WORD:$_DATABASE:$_N"
```

> This command sends a POST request to the target endpoint with a dict:// URL payload. Replace placeholders with wordlist values during the attack. Iterate through the dictionary using a script or tool like Burp Intruder. Expected output includes HTTP 200/redirect if processed, or error leaks revealing internal details (e.g., connection timeouts for closed ports, data dumps for open ones). If successful, the server will attempt to connect to the specified dict host/port, potentially allowing data exfiltration if you're listening.

### Step 3: Analyze Responses and Verify Exploitation

**Context**: Review server responses for indicators of SSRF, such as partial data from internal services or timing differences. If a payload triggers an internal fetch, chain it with further payloads to escalate (e.g., to metadata endpoints).

Use tools like Wireshark on the attacker side if exfiltrating, or check application logs if accessible. Success is confirmed by observing unauthorized server-side requests.
