---
id: 73c998d2-d9ec-4231-8bc3-3a5e4c2150ae
name: Authentication-Bypass-via-SQL-Injection-Using-Burp-Intruder
type: procedure
verified: true
submitted: true
created_at: '2020-07-23T10:59:25.216198+00:00'
updated_at: '2023-05-26T01:13:57.561193+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - broken authentication
  - Burp
  - hacking
  - injection
  - SQL
  - sqli
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Authentication-Bypass-via-SQL-Injection-Using-Burp-Intruder

## Summary

This procedure uses Burp Suite's Intruder tool to automate the testing of SQL injection payloads in a web application's login form, attempting to bypass authentication by injecting payloads into the username and password fields. Success is determined by analyzing response differences such as HTTP status codes (e.g., 302 redirect), content length changes, or the presence of authentication cookies, allowing unauthorized access without valid credentials.

## Description

SQL injection in authentication forms is a common vulnerability where unsanitized user input in login fields can manipulate backend database queries, often allowing attackers to bypass checks like 'SELECT * FROM users WHERE username = '$user' AND password = '$pass''. Burp Intruder automates the brute-forcing of payloads across these fields, using attack types like Pitchfork to pair username and password payloads systematically. This is particularly effective against classic SQLi variants like tautologies (' OR 1=1 --) or union-based attacks. The procedure assumes a POST-based login form and requires interception via Burp Proxy. It maps to MITRE ATT&CK technique T1190 (Exploit Public-Facing Application) under Initial Access, as it targets web apps directly. Use this in controlled environments like pentests to identify broken access control.

## Requirements

1. Burp Suite Professional edition (Community lacks full Intruder features).
2. Browser configured to proxy traffic through Burp (e.g., FoxyProxy extension or manual settings: 127.0.0.1:8080).
3. Access to the target web application's login page (no prior authentication needed).
4. A list of SQL injection payloads for username and password fields (e.g., common tautologies, error-based, or blind payloads).
5. Basic knowledge of HTTP requests and SQL syntax.

## Defense

Defensive measures and detection strategies:

- Implement prepared statements or parameterized queries in backend code to prevent SQL injection.
- Use web application firewalls (WAFs) like ModSecurity to block suspicious payloads in login requests.
- Enable logging of failed login attempts and anomalous response patterns (e.g., multiple 302s from the same IP).
- Rate-limit login attempts to detect brute-force activity.
- Monitor for unusual Burp-like user agents or proxy traffic patterns in access logs.

## Objectives

1. Identify if the login form is vulnerable to SQL injection for authentication bypass.
2. Automate payload testing to efficiently discover working injections.
3. Gain unauthorized access to the application upon successful bypass.
4. Validate success through response analysis without manual trial-and-error.

## Instructions

### Step 1: Intercept the Login Request

**Context**: Begin by capturing the HTTP POST request from the login form to prepare it for payload injection in Burp Intruder. This establishes the baseline request structure, including the username and password parameters.

Navigate to the target login page in your proxied browser. Enter dummy credentials (e.g., username: 'test', password: 'test') and submit the form. In Burp Suite's Proxy tab, ensure interception is enabled to capture the outgoing POST request.

**Expected Output**: A captured HTTP POST request in Burp Proxy, showing form parameters like username=test&password=test in the request body.

### Step 2: Send Request to Intruder

**Context**: Transfer the intercepted request to the Intruder tool, where payload positions will be defined. This allows Burp to treat the request as a template for automated attacks.

In the Proxy intercept tab, right-click the captured request and select "Send to Intruder". Switch to the Intruder tab in Burp.

**Expected Output**: The request appears in Intruder's Target and Positions sub-tabs, ready for payload marker addition.

### Step 3: Define Payload Positions

**Context**: Mark the username and password fields as injection points (payload positions) so Intruder can replace them with SQL payloads. Use the default § markers or manually add them.

In the Positions sub-tab, highlight the value of the username parameter (e.g., test) and click "Add §" to mark it as position 1. Repeat for the password parameter as position 2. Clear any unnecessary positions if present.

**Expected Output**: The request template shows §username§ and §password§ markers, indicating two payload positions.

### Step 4: Configure Attack Type

**Context**: Select an attack type that suits pairing separate payload lists for username and password, such as Pitchfork, to run combinations efficiently without exponential growth.

In the Positions sub-tab, set the attack type dropdown to "Pitchfork". This will iterate through payloads in list 1 (usernames) and list 2 (passwords) in parallel.

**Expected Output**: Attack type updated to Pitchfork, with positions assigned to lists 1 and 2.

### Step 5: Load Username Payloads

**Context**: Provide a list of SQL injection payloads for the username field, focusing on common bypass techniques like tautologies or comment tricks to alter the query logic.

Switch to the Payloads sub-tab. For Payload Sets > Payload Options > Position 1 (username), select "Simple list" and add payloads such as:
- ' OR '1'='1
- admin' --
- ' OR 1=1 #
- administrator' /*
Click "Update" to load the list.

**Expected Output**: List 1 populated with 4+ SQL payloads for username injection.

### Step 6: Load Password Payloads

**Context**: Add complementary SQL payloads for the password field to test combined injections, ensuring coverage of scenarios where the bypass relies on both fields.

For Position 2 (password), select "Simple list" and add payloads such as:
- ' OR '1'='1
- ' --
- 1' OR '1'='1
- ' #
Click "Update".

**Expected Output**: List 2 populated with SQL payloads for password injection.

### Step 7: Start the Attack and Analyze Results

**Context**: Launch the Intruder attack to send payloads and monitor responses for indicators of successful bypass, such as redirects or session cookies.

Click the "Start attack" button. In the results window, sort columns by Status Code and Length. Look for anomalies: successful logins often return 302 (redirect) with shorter length or Set-Cookie headers, unlike 200/401 failures.

**Expected Output**: A table of requests with varying payloads; successful ones show 302 status, reduced response length (e.g., redirect page vs. error), and headers like Set-Cookie: session=abc123.

### Step 8: Verify Bypass

**Context**: Confirm the bypass by replaying a successful payload request and checking if it grants access to protected areas.

Right-click a successful payload row in Intruder results and select "Send to Repeater". In Repeater, submit the request and follow any redirects to verify authenticated access (e.g., dashboard load without creds).

**Expected Output**: Successful navigation to post-login page, confirming authentication bypass.
