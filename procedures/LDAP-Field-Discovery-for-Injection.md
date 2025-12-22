---
type: procedure
description: >-
  Discover valid LDAP attributes by testing a wordlist against a target web
  application vulnerable to LDAP injection.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - '[[techniques/Account Discovery|T1087 - Account Discovery]]'
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
sub_techniques: []
tags:
  - '[[tags/Discover valid LDAP fields]]'
  - '[[tags/LDAP Injection]]'
  - '[[tags/Scripts]]'
commands:
  - '[[commands/python-run-ldap-discovery]]'
platforms:
  - Web
tools: []
validated: true
---

# LDAP-Field-Discovery-for-Injection

## Summary

This procedure identifies valid LDAP attributes in a web application by injecting crafted LDAP statements via POST requests, using a wordlist of common attributes. It detects which fields return a 'TRUE CONDITION' in responses, enabling further LDAP injection attacks to escalate access or extract data.

## Description

LDAP injection exploits web applications that build LDAP queries from user input without proper sanitization. By inserting malicious LDAP syntax, attackers can alter query logic to bypass authentication or enumerate directory information. This procedure focuses on reconnaissance: it systematically tests potential attribute names (e.g., cn, sn, mail) to find valid ones. The target is typically a login form that queries an LDAP server. Success reveals attributes for crafting more targeted injections, such as boolean-based or union-based LDAP attacks. This maps to discovery tactics by enumerating account-related fields and initial access via exploitation of remote services like LDAP directories.

## Requirements

1. Network access to the target web application's login endpoint (e.g., HTTP/HTTPS).
2. Python 3 installed with the 'requests' library (pip install requests).
3. A wordlist file ('dic') containing common LDAP attributes (e.g., cn, uid, sn, mail, memberOf).
4. Basic knowledge of the target's login form parameters (e.g., 'login' and 'password' fields).

## Defense

- Implement strict input validation and LDAP query parameterization to prevent injection.
- Use least-privilege accounts for LDAP bindings and monitor query logs for anomalies like null bytes (\x00) or unexpected attribute tests.
- Employ web application firewalls (WAFs) to detect and block crafted LDAP payloads in POST data.
- Enable logging of all LDAP operations and alert on boolean true conditions or excessive query volumes from single sources.

## Objectives

1. Identify valid LDAP attributes that can be exploited in injection payloads.
2. Build a list of confirmed fields for use in advanced LDAP injection techniques.
3. Validate the vulnerability without causing denial of service.

## Instructions

### Step 1: Prepare the Environment

**Context**: Set up the wordlist and target details to ensure the script has the necessary inputs. This step avoids runtime errors and customizes the test to the target's form.

Create or obtain a wordlist file named 'dic' with one LDAP attribute per line (e.g., cn\nuid\nsn\nmail). Update the script's URL variable to point to the target's login endpoint.

**Expected Output**: A ready-to-run script file and wordlist.

### Step 2: Execute the Discovery Script

**Context**: Run the Python script to iterate through the wordlist, injecting each attribute into an LDAP payload. The payload crafts a statement like '*)('+attribute+'=*)\x00' to test for valid fields by checking for 'TRUE CONDITION' in the response, indicating a match.

Save the script from [[codes/Python-LDAP-Field-Discovery-Script]] to a file (e.g., ldap_discovery.py), ensure the URL and wordlist path are correct, then execute it using [[commands/python-run-ldap-discovery]].

```bash
python3 ldap_discovery.py
```

> The script sends POST requests with the payload in the 'login' field and a dummy 'password'. It collects attributes where the response contains 'TRUE CONDITION', printing the list of valid fields at the end.

**Expected Output**: A printed list of valid attributes, e.g., ['cn', 'mail', 'sn']. If no fields are found, the list will be empty, indicating potential misconfiguration or no vulnerability.

### Step 3: Verify and Analyze Results

**Context**: Review the output to confirm valid fields and prepare for follow-on attacks. This step includes manual verification if needed.

Check the console output for the fields list. Manually test one valid attribute via a tool like Burp Suite by sending a POST with the payload to confirm the 'TRUE CONDITION' response.

**Expected Output**: Confirmed list of injectable attributes; successful manual test shows the expected response without errors.

> If results are inconsistent, adjust the payload for the specific application (e.g., change field names or true condition string).
