#!/usr/bin/env python
# coding: utf-8

# ### Each block in the blockchain will contain multiple pieces of information, but for sharing documents, the critical parts are the document itself 

# In[2]:


# import hash lib and time
import hashlib
import time


# In[5]:


# CLASS WITH MULTIPLE FUNCTIONS
class Block:
    def __init__(self, index, documents, timestamp, previous_hash):
        self.index = index
        self.documents = documents  # This could be a list of documents or a single document
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_content = f"{self.index}{self.documents}{self.timestamp}{self.previous_hash}"
        return hashlib.sha256(block_content.encode()).hexdigest()


# In[6]:


# BLOCKCHAIN STRUCTURE
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", time.time(), "0")

    def add_block(self, new_block):
        new_block.previous_hash = self.chain[-1].hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)


# In[8]:


# fUNCTIONALITY TO ADD DOCUMENT
def add_document_to_blockchain(blockchain, document):
    new_block = Block(len(blockchain.chain), document, time.time(), blockchain.chain[-1].hash)
    blockchain.add_block(new_block)

# Initialize blockchain
my_blockchain = Blockchain()

# Example of adding a document
add_document_to_blockchain(my_blockchain, "Document 1 Content or Reference")


# In[9]:


# vERIFY BLOCKCHAIN
def verify_blockchain(blockchain):
    for i in range(1, len(blockchain.chain)):
        current_block = blockchain.chain[i]
        previous_block = blockchain.chain[i-1]

        if current_block.hash != current_block.calculate_hash():
            return False
        if current_block.previous_hash != previous_block.hash:
            return False
    return True


# In[ ]:




