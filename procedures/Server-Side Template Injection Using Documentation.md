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





![07fefc1c-c7dd-40a3-b72f-a6e45586fed3.png]()



2. Edit one of the product description templates





![a477b125-b931-434b-8b02-584878d6a971.png]()



3. Observe that this template engine uses the syntax `${someExpression}` to render the result of an expression on the page. Either enter a new expression or change one of the existing ones to refer to an object that doesn't exist, such as `${hacker}`, and save the template.





![b86a8ef2-3168-4dbc-bab5-240514148638.png]()



4. The error message in the output shows that the Freemarker template engine is being used.





![855ebede-d537-48ae-9311-0c643b735aa6.png]()



5. Construct an exploit as shown below. This exploit deletes a file on the server named *morale.txt*. Click on preview and the file gets deleted on the server.



*`<#assign ex="freemarker.template.utility.Execute"?new()> ${ ex("rm /home/carlos/morale.txt") *}`





![e7f3e189-d20c-45ca-9b03-c582f83367b1.png]()





## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Server Side Template Injection]]
- [[SSTI]]
- [[Web Applications]]


