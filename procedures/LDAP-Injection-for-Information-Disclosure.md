---
id: 04a42434-7e7a-4e43-aeea-eef3249172e9
name: LDAP-Injection-for-Information-Disclosure
type: procedure
verified: true
submitted: true
created_at: '2020-08-22T15:03:36.120633+00:00'
updated_at: '2023-05-26T18:22:20.652618+00:00'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - '[[tags/LDAP Injection]]'
  - '[[tags/Web Applications]]'
commands:
  - '[[commands/curl-ldap-injection-payload]]'
tools:
  - '[[tools/Burp-Suite]]'
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# LDAP-Injection-for-Information-Disclosure

## Summary

This procedure demonstrates how to exploit LDAP injection vulnerabilities in web applications to disclose sensitive information, such as user objects or system resources, that should only be accessible to authorized users. By injecting malicious LDAP query syntax into user-controlled inputs, an attacker can manipulate the backend LDAP search to return unauthorized data, such as all user accounts or resource details.

## Description

LDAP injection occurs when user input is improperly sanitized and concatenated into LDAP queries, allowing attackers to alter the query logic. In a typical scenario, a web application like a resource explorer queries an LDAP directory to list available resources (e.g., printers with type=printer or scanners with type=scanner). An attacker can inject payloads to bypass filters and retrieve broader datasets, such as all users (uid=*) combined with resource types. This technique targets applications authenticating or querying LDAP directories without proper input validation, leading to information disclosure. It is commonly found in enterprise environments using LDAP for user and resource management. Successful exploitation requires identifying injectable parameters, crafting payloads that modify the query (e.g., using boolean operators like | or * wildcards), and observing the response for leaked data. Prerequisites include access to the web interface and basic knowledge of LDAP syntax.

## Requirements

1. Access to a web application that performs LDAP queries based on user input (e.g., search forms or resource selectors).
2. Network connectivity to the target application.
3. Tools for intercepting and modifying HTTP requests, such as [[tools/Burp-Suite]] or curl.
4. Basic understanding of LDAP query syntax (e.g., filters like (type=printer) or (uid=*)).

## Defense

Defensive measures and detection strategies:

- Implement input validation and sanitization to escape special LDAP characters (e.g., *, (, ), |) in user inputs.
- Use parameterized LDAP queries or LDAP filters that treat inputs as literals rather than query components.
- Enable LDAP query logging on the directory server to monitor for anomalous searches (e.g., wildcard expansions or unexpected boolean logic).
- Apply least privilege to LDAP binds, limiting application accounts to read-only access for specific object classes.
- Deploy web application firewalls (WAFs) with rules to detect LDAP injection patterns in request parameters.

## Objectives

1. Identify vulnerable input fields in the web application that influence LDAP queries.
2. Inject malicious LDAP syntax to alter query results and disclose unauthorized information.
3. Extract and analyze the leaked data, such as user objects or system resources.

## Instructions

### Step 1: Identify the Vulnerable Endpoint

**Context**: Locate the web page or form where user input affects an LDAP query, such as a resource explorer allowing selection of types like 'printer' or 'scanner'. Test for injection by observing how inputs modify backend behavior.

Inspect the application using browser developer tools or [[tools/Burp-Suite]] to capture requests. Look for POST or GET parameters that likely feed into LDAP filters (e.g., 'rsc1=printer', 'rsc2=scanner').

### Step 2: Craft the LDAP Injection Payload

**Context**: Construct a payload that manipulates the LDAP query to return more data than intended. For example, if the legitimate query is (&(type=printer)(uid=user)) or similar, inject to make it broader like *(|(type=printer)(uid=*))(type=scanner)*, which returns all printers, all users, and all scanners.

Common payloads include appending * for wildcards or | for OR logic. Ensure the payload closes any open parentheses and adds boolean operators to union results.

### Step 3: Send the Injection Request

**Context**: Submit the crafted payload via the identified parameter to execute the modified LDAP query and retrieve leaked information.

**Command** ([[commands/curl-ldap-injection-payload]]):
```bash
curl -X POST 'http://target.com/resource-explorer' \
  -d 'rsc1=printer' \
  -d 'rsc2=*)|(uid=*)(type=scanner' \
  -H 'Content-Type: application/x-www-form-urlencoded'
```

> This command sends a POST request with an injected payload in the 'rsc2' parameter, assuming the original query is something like (&(type=$_rsc1)(type=$_rsc2)). The injection closes the filter and adds (uid=*) to enumerate users alongside scanners. Expected output includes an expanded list of resources and user objects in the response body, such as JSON or HTML tables showing UIDs, types, and attributes not visible in normal queries.

### Step 4: Analyze the Response

**Context**: Review the server response for disclosed information, verifying if unauthorized data (e.g., full user lists) appears.

Parse the output manually or with tools like jq for JSON responses. Look for anomalies like increased result counts or sensitive attributes (e.g., email, roles). If successful, the response will include objects beyond the intended scope, confirming information disclosure.
