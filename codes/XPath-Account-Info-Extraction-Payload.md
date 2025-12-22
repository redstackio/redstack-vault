---
id: 16105846-dea4-4185-9d25-3d187a9a61e7
name: XPath-Account-Info-Extraction-Payload
type: code
language: xpath
verified: true
created_at: '2023-04-06T03:56:41.389450+00:00'
updated_at: '2023-04-10T20:24:47.983926+00:00'
platforms:
  - Web
tags:
  - xpath-injection
  - payload
validated: true
---

# XPath-Account-Info-Extraction-Payload

## Code

```xpath
"string(//user[name/text()='" +vuln_var1+ "' and password/text()=’" +vuln_var1+ "']/account/text())"
```

## Description

This XPath payload constructs a query to extract account information from an XML structure by matching username and password fields. It is injected into a vulnerable input to retrieve the 'account' text node for a specified user, bypassing normal authentication logic.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| vuln_var1 | Username or password value to match (used twice for name and password) | admin |

## Usage

Embed this payload in a web form input (e.g., username field) during login or search operations. For example, in a scripted request or Burp Intruder, replace vuln_var1 with target credentials to pull account details. Use in ethical pentesting only on authorized targets.

## Detection

- WAF rules matching XPath keywords like //user, text(), or string().
- Application logs showing malformed XPath queries or unusual XML parsing errors.
- Response analysis for unexpected XML fragments in output.

## Related

- [[procedures/XPath-Injection-for-User-Account-Retrieval]]
