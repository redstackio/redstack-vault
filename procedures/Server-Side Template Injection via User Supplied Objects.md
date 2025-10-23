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





![7aa14c81-fd6e-4324-ae27-d47b5f764ad9.png]()





2. Edit one of the product description templates.







![d1de99af-2d47-4d91-b3e1-2b2280e4084e.png]()





3. Change the template expressions to an invalid value or fuzz string like *`${{<%[%'"}}%*\ and save the template.`





![a8eacbde-e650-48dd-b0c3-2975c81e3d82.png]()





4. The error message shows that Django framework is being used.





![6088e10d-e0e4-4ed7-9fd2-66bb77e7f1f1.png]()





5. In the template, remove the invalid syntax and enter the following statement to invoke the `debug` built-in:
 `{% debug %}`







![2f22190e-b2ee-4f31-948e-0feda73d834b.png]()







6. Save the template. The output will contain a list of objects and properties to which you have access from within this template. Notice that you can access the `settings` object.





![f7abc1d2-422c-4ab6-8f49-ace9ca23ae7d.png]()





7. As Django documentation, settings object contains a SECRET_KEY property. In the template, remove the `{% debug %}` statement and enter the expression `{{settings.SECRET_KEY}} to access the secret key.`





![cd18dd72-b89b-441d-b01a-02c53ae10067.png]()





## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Server Side Template Injection]]
- [[SSTI]]
- [[Web Applications]]


