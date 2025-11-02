---
id: 658df61c-8d59-4acf-9f61-1cf550be26d5
name: Search Raw Data for Human Readable Strings
type: command
executor: bash
data: strings $_DUMP | grep $_STRING
output: 'root@kali:~# strings dump  | grep password

  security.ask_for_password

  security.insecure_password.ui.enabled

  urlclassifier.passwordAllowTable

  services.sync.prefs.sync.browser.safebrowsing.passwords.enabled

  services.sync.engine.passwords.validation.maxRecords

  ...

  RG_1=mail.megabank.com/login.php?username=admin&login_password=wh3r3sth3b33f?%3f&login='
created_at: '2020-03-31T05:01:26.325180+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[grep]]'
---

# Search Raw Data for Human Readable Strings

```bash
strings $_DUMP | grep $_STRING
```

## Expected Output

```
root@kali:~# strings dump  | grep password
security.ask_for_password
security.insecure_password.ui.enabled
urlclassifier.passwordAllowTable
services.sync.prefs.sync.browser.safebrowsing.passwords.enabled
services.sync.engine.passwords.validation.maxRecords
...
RG_1=mail.megabank.com/login.php?username=admin&login_password=wh3r3sth3b33f?%3f&login=
```


