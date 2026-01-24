#!/usr/bin/env python3
import time
import base64
import hashlib
import sys
import secrets

class Block:
    def __init__(self, index, previous_hash, timestamp, encoded_transactions, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.encoded_transactions = encoded_transactions
        self.nonce = nonce
    
    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.encoded_transactions}{self.nonce}"
        print("\nBlock strings:",block_string)
        print("Encoded blocks strings:",block_string.encode())
        print("Hashed blocks strings:",hashlib.sha256(block_string.encode()).hexdigest())
        print("Digest Hexa Hex value: ",hashlib.sha256(block_string.encode()).hexdigest())
        
        return hashlib.sha256(block_string.encode()).hexdigest()

def proof_of_work(previous_block, encoded_transactions):
    print("\nNew Block Previous Block:",previous_block.calculate_hash())
    print("New Block Encoded Transactions:",encoded_transactions)
    index = previous_block.index + 1
    print("New Block Index Now:",index)
    timestamp = int(time.time())
    print("New Block Timestamp:",timestamp)
    nonce = 0
    print("New Block Nonce:",nonce)

    block = Block(index, previous_block.calculate_hash(),
                  timestamp, encoded_transactions, nonce)
    
    while not is_valid_proof(block):
        print("Nonce bertambah 1")
        nonce += 1
        block.nonce = nonce
    
    return block

def is_valid_proof(block: Block):
    guess_hash = block.calculate_hash()
    print("Guess Hash:",guess_hash)
    print("Guess Hash 2 first index:",guess_hash[:2])
    return guess_hash[:2] == "00"

def get_all_blocks(blockchain):
    return blockchain

def blockchain_to_string(blockchain):
    block_strings = [f"{block.calculate_hash()}" for block in blockchain]
    return '-'.join(block_strings)

def generate_random_string(length):
    return secrets.token_hex(length // 2)

random_string = generate_random_string(64)

def main(token):
    key = bytes.fromhex(random_string)
    print("Key:", key)
    print("Key decode:",key.hex())

    genesis_block = Block(0,"0", int(time.time()), "EncodedGenesisBlock", 0)
    blockchain = [genesis_block]
    print("Genesis Block:",dir(genesis_block))
    print("The blockchain:",dir(blockchain))

    for i in range(1,5):
        encoded_transactions = base64.b64encode(f"Transaction_{i}".encode()).decode('utf-8')
        print(f"\n================================================\nEncoded Transactions_{i}: {encoded_transactions}\n================================================")
        new_block = proof_of_work(blockchain[-1], encoded_transactions)
        print(f"New Blocks Ditambahkan: {new_block.calculate_hash()}")
        blockchain.append(new_block)
    
    all_blocks = get_all_blocks(blockchain)
    print("\nSEMUA BLOCKS")
    # for block in all_blocks:
    #     print(block.calculate_hash())
    blockchain_string = blockchain_to_string(all_blocks)
    print(blockchain_string,len(blockchain_string))
    pass


if __name__ == "__main__":
    text = sys.argv[1]
    main(text)