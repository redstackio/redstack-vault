---
id: 112160e0-9d3e-401d-8f82-71205b3d927d
name: DOM XSS Using Source location.search Inside Select Element
type: procedure
verified: true
submitted: true
created_at: '2020-08-24T06:41:04.772306+00:00'
updated_at: '2023-05-26T01:11:38.990936+00:00'
platforms:
- Web
tags:
- '[[DOM XSS]]'
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# DOM XSS Using Source location.search Inside Select Element

**Status**: ✓ Verified

## Summary

Document.write function is called with data from location.search , which can be controlled by an attacker through url. 

## Description

# Description

Document.write function is called with data from location.search , which can be controlled by an attacker through url. 

# Instructions

1.Naviagte to the product page and click on *checkstock*.

2. Right click on the application page and select *inspect element *to check the search box HTML elements.

3. Use the search arrow in the left most of the console menu and hover it on top of the *checkstock*

4.Observe that there is a hidden parameter *storeId*. Change the url to 

*`product?productId=1&storeId= and put some alphanumeric strin*g`

5.Enter some random alpha numeric string as shown below.

6. Right click on the application and select inspect element as done in step 2. observe that random string has been placed inside a select element but also appended with “>

7. Modify the url from Step 4 to execute the payload in the followingway and load the modified url in the browser to see the alert being popped out.

*`product?productId=1&storeId="></select><img%20src=1%20onerror=alert(1)*>`

## Platforms

- Web

## Tags

- [[DOM XSS]]
- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
