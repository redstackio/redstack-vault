---
id: 4c54344f-b966-4c34-b318-9adbf99343e4
name: Brute-Force-MongoDB-Login-via-NoSQL-Regex-Injection
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:31.538401+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Brute Force]]'
sub_techniques: []
tags:
  - blind-nosql
  - nosql-injection
  - post-urlencoded
  - brute-force
  - mongodb
commands:
  - '[[commands/run-python-mongodb-brute-force-script]]'
platforms:
  - Web
tools: []
validated: true
---

# Brute-Force-MongoDB-Login-via-NoSQL-Regex-Injection

## Summary

This procedure demonstrates brute forcing a MongoDB login credential by exploiting a NoSQL injection vulnerability in the password field of a URL-encoded POST request. It uses the MongoDB $regex operator to test password prefixes incrementally, character by character, until the full password is discovered. This is effective against applications that do not properly sanitize input in authentication queries, allowing blind brute forcing without direct error feedback.

## Description

In vulnerable MongoDB-backed web applications, the login form may construct queries like {user: "admin", pass: "guess"}, but if pass is injectable, an attacker can append [$regex] => /^prefix/ to validate partial passwords. The script sends POST requests with escalating password prefixes, checking for a successful redirect (e.g., 302 to /dashboard) to confirm matches. This technique targets weak or default credentials in exposed MongoDB instances or web apps using MongoDB for auth. It assumes the application redirects on successful login and that the NoSQLi allows regex without escaping. The target environment is a web application with a login endpoint over HTTP/HTTPS, typically on port 80/443. Expected outcomes include recovering the full password, enabling further access to the database or dashboard for data exfiltration or persistence.

## Requirements

1. Network access to the target's login endpoint (e.g., http://target.com/login).
2. Python 3 environment with the requests library installed (pip install requests).
3. Knowledge of the target username (e.g., 'admin'; can be enumerated separately if needed).
4. The target application must be vulnerable to NoSQL injection in the password field, allowing $regex payloads.

## Defense

Defensive measures and detection strategies:

- Use strong, complex passwords (at least 12 characters, mixed case, numbers, symbols) to increase brute force resistance.
- Implement rate limiting on login attempts (e.g., 5 failures per minute per IP) to slow or block automated attacks.
- Sanitize and validate all user inputs in authentication queries; use parameterized queries or MongoDB's built-in escaping to prevent injection.
- Monitor application logs for suspicious patterns, such as repeated POST requests with regex-like payloads or high failure rates from single IPs.
- Deploy Web Application Firewalls (WAFs) to detect and block NoSQL injection attempts, including $regex operators in payloads.
- Enable MongoDB authentication and restrict network access to trusted IPs only.

## Objectives

1. Incrementally discover the full password for a known username (e.g., admin) via blind NoSQL injection.
2. Achieve successful authentication to access the MongoDB dashboard or database.
3. Enable unauthorized data access, modification, or exfiltration from the MongoDB instance.

## Instructions

### Step 1: Prepare the Brute Force Script

**Context**: Obtain and configure the Python script that handles the incremental brute forcing using $regex payloads. This step ensures the code is ready with target-specific details.

Save the script from [[codes/Python-Script-for-MongoDB-Password-Brute-Force-via-Regex]] to a file named `brute_mongo.py`. Edit the hardcoded values: set `username` to the target username (e.g., "admin") and `u` to the login endpoint URL (e.g., "http://target.com/login").

**Expected Output**: A configured Python file ready for execution.

### Step 2: Verify Dependencies

**Context**: Ensure the Python environment has the required library to send HTTP requests and handle SSL warnings.

Install the requests library if not present:

```bash
pip install requests
```

**Expected Output**: Successful installation confirmation, e.g., "Successfully installed requests-2.31.0".

### Step 3: Execute the Brute Force Attack

**Context**: Run the script to begin sending POST requests with escalating regex payloads, building the password character by character based on successful login responses.

**Command** ([[commands/run-python-mongodb-brute-force-script]]):
```bash
python brute_mongo.py
```

> This command executes the script, which iterates through printable characters, constructs payloads like `pass[$regex]=^currentprefix+c`, and sends them via POST. It appends matching characters to the password upon detecting a 302 redirect to the dashboard. The script runs indefinitely until manually stopped or the full password is built (monitor console output for progress). Why: This automates the blind guessing, leveraging the injection to validate prefixes without needing a wordlist.

**Expected Output**: Console prints like "Found one more char : a", "Found one more char : ab", building up to the full password (e.g., "Found one more char : secretpass"). If no match, it continues trying characters without output.
