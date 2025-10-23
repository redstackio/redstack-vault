---
id: 40a0ad95-399a-484a-8795-4fa61be73186
name: Use Telnet for SMTP/POP
type: cheatsheet
verified: false
created_at: '2020-07-14T18:23:48.621038+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Use Telnet for SMTP/POP

# Description

To test a SMTP or POP server you can connect to it with Telnet and using plaintext commands, authenticate and send or access emails.

These same commands can also be scripted to automate the process for a larger scale.







**Code**: [[
# connect
telnet target-ip 25
# provide valid or ]]







**Code**: [[
# connect
telnet target-ip 110
# login
USER usern]]






