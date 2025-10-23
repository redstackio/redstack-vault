---
id: fa2719cb-f7a8-40b7-bf49-3b8443e7ef21
name: Reflected XSS With AngularJS Sandbox escape Without Strings
type: procedure
verified: true
submitted: true
created_at: '2020-08-27T08:21:03.538584+00:00'
updated_at: '2023-05-26T01:10:41.520544+00:00'
platforms:
- Web
tags:
- '[[injection]]'
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Reflected XSS]]'
- '[[Web Applications]]'
---

# Reflected XSS With AngularJS Sandbox escape Without Strings

**Status**: ✓ Verified

## Summary

Some applications avoid using eval() in the angular JS to prevent execution of JS code. In this case, an attacker will use tostring() along with orderby to execute the JS code. 

## Description

# Description

Some applications avoid using *eval()* in the angular JS to prevent execution of JS code. In this case, an attacker will use *tostring()* along with orderby to execute the JS code.

# Instructions





1.Search for alphanumeric string with the search box.





![bf276982-6e4a-4279-8386-5566e28381f2.png]()





2.View the page source and observe that website uses AngularJS in an unusual way where the `$eval` function is not available and you will be unable to use any strings in AngularJS.





![f19bd9bf-6d22-4569-acb9-62d4d73db96f.png]()





3.Craft a payload using *Tostring()* to create a string without quotes. It then gets the `String` prototype and overwrites the `charAt` function for every string. This effectively breaks the AngularJS sandbox. Next, an array is passed to the `orderBy` filter. We then set the argument for the filter by again using* `toString(*)` to create a string and the `String` constructor property. Finally, we use the `*fromCharCod`e* method generate our payload by converting character codes into the string `*x=alert(1`)*. Because the `*charA`t* function has been overwritten, AngularJS will allow this code where normally it would not





![bd5d221a-bcf6-493d-a123-eb15caed848d.png]()





4.Loading the following url will trigger an alert popup in the application's response page. 



[*https://your-lab-id.web-security-academy.net/?search=1&toString().constructor.prototype.charAt%3d[].join;[1]|orderBy:toString().constructor.fromCharCode(120,61,97,108,101,114,116,40,49,41)=](https://your-lab-id.web-security-academy.net/?search=1&toString().constructor.prototype.charAt%3d%5b%5d.join;%5b1%5d|orderBy:toString().constructor.fromCharCode(120,61,97,108,101,114,116,40,49,41)=1)1*

## Platforms

- Web

## Tags

- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Reflected XSS]]
- [[Web Applications]]


