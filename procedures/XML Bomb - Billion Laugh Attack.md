---
id: 32ef4a2d-534b-47b2-9b48-1cc32daa548c
name: XML Bomb - Billion Laugh Attack
type: procedure
verified: true
submitted: true
created_at: '2020-09-05T20:08:19.446575+00:00'
updated_at: '2023-05-26T18:51:45.028236+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
- '[[xml]]'
- '[[XML Billion Laugh]]'
- '[[XML Bomb]]'
---

# XML Bomb - Billion Laugh Attack

**Status**: ✓ Verified

## Summary

XML Bomb is an attack where, when an XML request is sent with the payload, the parser will try to process the payload and the data feeds on itself. This will eventually lead to Denial of Service condition. 

## Description

# Description

XML Bomb is an attack where, when an XML request is sent with the payload, the parser will try to process the payload and the data feeds on itself. This will eventually lead to Denial of Service condition.

# Procedure

1. The below screenshot shows the intercepted request of a login page with XML request.

2. The request is modified and XML Bomb payload is added as shown in the below screenshot. When the Go button is clicked, no response was observed from the server as it has become non responsive.

## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
- [[xml]]
- [[XML Billion Laugh]]
- [[XML Bomb]]
