---
id: a05bd8c5-11df-40fc-a21b-2a8981f70bd9
name: Union SQL Injection - Finding Column Containing Text
type: procedure
verified: true
submitted: true
created_at: '2020-08-27T18:19:39.105305+00:00'
updated_at: '2023-05-26T01:27:44.224112+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[SQL]]'
- '[[sqli]]'
- '[[SQL Injection]]'
- '[[Web Applications]]'
---

# Union SQL Injection - Finding Column Containing Text

**Status**: ✓ Verified

## Summary

Union SQL injection uses the UNION statement to extract information from the database. It starts with identifying the number of columns in the table and then finding the column that contains text observed in the browser. 

## Description

# Description

Union SQL injection uses the UNION statement to extract information from the database. It starts with identifying the number of columns in the table and then finding the column that contains text observed in the browser.



# Procedure



1. Access the application and apply filter to list all categories. Observe *category* parameter in the URL and the value is set to All.





![3714f86c-97b1-4c76-bd2f-9fdb86b557c0.png]()



2. Add SQL injection payload with UNION statement as shown below.



*'+union+select+null--*



![97995919-2c9b-4bd8-a70e-8230e45ae698.png]()

3. Continue to increase the number of NULL values in the payload till the application loads without any error. From the below screenshot, number of columns can be identified as 3.





![742be7be-fcb5-4d15-9596-f095b5a516ba.png]()

4. Now, start replacing the NULL value with some random text e.g. 'test'.





![6fc4df88-1e08-4d4d-9f5c-0c5c1bbf2410.png]()



5. Move the test value to the next NULL position till the application loads without error.





![38c57312-2b26-4092-8d92-330a699f4959.png]()



6. This shows that the 2nd column contains the text that is displayed in the page.



## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[SQL]]
- [[sqli]]
- [[SQL Injection]]
- [[Web Applications]]


