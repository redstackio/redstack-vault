---
id: fd0961f9-fbbe-4a3e-9ab0-f1341fd01f19
name: Perform-Blind-XPath-Injection-for-Data-Extraction
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:41.409657+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - '[[tags/Blind Exploitation]]'
  - '[[tags/XPath Injection]]'
  - web-exploitation
  - injection
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Perform-Blind-XPath-Injection-for-Data-Extraction

## Summary

This procedure demonstrates how to perform blind XPath injection against web applications that use XML data sources for queries, such as login forms or search fields. By injecting XPath payloads into input fields, attackers can infer sensitive data like usernames or other XML elements without direct output from the application, using boolean-based or conditional techniques to extract information character by character.

## Description

Blind XPath injection exploits vulnerabilities in applications that construct XPath queries from user input without proper sanitization. For example, a login form might build an XPath like //user[username='input' and password='input'] to authenticate. An attacker injects payloads like ' or string-length(username)=5 -- to alter the query logic. Since it's 'blind,' the application doesn't return query results; success is inferred from response differences (e.g., true/false behaviors like page load times or error messages). This technique is useful for extracting data from XML-backed databases in reconnaissance or data theft scenarios. The target environment is typically a web application with XML processing (e.g., using libraries like libxml in PHP or Java). Prerequisites include identifying a vulnerable input point via error messages or trial-and-error fuzzing.

## Requirements

1. Access to a vulnerable web application input field that influences an XPath query (e.g., login username field).
2. Knowledge of the basic XML structure, such as element names (e.g., //user[username=...]), often guessed from common patterns or error leaks.
3. Tools for sending crafted HTTP requests, such as a browser, curl, or a proxy like Burp Suite.
4. Patience for iterative testing, as blind extraction can take many requests (e.g., hundreds for a single string).

## Defense

- Implement strict input validation and sanitization for all user inputs used in XPath queries, using parameterized queries or whitelisting.
- Use XML-aware security libraries (e.g., OWASP ESAPI) to escape special characters like ' and ".
- Monitor application logs and web traffic for anomalous request patterns, such as repeated boolean tests or unusual string functions in payloads.
- Enable web application firewalls (WAFs) with XPath injection rules to block suspicious inputs.

## Objectives

1. Confirm the presence of an XPath injection vulnerability using boolean conditions.
2. Determine the length of sensitive data elements (e.g., username length) to scope extraction.
3. Extract individual characters from XML data to reconstruct sensitive information like usernames or IDs.
4. Achieve data exfiltration without triggering direct error responses.

## Instructions

### Step 1: Identify Vulnerable Input and Test Basic Injection

**Context**: Locate an input field (e.g., username in a login form) that may be vulnerable to XPath injection. Test with a simple boolean payload to confirm if the application alters behavior based on true/false conditions, indicating XPath processing.

Inject a payload like ' or '1'='1 into the input and observe if authentication bypasses or different responses occur (e.g., success page vs. error).

> If the response changes (e.g., login succeeds on true condition), XPath injection is likely possible. This step verifies the vulnerability without extracting data.

### Step 2: Determine String Length Using Boolean Check

**Context**: Once vulnerability is confirmed, use the string-length function to infer the length of a target XML element (e.g., username). Iterate SIZE_INT from 0 upward until a true response is observed, revealing the length.

**Code** ([[codes/XPath-String-Length-Check]]):

```xpath
and string-length(account)=SIZE_INT
```

> Inject this into the vulnerable field, e.g., username=' and string-length(username)=5 --. Replace 'account' with the target XPath expression (e.g., //user[userid=1]/username) and test SIZE_INT values (1, 2, 3, etc.). A true response (e.g., successful login or no error) indicates the correct length. This narrows the extraction scope.

### Step 3: Extract Characters Using Substring Function

**Context**: With the length known, extract each character position (1 to length) by comparing substrings to possible values (a-z, 0-9, etc.). Use boolean conditions to identify matches, building the string iteratively.

**Code** ([[codes/XPath-Character-Extraction-Using-Substring]]):

```xpath
substring(//user[userid=5]/username,2,1)=CHAR_HERE
substring(//user[userid=5]/username,2,1)=codepoints-to-string(INT_ORD_CHAR_HERE)
```

> Inject into the field, e.g., username=' and substring(//user[userid=5]/username,2,1)='a' --. Test CHAR_HERE against alphabet characters or use INT_ORD_CHAR_HERE for Unicode (e.g., 97 for 'a'). A true response confirms the character. Repeat for each position. For example, if length is 5, test positions 1-5. This step reconstructs the full string after multiple requests.

### Step 4: Verify and Reconstruct Data

**Context**: Compile extracted characters into the full data element. Re-test the full reconstructed value in a non-blind query if possible to validate.

Submit the inferred data (e.g., full username) in a follow-up request to confirm accuracy, such as attempting login with the extracted username.

> Success is indicated by consistent behavior matching the boolean tests. If discrepancies occur, revisit length or character extractions for errors.
