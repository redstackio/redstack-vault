---
id: 11535e8b-c784-4905-84fd-6000f359b56c
name: Reflected XSS In a Template Literal(Where <>,\,'," are Unicode-escaped)
type: procedure
verified: true
submitted: true
created_at: '2020-08-27T10:26:20.588718+00:00'
updated_at: '2023-05-26T01:28:50.368354+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Reflected XSS]]'
- '[[Web Applications]]'
---

# Reflected XSS In a Template Literal(Where <>,\,'," are Unicode-escaped)

**Status**: ✓ Verified

## Summary

Template literals in JavaScript will allow embedded expressions.These are encapsulated in backticks and embededded expressions are identified using $. An attacker will make use of template literals to execute JS code which is otherwise blocked by the application. 

## Description

# Description

Template literals in JavaScript will allow embedded expressions.These are encapsulated in backticks and embededded expressions are identified using $. An attacker will make use of template literals to execute JS code which is otherwise blocked by the application.



# Instructions





1.Enter random string in the search box.







![5815b458-f189-4b0c-ae2c-8d984d43dc00.png]()





2.Observe that the random string has been reflected inside a JavaScript template string





![7d173d50-9d3e-48bf-a95c-78218b90f0e1.png]()





3. Search for ${} to escape JavaScript template string.





![ff1c6f48-871a-4758-b32b-adde675198e9.png]()





4. Observe that the JavaScript template has been escaped.







![24851acf-624f-4eeb-8a00-7931ffaea3dc.png]()





5. Enter the folowing payload in the box to execute JS inside the template string.

*`${alert(1)*}`





![75e23f32-b6d0-4db3-8103-d4799615f356.png]()





6. Observe the alert pop which is triggered by the payload from above step.





![19a80a1b-dc9d-46eb-99ce-1199d8e68d1a.png]()



## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Reflected XSS]]
- [[Web Applications]]


