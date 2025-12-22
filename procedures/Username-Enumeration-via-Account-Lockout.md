---
id: 5b744451-0553-4b54-ad8e-9f51a02824dd
name: Username-Enumeration-via-Account-Lockout
type: procedure
verified: true
submitted: false
created_at: '2020-09-02T16:51:28.290525+00:00'
updated_at: '2023-05-26T18:41:31.729360+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Account Discovery]]'
sub_techniques:
  - '[[T1087.001]]'
tags:
  - enumeration
  - reconnaissance
  - account-discovery
  - lockout
commands:
  - '[[commands/curl-login-attempt]]'
platforms:
  - Web
tools:
  - '[[tools/cURL]]'
  - '[[tools/Burp-Suite]]'
validated: true
---

# Username-Enumeration-via-Account-Lockout

## Summary

This procedure enumerates valid usernames on a web application's login page by performing repeated failed login attempts with guessed usernames. By observing differences in error messages or behaviors—such as account lockout notifications for valid users versus generic errors for invalid ones—attackers can identify legitimate accounts. This technique exploits poor error handling in authentication systems and is commonly used during reconnaissance to build a list of target usernames for further attacks like password spraying.

## Description

Username enumeration via account lockout targets web-based login forms where the application distinguishes between valid and invalid usernames in its responses. For example, after 5 failed login attempts with a valid username, the system might lock the account and display a message like "Account locked due to too many failed attempts," while invalid usernames might only show "Invalid username or password." This difference allows systematic guessing of usernames (e.g., common names like admin, user, or from public sources). The technique requires no special privileges but relies on the target's lockout policy being predictable and verbose. It maps to MITRE ATT&CK's Account Discovery tactic, as it reveals active user accounts. Use this in controlled red team environments or authorized testing only, as it can lead to denial-of-service if lockouts affect legitimate users.

## Requirements

1. Network access to the target's login endpoint (e.g., HTTP/HTTPS).
2. Knowledge of the login form structure (username/password fields, submission method).
3. Awareness of the account lockout threshold (e.g., 5 failed attempts; test manually first).
4. Tools like curl for automation or Burp Suite for manual interception and observation.
5. A list of potential usernames to test (e.g., from OSINT or common patterns).

## Defense

Defensive measures include implementing consistent error messages (e.g., always "Invalid credentials") without revealing username validity, rate limiting login attempts per IP, using CAPTCHA after failures, and monitoring for anomalous login patterns. Enable logging of failed authentications to detect enumeration attempts.

## Objectives

1. Identify valid usernames by triggering distinct lockout responses.
2. Compile a list of confirmed accounts for subsequent attacks.
3. Avoid detection by spacing attempts or using proxies.

## Instructions

### Step 1: Identify Login Endpoint and Test Error Responses

**Context**: First, locate the login page and understand the baseline error messages for valid vs. invalid inputs. This establishes the difference that will indicate enumeration success.

**Command** ([[commands/curl-login-attempt]]):
```bash
curl -X POST -d "username=nonexistent&password=wrong" https://target.com/login -c cookies.txt
```

> Send a single failed login attempt with a likely invalid username. Observe the response body for generic errors like "Invalid username or password." Repeat with a known valid username (if available) or common ones to note differences, such as "User not found" vs. "Incorrect password."

### Step 2: Prepare Username List and Lockout Threshold

**Context**: Gather potential usernames and determine the lockout limit to avoid unnecessary attempts. Common sources include public directories, social media, or patterns like first.last@domain.com.

Create a file `usernames.txt` with one username per line (e.g., admin, user, john.doe).

Test the lockout threshold manually: Attempt logins with a dummy valid-like username until lockout triggers (e.g., after 5 tries, response changes to "Account locked").

### Step 3: Automate Failed Login Attempts

**Context**: For each username, perform repeated failed logins (e.g., 6 attempts) using a weak password to trigger lockout if valid. Monitor responses for lockout indicators.

**Command** ([[commands/curl-login-attempt]]):
```bash
for i in {1..6}; do curl -X POST -d "username=$USERNAME&password=wrongpass" https://target.com/login -b cookies.txt -w "%{http_code} %{time_total}s\n"; done
```

> Loop through attempts for each username in `usernames.txt`. Use a bash script to iterate: `while read username; do ...; done < usernames.txt`. Replace `$USERNAME` with the variable. If the response after attempts includes lockout language (e.g., HTTP 200 with "locked" text), mark as valid.

### Step 4: Log and Analyze Responses

**Context**: Capture all responses to differentiate outcomes. Valid usernames will show lockout after threshold; invalid ones remain generic.

Save outputs to files: `curl ... > response-$USERNAME.txt`. Grep for keywords like "lockout," "suspended," or status changes (e.g., `grep -i lock response-*.txt`).

### Step 5: Reset and Verify

**Context**: If possible, wait for lockout timers to expire or use self-service reset to confirm. Avoid excessive testing to prevent alerting defenders.

Manually attempt a valid login post-lockout to verify the effect, or monitor for email notifications if applicable.

### Step 6: Compile Valid Usernames

**Context**: Aggregate results into a usable list for further reconnaissance or attacks.

Create `valid_users.txt` with confirmed usernames. Review logs for false positives (e.g., rate limits mimicking lockouts).
