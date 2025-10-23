---
id: 2ee053f5-bc82-4507-a981-cec5be5951c1
name: Generating Passwords and Credentials
type: cheatsheet
verified: true
created_at: '2019-09-30T19:48:33.849231+00:00'
updated_at: '2023-05-30T20:05:52.591919+00:00'
---

# Generating Passwords and Credentials

**Status**: ✓ Verified

## Description

Instructions on generating passwords, credentials,.



## Generate OpenSSL Private Keys and Certificates 





**Command** ([[OpenSSL Generate a Private Key]]):

```bash
openssl genrsa -out $_KEY 4096
```









**Command** ([[OpenSSL Generate a CA Certificate]]):

```bash
openssl req -x509 -new -nodes -key $_ROOT_CA -sha256 -days 365 -out $_ROOT_CA_CRT
```









**Command** ([[OpenSSL Generate a CSR from a Private Key]]):

```bash
openssl req -new -key $_PRIVATE_KEY -out $_PRIVATE_CSR
```









**Command** ([[OpenSSL Sign a CSR with a CA Key]]):

```bash
openssl x509 -req -in $_PRIVATE_CSR -CA $_ROOT_CA_CRT -CAkey $_ROOT_CA -CAcreateserial -out $_PRIVATE_CRT -days 365 -sha256
```









**Command** ([[OpenSSL Generate a PKCS12 with a Private Key and CRT]]):

```bash
openssl pkcs12 -export -out $_PKCS12.pfx -inkey $_PRIVATE_KEY -in $_SIGNED_CRT
```









**Command** ([[OpenSSL View RSA Key Information]]):

```bash
openssl rsa -in $_PRIVATE_KEY -text -noout
```









**Command** ([[OpenSSL Compare the Modulus of a CRT and Private Key]]):

```bash
openssl x509 -noout -modulus -in $SIGNED_CRT | md5sum; 
openssl rsa -noout -modulus -in $_PRIVATE_KEY | md5sum
```





## Generate  Credentials with PowerShell





**Command** ([[PowerShell Generate a Secure String]]):

```bash
$pass = ConvertTo-SecureString "$_PASSWORD" -AsPlainText -Force
```









**Command** ([[PowerShell Generate Credentials Using a Secure String]]):

```bash
$creds = New-Object System.Management.Automation.PSCredential('$_COMPUTER_NAME/$_USERNAME', $pass)
```









**Command** ([[PowerShell Extract Password from Secure String Credentials]]):

```bash
$creds.getnetworkcredential() | fl *
```









**Command** ([[PowerShell Print a Secure String]]):

```bash
 $_SECURE_STRING |ConvertFrom-SecureString
```







## Generate Password Hashes for /etc/shadow





**Command** ([[mkpasswd Generate a SHA512-crypt hash]]):

```bash
mkpasswd -m sha512crypt -S $_SALT $_PASSWORD
```









**Command** ([[OpenSSL Generate a SHA512-crypt hash]]):

```bash
openssl passwd -6 -salt $_SALT $_PASSWORD
```









**Command** ([[mkpasswd Generate a MD5 Hash]]):

```bash
mkpasswd -5 -S $_SALT $_PASSWORD
```










