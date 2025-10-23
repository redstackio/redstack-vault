---
id: 8fa9aa94-d69c-487a-8609-6e8c8ebd69ef
name: convert tickets between linux / windows format
type: command
executor: bash
data: 'python ticket_converter.py ticket.kirbi ticket.ccache

  python ticket_converter.py ticket.ccache ticket.kirbi

  '
output: null
created_at: '2020-07-14T18:14:59.605634+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# convert tickets between linux / windows format

```bash
python ticket_converter.py ticket.kirbi ticket.ccache
python ticket_converter.py ticket.ccache ticket.kirbi

```


