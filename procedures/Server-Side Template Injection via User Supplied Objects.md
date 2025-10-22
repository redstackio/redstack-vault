---
id: be2d5a3a-2ecf-47e7-9ae3-6b5905c29ecb
name: Server-Side Template Injection via User Supplied Objects
type: procedure
verified: false
submitted: false
created_at: '2020-08-24T06:12:14.484247+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Server Side Template Injection]]'
- '[[SSTI]]'
- '[[Web Applications]]'
---

# Server-Side Template Injection via User Supplied Objects

## Summary

Server-Side Template Injection attack can be performed by injecting code in the template from the browser. Sensitive information can be disclosed using the user supplied objects. 

## Description

# Description

Server-Side Template Injection attack can be performed by injecting code in the template from the browser. Sensitive information can be disclosed using the user supplied objects.

# Procedure

1. Login into the application

2. Edit one of the product description templates.

3. Change the template expressions to an invalid value or fuzz string like *`${{<%[%'"}}%*\ and save the template.`

4. The error message shows that Django framework is being used.

5. In the template, remove the invalid syntax and enter the following statement to invoke the `debug` built-in:
 `{% debug %}`

6. Save the template. The output will contain a list of objects and properties to which you have access from within this template. Notice that you can access the `settings` object.

7. As Django documentation, settings object contains a SECRET_KEY property. In the template, remove the `{% debug %}` statement and enter the expression `{{settings.SECRET_KEY}} to access the secret key.`

## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Server Side Template Injection]]
- [[SSTI]]
- [[Web Applications]]
