#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
from blockchain import Blockchain, Block
import time


# In[2]:


# Initialize the blockchain
blockchain = Blockchain()

# Define function to add a document to the blockchain
def add_document_to_blockchain(document_content):
    new_block = Block(len(blockchain.chain), document_content, time.time(), blockchain.chain[-1].hash)
    blockchain.add_block(new_block)


# In[3]:


# Streamlit UI
st.title('Blockchain Document Sharing by Ammar Jamshed')


# In[4]:


# Display current blockchain
st.write('Current Blockchain:')
for block in blockchain.chain:
    st.write(vars(block))


# In[6]:


# Document upload
document = st.file_uploader("Upload a document", type=['txt', 'pdf', 'docx'])
if document is not None:
   # For simplicity, this example reads the file content as is
   # For real applications, consider the file format and security implications
   document_content = document.getvalue().decode("utf-8")
   add_document_to_blockchain(document_content)
   st.success('Document added to the blockchain!')
   
   st.write('Updated Blockchain:')
   for block in blockchain.chain:
       st.write(vars(block))

