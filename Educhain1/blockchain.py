import hashlib
import json
import datetime


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = {
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }

        block_string = json.dumps(
            block_data, sort_keys=True
        ).encode("utf-8")

        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty=3):
        target = "0" * difficulty

        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()


class EduChain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(
            0,
            str(datetime.datetime.now()),
            {"message": "EduChain Genesis Block"},
            "0"
        )

    def get_latest_block(self):
        return self.chain[-1]

    def add_certificate(self, student_id, certificate_hash,
                        issuer, certificate_type):
        data = {
            "student_id": student_id,
            "certificate_hash": certificate_hash,
            "issuer": issuer,
            "certificate_type": certificate_type,
            "issued_date": str(datetime.date.today())
        }

        new_block = Block(
            len(self.chain),
            str(datetime.datetime.now()),
            data,
            self.get_latest_block().hash
        )

        new_block.mine_block()
        self.chain.append(new_block)

    def verify_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                return False

            if current.previous_hash != previous.hash:
                return False

        return True

    def find_student_records(self, student_id):
        return [
            block.data
            for block in self.chain
            if block.data.get("student_id") == student_id
        ]

    def display_chain(self):
        print("\n========== EDUCATION BLOCKCHAIN ==========")

        for block in self.chain:
            print("\nBlock:", block.index)
            print("Timestamp:", block.timestamp)
            print("Data:", json.dumps(block.data, indent=4))
            print("Previous Hash:", block.previous_hash)
            print("Hash:", block.hash)
            print("Nonce:", block.nonce)

        print("\n==========================================")


# Compatibility name if your old code imports EduBlockchain.
Blockchain = EduChain
