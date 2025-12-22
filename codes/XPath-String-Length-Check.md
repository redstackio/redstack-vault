---
id: 11c60356-fce2-4b76-a880-e6dd53611f80
type: code
name: XPath-String-Length-Check
language: xpath
verified: true
created_at: '2023-04-06T03:56:41.407581+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - xpath-injection
  - blind-exploitation
validated: true
---

# XPath-String-Length-Check

## Code

```xpath
and string-length(account)=SIZE_INT
```

## Description

This XPath snippet performs a boolean check to determine the length of a string value in an XML document during blind injection attacks. It compares the length of the specified element (e.g., a username) to a test integer, allowing attackers to infer the length through application response differences without direct output.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| account | The XPath path to the string element being tested | //user/username |
| SIZE_INT | The integer length value to compare against (iterate from 0) | 5 |

## Usage

Inject this payload into a vulnerable input field that constructs an XPath query, such as a login form's username parameter: username=' and string-length(//user/username)=5 --. Send requests with incrementing SIZE_INT until a 'true' response (e.g., successful page load) is observed, revealing the string's length. This is a foundational step in blind XPath data extraction, used in procedures like [[procedures/Perform-Blind-XPath-Injection-for-Data-Extraction]].

## Detection

- Web application logs showing repeated queries with string-length functions or boolean comparisons.
- Intrusion detection systems (IDS) alerting on XPath-specific functions in user inputs.
- Anomalous traffic patterns with high volumes of similar requests testing incremental integer values.
