---
id: b10fc917-52ca-4954-a6ac-e2fad691fb08
name: build dns subdomain wordlist with sed
type: command
executor: ''
data: sed 's/$/.$_TARGET_DOMAIN/' $_SECLISTS_WORDLIST > $_OUTPUT_FILE
output: 'root@hacker:~# sed ''s/$/.owasp.org/'' /opt/SecLists/Discovery/DNS/subdomains-top1million-20000.txt
  > hosts-wordlist.txt

  www.owasp.org

  mail.owasp.org

  ftp.owasp.org

  localhost.owasp.org

  webmail.owasp.org

  smtp.owasp.org

  webdisk.owasp.org

  pop.owasp.org

  cpanel.owasp.org

  whm.owasp.org

  ... CUT'
created_at: '2020-06-30T04:41:15.217716+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# build dns subdomain wordlist with sed

```bash
sed 's/$/.$_TARGET_DOMAIN/' $_SECLISTS_WORDLIST > $_OUTPUT_FILE
```

## Expected Output

```
root@hacker:~# sed 's/$/.owasp.org/' /opt/SecLists/Discovery/DNS/subdomains-top1million-20000.txt > hosts-wordlist.txt
www.owasp.org
mail.owasp.org
ftp.owasp.org
localhost.owasp.org
webmail.owasp.org
smtp.owasp.org
webdisk.owasp.org
pop.owasp.org
cpanel.owasp.org
whm.owasp.org
... CUT
```


