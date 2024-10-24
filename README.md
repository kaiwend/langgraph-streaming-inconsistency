# How to run

create venv
```sh
python -m venv .venv
```

activate venv
```sh
source .venv/bin/activate
```

install langgraph
```sh
pip install -r requirements.txt
```

run script
```sh
python example.py
```

expected result:
```
on_chain_end {'a': 0, 'b': 0}
on_chain_end {'a': 1}
on_chain_end {'a': 1}
on_chain_end {'b': 1}
on_chain_end {'b': 1}
on_chain_end {'a': 1}
invoke result:  {'a': 1}
**************
graph without output keys defined
**************
on_chain_end {'a': 0, 'b': 0}
on_chain_end {'a': 1}
on_chain_end {'a': 1}
on_chain_end {'b': 1}
on_chain_end {'b': 1}
on_chain_end {'a': 1, 'b': 1}
*** stream outputs ***
{'node_a': {'a': 1}}
{'node_b': {'b': 1}}
**************
graph with output keys (a) defined
**************
on_chain_end {'a': 0, 'b': 0}
on_chain_end {'a': 1}
on_chain_end {'a': 1}
on_chain_end {'b': 1}
on_chain_end {'b': 1}
on_chain_end {'a': 1}
*** stream outputs ***
{'node_a': {'a': 1}}
{'node_b': None}
```
