---
id: 34a353fa-c241-448c-91cc-38d990537d00
name: User-Enumeration-via-Response-Differences-with-Burp-Intruder
type: procedure
verified: true
submitted: true
created_at: '2020-09-01T15:28:11.573734+00:00'
updated_at: '2023-05-26T18:09:38.131345+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Account Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Enumeration]]'
  - '[[tags/Web Applications]]'
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
---

# User-Enumeration-via-Response-Differences-with-Burp-Intruder

## Summary

This procedure demonstrates how to enumerate valid usernames and passwords on a web application's login page by identifying subtle differences in error response messages using Burp Suite's Intruder tool. When brute-force attempts yield inconsistent error messages (e.g., a missing punctuation mark for valid credentials), these differences can reveal valid accounts without triggering rate limits or alerts.

## Description

Many web applications fail to implement consistent error messaging during login attempts, leading to information disclosure vulnerabilities. For example, an error like "Invalid username or password" might appear fully for invalid usernames but lack a period ("Invalid username or password") for valid ones. This procedure captures a sample login request, uses Burp Intruder to automate payload injection into username and password fields, extracts response differences via grep-extract, and identifies valid credentials. It targets public-facing login endpoints and requires proxy interception. The technique is effective against applications without proper blind authentication or CAPTCHA protections, allowing attackers to build a list of valid accounts for further exploitation like credential stuffing or account takeover.

## Requirements

1. Access to the target web application's login page (e.g., via browser).
2. Burp Suite Professional or Community Edition installed and configured as a proxy.
3. A wordlist of potential usernames (e.g., from SecLists: https://github.com/danielmiessler/SecLists/tree/master/Usernames).
4. Browser configured to route traffic through Burp proxy (e.g., FoxyProxy extension).
5. Basic knowledge of HTTP requests and Burp Suite navigation.

## Defense

Defensive measures and detection strategies:

- Implement consistent, generic error messages (e.g., always "Invalid credentials") without variations that leak information.
- Enforce rate limiting, CAPTCHA, or multi-factor authentication on login endpoints to hinder automated enumeration.
- Monitor for unusual traffic patterns, such as high volumes of login requests from a single IP or proxy signatures (e.g., Burp's default User-Agent).
- Use web application firewalls (WAFs) to detect and block Intruder-like payload fuzzing.
- Enable logging of failed logins and alert on anomalies in response times or message patterns.

## Objectives

1. Identify valid usernames by analyzing subtle response differences during username fuzzing.
2. Enumerate corresponding valid passwords using the same method on discovered usernames.
3. Successfully authenticate with enumerated credentials to confirm access.
4. Compile a list of valid accounts for subsequent attacks.

## Instructions

### Step 1: Capture Sample Login Request

**Context**: Perform a failed login with random credentials to capture the baseline HTTP POST request to the login endpoint. This provides the template for Intruder attacks.

Intercept the request using Burp's Proxy tab. Navigate to the login page, enter a random username (e.g., "randomuser") and password (e.g., "randompass"), and submit. In Burp Proxy > HTTP History, right-click the login POST request and select "Send to Intruder."

**Expected Output**: A captured POST request in the format:

```http
POST /login HTTP/1.1
Host: target.com
Content-Type: application/x-www-form-urlencoded

username=randomuser&password=randompass
```

### Step 2: Configure Intruder Attack Type and Positions

**Context**: Set up Intruder to perform a sniper attack, targeting the username field for payload injection. This allows systematic testing of username candidates.

In the Intruder Positions tab, select "Sniper" as the attack type. Clear all payload positions (§), then highlight the username value in the request body and click "Add §" to mark it for fuzzing (e.g., username=§randomuser§).

**Expected Output**: The request body updated with payload markers:

```http
username=§randomuser§&password=randompass
```

### Step 3: Load Username Payloads

**Context**: Supply a list of potential usernames to test against the login endpoint, enabling automated enumeration.

In the Intruder Payloads tab, under Payload Sets > Payload Options > Input, select "Simple list" and load or paste usernames from a wordlist (e.g., common names like admin, user, accounting from SecLists).

**Expected Output**: Payload list populated with entries like:

- admin
- user
- accounting

### Step 4: Set Up Grep-Extract for Response Analysis

**Context**: Configure extraction to pull error messages from responses, highlighting differences between valid and invalid attempts.

Switch to the Intruder Options tab > Grep - Extract. Click "Add" and, using a sample response from the attack, scroll to the error message section (e.g., body text). Highlight the full error string like "Invalid username or password." and add it as an extraction rule.

**Expected Output**: Extraction rule added, e.g., capturing "Invalid username or password" from response bodies.

### Step 5: Execute Username Enumeration Attack

**Context**: Run the Intruder attack to fuzz usernames and observe extracted responses for anomalies indicating valid accounts.

Click "Start Attack" in the Intruder control panel. Once complete, review the results table. Sort by response length or manually inspect extracted messages for differences (e.g., missing period in "Invalid username or password" for valid usernames like "accounting").

**Expected Output**: Intruder results table with columns for payload, status, length, and extracted grep items. Anomalous responses (e.g., shorter error without ".") flag valid usernames.

### Step 6: Repeat for Password Enumeration

**Context**: Using a discovered valid username, repeat the process to enumerate passwords, targeting the password field instead.

Return to Intruder Positions, clear username markers, and add § to the password value (e.g., password=§randompass§). Load a password wordlist in Payloads. Reconfigure grep-extract if needed for password-specific errors. Start the attack and analyze for similar response differences.

**Expected Output**: Valid password identified via response anomaly (e.g., successful login indicators or altered error text).

### Step 7: Verify Login with Enumerated Credentials

**Context**: Confirm the enumerated username-password pair grants access, validating the enumeration success.

Return to the browser, enter the discovered credentials (e.g., username: accounting, password: discoveredpass), and submit the login form. Intercept via Burp to confirm no errors.

**Expected Output**: Successful redirection to dashboard or authenticated session (e.g., 302 redirect or welcome message).

