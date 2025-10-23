---
id: adffcae4-5128-4f20-9cde-4fb0731f5be3
name: cachedump
type: tool
verified: false
created_at: '2019-08-28T21:17:29.357790+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# cachedump

## Overview

creddump is a python tool to extract various credentials and secrets from Windows registry hives. It currently extracts: LM and NT hashes (SYSKEY protected) Cached domain passwords LSA secrets It essentially performs all the functions that bkhive/samdump2, cachedump, and lsadump2 do, but in a platf

## Description

creddump is a python tool to extract various credentials and secrets from Windows registry hives. It currently extracts:



LM and NT hashes (SYSKEY protected)



Cached domain passwords



LSA secrets



It essentially performs all the functions that bkhive/samdump2, cachedump, and lsadump2 do, but in a platform-independent way.It is also the first tool that does all of these things in an offline way (actually, Cain & Abel does, but is not open source and is only available on Windows).






