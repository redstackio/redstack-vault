---
id: 2d8dc443-815f-451e-a186-b840e1a34ad1
name: Clobbering DOM XSS To Enable XSS
type: procedure
verified: false
submitted: false
created_at: '2020-08-31T14:10:17.130395+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
platforms:
- Web
tags:
- '[[DOM XSS]]'
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
---

# Clobbering DOM XSS To Enable XSS

## Summary

If an attacker is able to contol some of the HTML content on the page , he can clobber some object such as anchor tag to execute his payload. 

## Description

# Description

If an attacker is able to contol some of the HTML content on the page , he can clobber some object such as anchor tag to execute his payload.

# Instructions

1. Navigate to the *view post* of the application

2. Right click on the page and select *developer tools .*

3. From developer tools menu navigate to *network *. Double click on* loadCommentsWithDomClobbering.js* to open the source code of JS.

4.Observe the following code

*let defaultAvatar = window.defaultAvatar || {avatar: '/resources/images/avatarDefault.svg'}*

*Observe that the defaultavatar uses logical or operator function .*

5. Enter the following payload in the comment section

*<a id=defaultAvatar><a id=defaultAvatar name=avatar href="cid:&quot;onerror=alert(1)//">*

6. Post the comment and it can be seen the comment has been successfully posted.

7. Return to the comment section of the blog post and enter the comments and post the comments.

8.Creating two anchors with same ID will make them to be grouped in DOM collection. The “name” attribute in the second anchor contains the value "avatar", which will clobber the “avatar” property with the contents of the “href” attribute. When the second  comment is posted , the browser uses the newly added variable and triggers the event handler to execute the alert() which can be seen in the response of the page.

## Platforms

- Web

## Tags

- [[DOM XSS]]
- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
