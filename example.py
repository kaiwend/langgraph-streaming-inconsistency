from typing import TypedDict

from langchain_core.callbacks.base import BaseCallbackHandler
from langchain_core.runnables.config import RunnableConfig
from langgraph.graph import END, StateGraph
from langgraph.graph.graph import START


class CustomCallbackHandler(BaseCallbackHandler):
    def on_chain_end(self, _outputs, **kwargs):
        print("on_chain_end", _outputs)


class OutputType(TypedDict):
    a: int


class State(TypedDict):
    a: int
    b: int


graph = StateGraph(State, output=OutputType)
graph.add_node("node_a", lambda state: {"a": state["a"] + 1})
graph.add_node("node_b", lambda state: {"b": state["b"] + 1})

graph.add_edge(START, "node_a")
graph.add_edge("node_a", "node_b")
graph.add_edge("node_b", END)

input = {"a": 0, "b": 0}

config = RunnableConfig(callbacks=[CustomCallbackHandler()])

compiled_graph = graph.compile()

invoke_result = compiled_graph.invoke(input, config)
print("invoke result: ", invoke_result)

print("**************")
print("graph without output keys defined")
print("**************")
graph_without_output_keys_results = []
for stream_output in compiled_graph.stream(input, config):
    graph_without_output_keys_results.append(stream_output)

print("*** stream outputs ***")
for stream_output in graph_without_output_keys_results:
    print(stream_output)

print("**************")
print("graph with output keys (a) defined")
print("**************")
graph_with_output_keys_results = []
for stream_output in compiled_graph.stream(input, config, output_keys=["a"]):
    graph_with_output_keys_results.append(stream_output)

print("*** stream outputs ***")
for stream_output in graph_with_output_keys_results:
    print(stream_output)
