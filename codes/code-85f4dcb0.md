---
id: 85f4dcb0-2c8b-4508-bef7-aa1b5c78a4b6
type: code
language: Bash
verified: false
created_at: '2020-07-14T18:14:37.896110+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 85f4dcb0

**Language**: Bash

```bash

# connect
telnet target-ip 25
# provide valid or fake email-address
EHLO username@domain.tld
# set mail-from
MAIL FROM: <username@domain>
# set recipient-to
RCPT TO: <target-username@target-domain.tld>
# set body and sent mail
DATA
354 Ok Send data ending with <CRLF>.<CRLF>
FROM: username@domain
Hallo World!
.

```
