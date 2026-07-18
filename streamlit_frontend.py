import streamlit as st 
from langgraph_backend import chatbot 

CONFIG = { 'configurable' : { 'thread_id' : 'thred-1'}}


# use session state becouse every time we enter the list got erase   
# session state is a dictionary inbuilded in the streamlit  
if 'message_history' not in st.session_state : 
    st.session_state['message_history'] = [ ]


# { 'role' : 'user' , 'content' : 'hi'}

## history 
for message in st.session_state['message_history']   : 
    with st.chat_message(message['role']) : 
        st.text( message['content'])


user_input = st.chat_input('Type Here ...')

if user_input  :
    st.session_state['message_history'].append( {'role' : 'user' , 'content' : user_input })

    with st.chat_message('user') : 
        st.text( user_input )

    response = chatbot.invoke({"messages" : ('human' , user_input ) } , config = CONFIG  )
     
    ai_message = response['messages'][-1].content
    st.session_state['message_history'] .append( {'role' : 'assistant' , 'content' : ai_message  })
    with st.chat_message('assistant') :  
        st.text(ai_message)

    