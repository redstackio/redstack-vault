---
tags:
  - broken-access-control
  - information-disclosure
  - http-interception
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands:
  - '[[commands/http-get-personnel-php]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:51.992Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 30f414e3-c725-44e3-b174-fac490659a16
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass Access Control by Modifying Redirect Response with Burp Suite

## Summary

This procedure exploits a broken access control vulnerability in web applications where unauthorized requests to protected pages result in a 302 redirect response that includes the full HTML content of the sensitive page in the body. By intercepting the response with Burp Suite and removing the Location header, attackers can view leaked private information such as user names, emails, and internal details, facilitating further unauthenticated attacks like XSS or SQL injection.

## Description

The vulnerability occurs because the server fails to clear or restrict the response body during redirects for unauthorized users, embedding the protected page's HTML. This is common in PHP-based web apps with session management (e.g., JSESSIONID cookies). The attack requires proxying traffic through Burp Suite to modify responses in real-time. Prerequisites include network access to the target and a configured proxy. Expected outcomes include direct access to sensitive data without authentication, with high impact on confidentiality.

## Requirements

1. Burp Suite installed and running with proxy listener on localhost:8080
2. Browser configured to use Burp as proxy (e.g., manual proxy settings in Firefox)
3. Target web application with known protected endpoints (e.g., /personnel.php)
4. No authentication tokens; exploits public-facing nature

## Defense

Defensive measures and detection strategies:

- Ensure redirect responses for unauthorized access have empty or generic bodies (e.g., implement proper 401/403 handling without content)
- Use Content-Security-Policy (CSP) headers to prevent inline content rendering
- Monitor for anomalous proxy traffic or modified HTTP responses via WAF logs
- Implement server-side access checks that strip content before redirects

## Objectives

1. Intercept and alter HTTP responses to bypass client-side redirects
2. Disclose protected page content including user data
3. Enable reconnaissance for chained vulnerabilities like injection flaws

## Instructions

### Step 1: Configure Burp Suite Interception

**Context**: Prepare Burp to capture responses from the target application.

**Command** (No direct command; UI action):

Enable Live Interception in Burp Proxy under the Intercept tab.

> This sets Burp to pause on responses, allowing inspection and modification. Expected output: Intercept tab active with "Intercept is on" message.

### Step 2: Request Protected Endpoint and Intercept

**Context**: Trigger the vulnerable response by accessing a protected page.

**Command** ([[commands/http-get-personnel-php]]):
```bash
curl -X GET "https://target/personnel.php" -H "Host: target" -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" -H "Accept-Language: ru,en-US;q=0.7,en;q=0.3" -H "Accept-Encoding: gzip, deflate" -H "Cookie: JSESSIONID=example; __VCAP_ID__=example; TS01771652=example; TS01771652031=example; TSf7f79454027=example" -H "Connection: close" --insecure
```

> Send via browser proxied through Burp or curl; right-click in Burp Proxy history and select "Do intercept > Response to this request". Expected output: 302 response with Location: login.php and body containing full protected HTML.

### Step 3: Modify and Forward Response

**Context**: Remove the redirect to expose the content.

**Command** (UI modification in Burp):

In the Intercept tab, delete the "Location: login.php" line and click Forward.

> This prevents the browser from redirecting, rendering the sensitive body directly. Expected output: Browser shows leaked HTML with private data.

### Step 4: Analyze Disclosed Content

**Context**: Extract and document the leaked information.

**Command** (No command; inspection):

Use Burp Inspector or browser dev tools to parse the HTML for data like emails and names.

> Focus on elements from pages like /personnel.php. Expected output: Visible user lists, emails, and internal details enabling further testing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/http-get-personnel-php]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- broken-access-control
- information-disclosure
- web-vulnerability
