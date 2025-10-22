---
id: 36b17e39-2824-4c69-982e-2a8539657d38
name: Reflected DOM XSS
type: procedure
verified: true
submitted: true
created_at: '2020-08-23T18:03:15.781222+00:00'
updated_at: '2023-05-26T18:39:04.335999+00:00'
platforms:
- Web
tags:
- '[[Reflected DOMXSS]]'
- '[[Web Applications]]'
---

# Reflected DOM XSS

**Status**: ✓ Verified

## Summary

Descritpion In reflected DOM xss, the server side process the payload from a request and the payload gets reflected in the response. Instructions 1. Enter the text xss in the search box as shown below. 

## Description

Descritpion

In reflected DOM xss, the server side process the payload from a request and the payload gets reflected in the response.

Instructions

1. Enter the text xss in the search box as shown below.

2.Intercept the request using burpsite.

3. observe the response reflects the search term *xss *in the body.

4.Use the developer tools in chrome browser to identify the searchresults.js. It can be seen that the JS file eval() function call .

5. Observe that the search term in the application doesnot escape the'\' in the JSON response.

6. Enter the payload ***\"-alert(1)*}// in the search field **

6. Payload gets executed and a alert(1) can be seen.

## Platforms

- Web

## Tags

- [[Reflected DOMXSS]]
- [[Web Applications]]
