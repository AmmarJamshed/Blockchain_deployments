#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest
from blockchain import Blockchain, add_document_to_blockchain


# In[2]:


class BlockchainDocumentTest(unittest.TestCase):
    def setUp(self):
        """Set up a new blockchain for each test."""
        self.blockchain = Blockchain()

    def test_document_block_addition(self):
        """Test adding a document to the blockchain."""
        document_content = "This is a sample document."
        add_document_to_blockchain(self.blockchain, document_content)
        
        # Verify the blockchain now has two blocks (genesis block + document block)
        self.assertEqual(len(self.blockchain.chain), 2)
        
        # Verify that the last block in the chain contains the document
        last_block = self.blockchain.chain[-1]
        self.assertEqual(last_block.documents, document_content)
        
        # Verify the integrity of the blockchain
        self.assertTrue(verify_blockchain(self.blockchain), "The blockchain is invalid. ")


# In[5]:


def verify_blockchain(blockchain):
    """Function to verify the integrity of the blockchain."""
    for i in range(1, len(blockchain.chain)):
        current_block = blockchain.chain[i]
        previous_block = blockchain.chain[i-1]

        # Check current block's hash is correct
        if current_block.hash != current_block.calculate_hash():
            return False
        # Check current block's previous hash matches the previous block's hash
        if current_block.previous_hash != previous_block.hash:
            return False
    return True

