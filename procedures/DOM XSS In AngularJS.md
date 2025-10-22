---
id: 8c78ebff-0f00-478d-bb0e-e48233cc6fc1
name: DOM XSS In AngularJS
type: procedure
verified: true
submitted: true
created_at: '2020-08-23T18:59:50.837613+00:00'
updated_at: '2023-05-26T01:36:35.728291+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Reflected XSS]]'
- '[[Web Applications]]'
---

# DOM XSS In AngularJS

**Status**: ✓ Verified

## Summary

Description AngularJS is used to dynamically build the web applications. It scans the elements of HTML nodes containing ng-app directive. When this directive is used , javascript gets executed inside the double curly braces. Instructions 1. Enter some random text in the search box . 

## Description

Description

AngularJS is used to dynamically build the web applications. It scans the elements of HTML nodes containing ng-app directive. When this directive is used , javascript gets executed inside the double curly braces.

Instructions

1. Enter some random text in the search box .

2. Right click inside the search box and click on *Inspect element* . Observe that the search term is enclosed in *ng-app* directive

3.Enter the following AngularJS expression in the search box: *{{$on.constructor('alert(1)')()}}*

4. Click on search . Observe that paylaod gets executed and a alert can be seen.

## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Reflected XSS]]
- [[Web Applications]]
