---
id: 9a4b0d23-b558-4024-98d8-4d3dfefe666d
name: dd_rescue
type: tool
verified: false
created_at: '2019-08-28T21:17:38.113954+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
---

# dd_rescue

## Overview

Like dd, dd_rescue does copy data from one file or block device to another. You can specify file positions (called seek and Skip in dd). There are several differences: dd_rescue does not provide character conversions. The command syntax is different. Call dd_rescue -h. dd_rescue does not abort on e

## Description

Like dd, dd_rescue does copy data from one file or block device to another. You can specify file positions (called seek and Skip in dd). There are several differences:



dd_rescue does not provide character conversions.



The command syntax is different. Call dd_rescue -h.



dd_rescue does not abort on errors on the input file, unless you specify a maximum error number. Then dd_rescue will abort when this number is reached.



dd_rescue does not truncate the output file, unless asked to.



You can tell dd_rescue to start from the end of a file and move backwards.



It uses two block sizes, a large (soft) block size and a small (hard) block size. In case of errors, the size falls back to the small one and is promoted again after a while without errors.










