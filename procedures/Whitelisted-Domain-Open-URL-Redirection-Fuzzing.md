---
id: ae1b3048-5e3b-49c1-acaf-27965af8d364
name: Whitelisted-Domain-Open-URL-Redirection-Fuzzing
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:31.776465+00:00'
updated_at: '2023-04-10T20:23:06.271279+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - '[[techniques/Phishing|T1566 - Phishing]]'
  - '[[techniques/Spearphishing Link|T1566.001 - Spearphishing Link]]'
sub_techniques: []
tags:
  - '[[tags/Fuzzing]]'
  - '[[tags/Open URL Redirection]]'
  - phishing
  - web-vulnerability
commands:
  - '[[commands/prepare-open-redirect-payloads-with-whitelisted-domain]]'
platforms:
  - Web
tools: []
validated: true
---

# Whitelisted-Domain-Open-URL-Redirection-Fuzzing

## Summary

This procedure tests web applications for open URL redirection vulnerabilities by fuzzing with payloads restricted to whitelisted domains. It prepares customized payload files from a base template, allowing testers to simulate redirects to trusted domains that might still enable phishing or bypass filters, helping identify misconfigurations in redirection logic.

## Description

Open URL redirection vulnerabilities occur when a web application allows user-supplied URLs to redirect users without proper validation, potentially leading to phishing attacks by mimicking legitimate sites. This procedure focuses on whitelisted domains—those explicitly allowed by the application—to test if the filtering is effective or if bypasses exist (e.g., via path traversal, encoding, or subdomain tricks). It assumes a base payload file (Open-Redirect-payloads.txt) containing common open redirect patterns with a placeholder domain. The technique generates tailored payloads for specific whitelisted domains, which can then be fed into tools like Burp Suite for fuzzing against redirection endpoints (e.g., /redirect?url=). This is useful in red team engagements targeting login flows, email links, or OAuth callbacks where redirects are common. Success indicates potential for phishing via trusted-looking URLs, with outcomes including redirected HTTP responses confirming the vuln.

## Requirements

1. Access to the target web application (e.g., via browser or proxy like Burp Suite).
2. A pre-defined list of whitelisted domains provided by the application or reconnaissance (e.g., company.com, trusted-partner.net).
3. Base payload file: Open-Redirect-payloads.txt containing redirect patterns with placeholder 'www.whitelisteddomain.tld'.
4. Unix-like environment (Linux/macOS) for sed and awk commands, or compatible tools on Windows (e.g., Git Bash).
5. Optional: Burp Suite or similar for injecting payloads into requests.

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation using whitelists with exact domain matching, rejecting any non-exact matches or relative paths.
- Use redirect-to flags or server-side validation to ensure redirects only go to internal or verified endpoints.
- Monitor application logs for suspicious redirect patterns, such as high volumes of requests to whitelisted domains from unusual sources.
- Employ Web Application Firewalls (WAFs) to block common open redirect payloads and rate-limit fuzzing attempts.

## Objectives

1. Identify if the target application allows open redirects to whitelisted domains, potentially enabling phishing.
2. Test the robustness of domain whitelisting against bypass techniques like subdomain manipulation or protocol relative URLs.
3. Generate evidence (e.g., successful redirect logs) for remediation, such as improving input sanitization.

## Instructions

### Step 1: Prepare Environment

**Context**: Ensure the base payload file exists and contains standard open redirect patterns (e.g., ?url=//www.whitelisteddomain.tld/, /redirect?url=https://www.whitelisteddomain.tld/login). This step sets up the file for customization.

Create or verify Open-Redirect-payloads.txt if not present.

> Download a standard open redirect payload list from resources like PayloadsAllTheThings and replace placeholders accordingly.

### Step 2: Generate Customized Payloads

**Context**: Use the command to replace the placeholder domain in the base file with a specific whitelisted domain and append a full HTTPS URL variant. This creates a Burp-compatible file (e.g., Open-Redirect-payloads-burp-www.example.com.txt) for fuzzing.

**Command** ([[commands/prepare-open-redirect-payloads-with-whitelisted-domain]]):
```bash
WHITELISTEDDOMAIN="www.example.com" && sed 's/www.whitelisteddomain.tld/'"$WHITELISTEDDOMAIN"/' Open-Redirect-payloads.txt > Open-Redirect-payloads-burp-"$WHITELISTEDDOMAIN".txt && echo "$WHITELISTEDDOMAIN" | awk -F. '{print "https://"$0"."$NF}' >> Open-Redirect-payloads-burp-"$WHITELISTEDDOMAIN".txt
```

> This command substitutes the placeholder, saves to a new file, and appends an HTTPS version of the domain (e.g., https://www.example.com.com for potential bypass testing). Expected output: A new .txt file with ~50-100 payloads tailored to the domain. Verify by checking file contents with cat or a text editor—no errors in substitution.

### Step 3: Fuzz the Target Endpoint

**Context**: Load the generated payload file into a fuzzing tool and test against suspected redirection parameters (e.g., ?next=, ?redirect_uri=). Intercept with a proxy to observe responses.

Configure Burp Intruder or similar: Set payload positions in the URL/query and load the .txt file as the payload source. Send requests to the target (e.g., https://target.com/login?redirect=$_PAYLOAD).

> Monitor for 3xx redirect responses to the whitelisted domain. If redirects succeed without validation errors, the vuln is confirmed. Expected output: HTTP 302/301 with Location header pointing to the payload URL.

### Step 4: Validate and Document

**Context**: Confirm the redirect leads to a controllable page and note any bypasses (e.g., if //example.com works but https://example.com doesn't).

Test a sample payload manually via curl:
```bash
curl -i "https://target.com/redirect?url=https://www.example.com/malicious"
```

> Look for successful redirects in the Location header. Document vulnerable endpoints and whitelisted domains that failed filtering for reporting.
