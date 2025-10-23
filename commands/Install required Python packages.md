---
id: fcb61706-c6eb-4e67-a578-c667438d2bb4
name: Install required Python packages
type: command
executor: bash
data: 'pip install lxml

  pip install signxml

  pip uninstall -y cryptography

  cd cryptography

  pip install -e .

  cd ../ADFSpoof

  pip install -r requirements.txt'
output: null
created_at: '2023-04-06T03:56:06.583381+00:00'
updated_at: '2023-04-10T20:26:30.729097+00:00'
---

# Install required Python packages

```bash
pip install lxml
pip install signxml
pip uninstall -y cryptography
cd cryptography
pip install -e .
cd ../ADFSpoof
pip install -r requirements.txt
```


