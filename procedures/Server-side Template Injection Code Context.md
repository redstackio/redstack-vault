---
id: 902fb8e4-0cb6-44de-b2f9-975ee470f93b
name: Server-side Template Injection Code Context
type: procedure
verified: true
submitted: true
created_at: '2020-08-27T17:38:07.272023+00:00'
updated_at: '2023-05-26T01:31:55.968174+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[Server Side Template Injection]]'
- '[[Web Applications]]'
---

# Server-side Template Injection Code Context

**Status**: ✓ Verified

## Summary

An attacker will manipulate the user controlled input ot execute the server-side attack by changing parameter values. 

## Description

# Description

An attacker will manipulate the user controlled input ot execute the server-side attack by changing parameter values.

# Instructions

1.Login to the account with the credentials provided.

2.With Burp proxying the requests through the browser, navigate to the comment section and enter some random text and click on *Post Comment *to submit the comment.

3.Under proxy tab, go to HTTP History identify the POST request with *`my-account/change-blog-post-author-displa*y and send the request to the repeater tab.`

4. From repeater tab, modify the* `blog-post-author-display* parameter value to *user.nickname}}{{7*7}}* and send the request to the server `. 

5.`Observe that the the username in the comment section is now changed to H0td0g49}} which indicates server-side template injection vulnerability.`

6.Modify the parameter value as below: to the request in step 3.

* `blog-post-author-display=user.name}}{%25+import+os+%25}{{os.system('rm%20/home/carlos/morale.txt'*)`

*`Reload the page in the browser to execute the payload*.`

## Platforms

- Web

## Tags

- [[injection]]
- [[Server Side Template Injection]]
- [[Web Applications]]
