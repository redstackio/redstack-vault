---
id: f2d65daa-f252-42c5-abe2-34ad50700ab0
name: xpath-injection-through-search
type: procedure
verified: true
submitted: true
created_at: '2020-07-31T16:17:37.677420+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - '[[tags/injection]]'
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/Web Applications]]'
  - '[[tags/xml]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
commands:
  - '[[commands/curl-basic-get-request]]'
  - '[[commands/curl-xpath-error-injection]]'
  - '[[commands/curl-xpath-payload-injection]]'
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# XPath Injection Through Search

## Summary

This procedure demonstrates how to identify and exploit XPath injection vulnerabilities in a web application's search functionality to exfiltrate sensitive information, such as passwords, from the backend XML data store. By injecting malformed XPath queries into user-controlled parameters, an attacker can bypass normal query logic, trigger errors to confirm the vulnerability, and extract confidential data like user credentials.

## Description

XPath injection occurs when user input is improperly sanitized and directly concatenated into XPath queries used to parse XML data in web applications. This vulnerability allows attackers to manipulate the query structure, potentially dumping entire XML documents or specific sensitive elements. The procedure targets search endpoints that accept parameters like 'action' or 'query', common in applications using XML for data storage. Success relies on observing error messages that reveal XPath usage and crafting payloads to close the original query context while appending new extraction logic. This technique is particularly effective against legacy web apps or those with weak input validation, leading to unauthorized data disclosure.

## Requirements

1. Access to a web application with a search feature that uses XPath for querying XML data (e.g., user directories or product catalogs).
2. Network connectivity to the target application, typically over HTTP/HTTPS on port 80/443.
3. Tools like a browser, curl, or Burp Suite for intercepting and modifying requests.
4. Basic knowledge of XPath syntax to craft payloads.

## Defense

Defensive measures and detection strategies:

- Implement parameterized XPath queries or use XML-aware libraries that bind parameters safely (e.g., XmlDocument.SelectNodes with parameters in .NET).
- Apply strict input validation and sanitization, rejecting or escaping special characters like single quotes ('), brackets ([]), and pipes (|).
- Enable web application firewall (WAF) rules to detect anomalous XPath patterns in request parameters.
- Log and monitor for error responses containing XPath-related stack traces or XML parsing exceptions.
- Use least-privilege access to the XML data store, limiting query scope to authorized elements only.

## Objectives

1. Confirm the presence of an XPath injection vulnerability by triggering an error with a single quote injection.
2. Extract sensitive information, such as passwords, by constructing a malicious XPath payload.
3. Achieve data exfiltration without authentication, demonstrating unauthorized access to backend data.

## Instructions

### Step 1: Observe Normal Search Request

**Context**: Identify the target search endpoint and understand the normal request structure, including user-controlled parameters like 'action' that are passed to XPath queries. This baseline helps spot deviations caused by injections.

**Command** ([[commands/curl-basic-get-request]]):
```bash
curl -X GET "http://target.com/search?action=user&query=test" -v
```

> This sends a standard GET request to the search page. Inspect the response for normal XML-processed results, such as a list of users or items. No errors should appear, confirming the endpoint's functionality.

### Step 2: Inject Single Quote to Trigger Error

**Context**: Append a single quote (') to a user-controlled parameter to break the XPath query syntax, forcing the application to reveal error details that confirm XPath usage. This step enumerates server-side information without extracting data yet.

**Command** ([[commands/curl-xpath-error-injection]]):
```bash
curl -X GET "http://target.com/search?action=user'" -v
```

> The single quote closes the string in the XPath query prematurely, causing a syntax error. Look for responses containing phrases like "XPathException," "invalid XPath," or XML parsing errors, which validate the vulnerability. If no error appears, try other parameters like 'query'.

### Step 3: Craft and Submit XPath Payload for Data Exfiltration

**Context**: Build an XPath payload that closes the original query context (e.g., using ')] to end a predicate) and appends a union operation (|) to extract sensitive elements like passwords from the XML structure. This step accomplishes the primary objective of leaking confidential data.

**Command** ([[commands/curl-xpath-payload-injection]]):
```bash
curl -X GET "http://target.com/search?action=user')]//password | //a[contains(.,'admin')]/following-sibling::password" -v
```

> The payload ')]//password | //a[contains(.,'admin')]/following-sibling::password assumes a common XML structure where passwords follow user elements. Adjust based on observed schema from errors. Success is indicated by the response body displaying plaintext passwords or XML fragments containing sensitive info, rather than an error or empty results.
