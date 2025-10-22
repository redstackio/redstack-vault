---
id: 596ba10e-f47b-48c1-8b51-cd94219c08a6
name: Server-Side Template Injection Using Documentation
type: procedure
verified: true
submitted: true
created_at: '2020-08-23T18:31:14.207991+00:00'
updated_at: '2023-05-26T01:37:33.968203+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Server Side Template Injection]]'
- '[[SSTI]]'
- '[[Web Applications]]'
---

# Server-Side Template Injection Using Documentation

**Status**: ✓ Verified

## Summary

A payload can be added to the existing template on the web page and it gets executed resulting in code execution at the server. 

## Description

# Description

A payload can be added to the existing template on the web page and it gets executed resulting in code execution at the server.

# Procedure

# 

1. Login into the application

2. Edit one of the product description templates

3. Observe that this template engine uses the syntax `${someExpression}` to render the result of an expression on the page. Either enter a new expression or change one of the existing ones to refer to an object that doesn't exist, such as `${hacker}`, and save the template.

4. The error message in the output shows that the Freemarker template engine is being used.

5. Construct an exploit as shown below. This exploit deletes a file on the server named *morale.txt*. Click on preview and the file gets deleted on the server.

*`<#assign ex="freemarker.template.utility.Execute"?new()> ${ ex("rm /home/carlos/morale.txt") *}`

## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Server Side Template Injection]]
- [[SSTI]]
- [[Web Applications]]
