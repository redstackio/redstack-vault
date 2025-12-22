---
tags:
  - nosql-injection
  - mongodb
  - endpoint-analysis
type: procedure
tools:
  - '[[tools/Python]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:51.982Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: d8186a3a-061c-4d42-bc00-86ab5d15b825
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-MongoDB-Injection-in-Login-Endpoints

## Summary

This procedure involves analyzing the login endpoints of the express-cart application to identify NoSQL injection vulnerabilities where user-supplied email parameters are directly inserted into MongoDB queries without sanitization, allowing operators like $regex to be injected.

## Description

In the express-cart v1.1.7 application, the customer and admin login handlers (e.g., POST /login) use code like `db.customers.findOne({email: req.body.loginEmail})` or similar for admins. Since `req.body.loginEmail` is parsed from JSON without validation, attackers can supply MongoDB objects instead of strings, leading to injection. This procedure focuses on static or dynamic analysis to confirm the flaw, typically by reviewing source code or observing query behavior with test inputs. Prerequisites include access to the application source or a debugging setup like attaching to the Node.js process.

## Requirements

1. Access to the target application's source code or runtime environment (e.g., via deobfuscation or proxy interception)
2. Knowledge of Node.js/Express and MongoDB query syntax
3. Tools for HTTP request inspection (e.g., Burp Suite or Python scripts)

## Defense

Defensive measures and detection strategies:

- Implement input sanitization by converting `req.body.loginEmail` to a string before querying (e.g., `String(req.body.loginEmail)`)
- Use MongoDB query builders or ORMs like Mongoose with schema validation to prevent operator injection
- Monitor login endpoint logs for anomalous payloads containing $ operators

## Objectives

1. Confirm the presence of unsanitized input in MongoDB queries
2. Identify exact endpoints (customer vs. admin) vulnerable to injection
3. Establish baseline for payload crafting in subsequent steps

## Instructions

### Step 1: Review Login Handler Code

**Context**: Examine the Express route handlers for login to locate the MongoDB query construction.

No specific command; manually inspect files like `routes/login.js` or equivalent. Look for direct use of `req.body` in `findOne` or `find` calls.

> Expected: Code snippet showing `db.collection.findOne({field: req.body.param})` without sanitization.

### Step 2: Test with Basic Input

**Context**: Send a simple JSON payload to observe if it affects the query response.

Use Python with [[tools/requests-Library]] to send a test request:

```python
import requests

data = {"loginEmail": "test@example.com"}
response = requests.post("http://target.com/login", json=data)
print(response.text)
```

> Expected: Standard login error. If the input is echoed or alters behavior unexpectedly, injection is likely.

### Step 3: Probe for Operator Injection

**Context**: Attempt to inject a basic operator to confirm vulnerability.

Send a payload with $ne (not equal) to bypass login logic:

```python
data = {"loginEmail": {"$ne": "invalid"}}
response = requests.post("http://target.com/login", json=data)
```

> Expected: Different response (e.g., no error or match found), indicating injection success.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Python]]

## Tags

- nosql-injection
- mongodb
- endpoint-analysis
