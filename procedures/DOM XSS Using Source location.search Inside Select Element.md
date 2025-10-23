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







![880aa052-53a3-4cbf-8bb7-fb8f824f42b4.png](_assets/images/Mash/880aa052-53a3-4cbf-8bb7-fb8f824f42b4.png)





2. Right click on the application page and select *inspect element *to check the search box HTML elements.









![20168639-5bb1-4960-b05d-11c7ed9738e5.png](_assets/images/Mash/20168639-5bb1-4960-b05d-11c7ed9738e5.png)





3. Use the search arrow in the left most of the console menu and hover it on top of the *checkstock*





![abcafa50-d27b-4143-97f5-976013bf46e5.png](_assets/images/Mash/abcafa50-d27b-4143-97f5-976013bf46e5.png)





4.Observe that there is a hidden parameter *storeId*. Change the url to 



*`product?productId=1&storeId= and put some alphanumeric strin*g`







![fcfdeba5-51ac-40c0-bdad-8871cefbeb14.png](_assets/images/Mash/fcfdeba5-51ac-40c0-bdad-8871cefbeb14.png)







5.Enter some random alpha numeric string as shown below.







![76b4e0f0-c5f5-4fdb-8f38-f0a0e31023e8.png](_assets/images/Mash/76b4e0f0-c5f5-4fdb-8f38-f0a0e31023e8.png)





6. Right click on the application and select inspect element as done in step 2. observe that random string has been placed inside a select element but also appended with “>









![5fdc59bc-700c-4f42-a4e3-78c643cf53f8.png](_assets/images/Mash/5fdc59bc-700c-4f42-a4e3-78c643cf53f8.png)





7. Modify the url from Step 4 to execute the payload in the followingway and load the modified url in the browser to see the alert being popped out.



*`product?productId=1&storeId="></select><img%20src=1%20onerror=alert(1)*>`





![13f6cc4a-fc42-44c5-a3fb-83716290d3a2.png](_assets/images/Mash/13f6cc4a-fc42-44c5-a3fb-83716290d3a2.png)



## Platforms

- Web

## Tags

- [[DOM XSS]]
- [[injection]]
- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]


