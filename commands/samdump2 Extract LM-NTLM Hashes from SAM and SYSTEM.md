---
id: 2c444605-0b52-4ddd-a201-6794dc4c931f
name: samdump2 Extract LM/NTLM Hashes from SAM and SYSTEM
type: command
executor: bash
data: samdump2 SYSTEM SAM
output: 'root@kali:~# samdump2 SYSTEM SAM

  *disabled* Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::

  *disabled* Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::

  Bob:1000:aad3b435b51404eeaad3b435b51404ee:81ABA903C80B8F4DAAD5225F7D996FBC:::'
created_at: '2019-12-28T01:37:58.768729+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# samdump2 Extract LM/NTLM Hashes from SAM and SYSTEM

```bash
samdump2 SYSTEM SAM
```

## Expected Output

```
root@kali:~# samdump2 SYSTEM SAM
*disabled* Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
*disabled* Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Bob:1000:aad3b435b51404eeaad3b435b51404ee:81ABA903C80B8F4DAAD5225F7D996FBC:::
```


