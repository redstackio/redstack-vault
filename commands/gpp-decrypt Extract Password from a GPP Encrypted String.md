---
id: e7acf84f-ffe3-4c0b-a483-99c997916834
name: gpp-decrypt Extract Password from a GPP Encrypted String
type: command
executor: bash
data: gpp-decrypt $_ENCRYPTED_STRING
output: 'root@kali:~# gpp-decrypt ''CiDUq6tbrBL1m/js9DmZNIydXpsE69WB9JrhwYRW9xywOz1/0W5VCUz8tBPXUkk9y80n4vw74KeUWc2+BeOVDQ''

  /usr/bin/gpp-decrypt:21: warning: constant OpenSSL::Cipher::Cipher is deprecated

  MyUnclesAreMarioAndLuigi!!1!'
created_at: '2019-09-26T22:51:06.756813+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[gpp-decrypt]]'
- '[[openssl]]'
---

# gpp-decrypt Extract Password from a GPP Encrypted String

```bash
gpp-decrypt $_ENCRYPTED_STRING
```

## Expected Output

```
root@kali:~# gpp-decrypt 'CiDUq6tbrBL1m/js9DmZNIydXpsE69WB9JrhwYRW9xywOz1/0W5VCUz8tBPXUkk9y80n4vw74KeUWc2+BeOVDQ'
/usr/bin/gpp-decrypt:21: warning: constant OpenSSL::Cipher::Cipher is deprecated
MyUnclesAreMarioAndLuigi!!1!
```


