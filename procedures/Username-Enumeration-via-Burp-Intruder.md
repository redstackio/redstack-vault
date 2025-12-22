---
id: b7f2e1d4-9a3c-4e5f-8b2a-3d6e7f8g9h0i
type: procedure
verified: true
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Account Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Enumeration]]'
  - '[[tags/Web Applications]]'
  - brute-force
  - username-enumeration
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: medium
detection_risk: high
validated: true
---

# Username-Enumeration-via-Burp-Intruder

## Summary

This procedure uses Burp Suite's Intruder tool to perform username enumeration on a web application's login form by brute-forcing potential usernames and identifying valid ones through differences in response lengths or content. It exploits applications that provide distinct error messages or response behaviors for invalid versus valid usernames paired with incorrect passwords, allowing attackers to confirm account existence without knowing the password.

## Description

Username enumeration is a common reconnaissance technique in web application attacks, often targeting login endpoints that leak information about valid accounts. This procedure focuses on using Burp Intruder to automate the brute-force process. By sending a series of login requests with a fixed invalid password and varying usernames from a wordlist, the attacker observes variations in server responses—such as longer error messages for valid usernames (e.g., "Invalid password for user X") versus generic ones (e.g., "Invalid credentials"). This method is effective against applications without rate limiting or CAPTCHA on login attempts. It maps to the MITRE ATT&CK framework under Discovery tactic TA0007 and technique T1087 (Account Discovery), commonly used in initial access phases to build a target user list for further attacks like password spraying or credential stuffing.

## Requirements

1. Burp Suite Professional edition (Community edition lacks Intruder).
2. Proxy interception setup (e.g., browser configured to route traffic through Burp at 127.0.0.1:8080).
3. A wordlist of potential usernames (e.g., from SecLists: https://github.com/danielmiessler/SecLists/tree/master/Usernames).
4. Network access to the target web application's login endpoint.
5. Basic knowledge of HTTP requests and Burp Suite navigation.

## Defense

Defensive measures include implementing consistent error messages for all login failures (e.g., always return "Invalid credentials"), enforcing rate limiting or account lockouts after failed attempts, deploying CAPTCHA challenges on suspicious login patterns, and monitoring application logs for repeated requests from the same IP or user-agent. Web Application Firewalls (WAFs) can detect and block brute-force patterns based on request volume and payload variations.

## Objectives

1. Identify valid usernames on the target application without requiring passwords.
2. Confirm account existence through response analysis.
3. Gather a list of enumerable accounts for subsequent attacks like password brute-forcing.
4. Validate the enumeration by attempting login with the discovered username and an invalid password, observing a specific "invalid password" error.

## Instructions

### Step 1: Intercept a Sample Login Request

**Context**: Begin by capturing a baseline login request using invalid credentials to understand the normal response structure. This establishes the payload position for Intruder and confirms the application's behavior for invalid usernames.

Configure your browser to proxy traffic through Burp Suite. Navigate to the target's login page and submit a login attempt with a random invalid username (e.g., "nonexistent") and password (e.g., "wrongpass"). In Burp's Proxy > HTTP history tab, locate and intercept the POST request to the login endpoint.

Forward the request and inspect the response in the Inspector or Repeater tab using [[tools/Burp-Suite]]. Note the response body, which should indicate invalid credentials (e.g., "Invalid username or password").

**Expected Output**: A 200 OK or 401/403 response with a generic error message of consistent length (e.g., 3264 bytes), confirming no account-specific details leak.

### Step 2: Send the Request to Intruder

**Context**: Transfer the captured request to Burp Intruder to prepare for automated payload injection. This allows systematic testing of multiple usernames while keeping other parameters (e.g., password) constant.

Right-click the request in Proxy > HTTP history (or Target > Site map) and select "Send to Intruder." Switch to the Intruder tab in Burp Suite.

In the Positions sub-tab, clear all payload positions (§) by clicking "Clear §" then add a single payload marker around the username parameter (e.g., change "username=nonexistent" to "username=§nonexistent§"). Set the attack type to "Sniper" for sequential testing of one payload position.

**Expected Output**: Intruder interface shows the request with the username parameter marked for payloads, ready for configuration.

### Step 3: Configure Payloads and Start the Attack

**Context**: Load a list of potential usernames into Intruder to automate the brute-force. This step simulates rapid login attempts to probe for valid accounts.

In the Payloads sub-tab, set Payload type to "Simple list." Paste or load a list of usernames (e.g., from SecLists Usernames directory: common names like "admin," "user," "austin"). Optionally, add payload processing rules for encoding if needed (e.g., URL encoding).

Click "Start attack" to launch the brute-force. Burp will send requests for each username with the fixed invalid password and collect responses.

**Expected Output**: Intruder results table populates with columns for request number, status, length, and response details. Most responses should have identical lengths (e.g., 3264 bytes for invalid usernames).

### Step 4: Analyze Responses for Valid Usernames

**Context**: Review the Intruder results to identify anomalies indicating valid usernames. Differences in response length or content reveal account existence.

Sort the results by the "Length" column in the Intruder attack window. Look for outliers—e.g., a response of 3266 bytes amid 3264-byte responses, suggesting a more detailed error like "Invalid password for [username]."

Click on suspicious responses to view full details in the Response pane. Note the username corresponding to the anomalous entry.

**Expected Output**: Identification of one or more valid usernames (e.g., "austin") based on response length or error message specificity.

### Step 5: Verify the Enumerated Username

**Context**: Confirm the discovery by manually attempting login with the identified username and an invalid password. This validates the enumeration without risking account lockout from further brute-forcing.

Return to the login page or use Burp Repeater. Submit a request with the discovered username (e.g., "austin") and a random invalid password. Intercept and forward if needed.

Observe the response, which should now specify an invalid password error, confirming the username exists.

**Expected Output**: Response like "Invalid password" (specific to the user), differing from the generic invalid credentials message, proving successful enumeration.
