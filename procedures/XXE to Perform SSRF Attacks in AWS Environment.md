---
id: 784a54f4-b892-4f3c-82c5-51fb99eacc23
name: XXE to Perform SSRF Attacks in AWS Environment
type: procedure
verified: true
submitted: true
created_at: '2020-08-23T18:16:54.485269+00:00'
updated_at: '2023-05-26T18:40:57.134714+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
- '[[xxe]]'
---

# XXE to Perform SSRF Attacks in AWS Environment

**Status**: ✓ Verified

## Summary

XXE can be performed by adding an external entity in the XML request. In AWS environment, it is possible to retrieve data from the EC2 instance on which the web server is running. 

## Description

# Description

XXE can be performed by adding an external entity in the XML request. In AWS environment, it is possible to retrieve data from the EC2 instance on which the web server is running.



# Procedure



1. Visit the product page and click on Check stock. Intercept the request and send it to repeater.





![03b569b5-1309-4ad4-937f-0c504e7fc841.png]()



2. Insert the following external entity definition between the XML declaration and the `stockCheck` element and then replace the `productId` number with a reference to the external entity: `&xxe;`



*`<!DOCTYPE test [ <!ENTITY xxe SYSTEM "http://169.254.169.254/"> ]>* `





![f7005a12-6a53-4f64-9641-4c0b1cb6ca9d.png]()



3. The response should contain "Invalid product ID:" followed by the response from the metadata endpoint, which will initially be a folder name. Iteratively update the URL in the DTD to explore the API until you reach `/latest/meta-data/iam/security-credentials/admin`. This should return JSON containing the `SecretAccessKey`.





![686cd9cd-bb66-4714-8016-a67fac35da6d.png]()





## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
- [[xxe]]


