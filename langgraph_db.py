from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_groq import ChatGroq
from langgraph.graph.message import add_messages
from langgraph.checkpoint.sqlite   import SqliteSaver  
from dotenv import load_dotenv
import sqlite3 


CONFIG = { "configurable" : { "thread_id" : "thred-1"}}


load_dotenv( )

class ChatState(TypedDict):

    messages: Annotated[list[BaseMessage], add_messages]



llm = ChatGroq(model= "openai/gpt-oss-120b",temperature=0.7)


def chat_node(state: ChatState):

        # take user query from state
        messages = state['messages']

        # send to llm
        response = llm.invoke(messages)

        # response store state
        return {'messages': [response]}



# database 
conn = sqlite3.connect( database= "chatbot_db" , check_same_thread=False)  # same database is used in different threads 


## checkpointer 
checkpointer = SqliteSaver(conn= conn  ) 



graph = StateGraph(ChatState)
# add nodes
graph.add_node('chat_node', chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot = graph.compile(checkpointer= checkpointer )


## get a total no of checkpoints
def retrive_all_treads( ) : 
    all_thread = set( ) 
    for checkpoints in checkpointer.list(None) :    # checkpointer list give the all threadss 
        all_thread.add(checkpoints.config['configurable']['thread_id']) 

    return list(all_thread) 

