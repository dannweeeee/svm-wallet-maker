from bip_utils import (Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes, base58, Bip39MnemonicGenerator, Bip39WordsNum)
import csv
import os

class SolanaWalletGenerator:
    def __init__(self, mnemonic: str, password: str = ''):
        """
        Initializes the wallet generator with a mnemonic and an optional password.
        :param mnemonic: The BIP-39 mnemonic phrase.
        :param password: Optional password for the mnemonic.
        """
        self.mnemonic = mnemonic.strip()
        self.password = password

    def get_address_and_private_key(self, account_index: int = 0):
        """
        Derives the Solana address and private key using the BIP-44 standard.
        :param account_index: Index of the account in the derivation path.
        :return: A tuple containing the Solana public address and Base58-encoded private key.
        """
        # generate the seed from the mnemonic
        seed_bytes = Bip39SeedGenerator(self.mnemonic).Generate(self.password)

        # derive the BIP-44 path for Solana
        bip44_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.SOLANA)
        bip44_acc_ctx = bip44_ctx.Purpose().Coin().Account(account_index)

        # get private and public keys
        priv_key_bytes = bip44_acc_ctx.PrivateKey().Raw().ToBytes()
        public_key_bytes = bip44_acc_ctx.PublicKey().RawCompressed().ToBytes()[1:]

        # concatenate private and public key bytes for Solana format
        key_pair = priv_key_bytes + public_key_bytes

        # return address and Base58-encoded private key
        return bip44_acc_ctx.PublicKey().ToAddress(), base58.Base58Encoder.Encode(key_pair)

# function to create a specified number of Solana wallets
def create_solana_wallets(num_wallets, output_file):
    # Check if output directory exists, if not create it
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    wallets = []

    # generate wallets with different mnemonics
    for i in range(num_wallets):
        # generate a random mnemonic for each wallet
        mnemonic = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_12)
        mnemonic_str = mnemonic.ToStr()  # convert Bip39Mnemonic object to string
        generator = SolanaWalletGenerator(mnemonic_str)
        public_key, private_key = generator.get_address_and_private_key()
        wallets.append({
            "public_key": public_key,
            "private_key": private_key,
            "mnemonic": mnemonic_str
        })

    # write wallets to a CSV file
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Public Key", "Private Key (Base58)", "Mnemonic"])
        for wallet in wallets:
            writer.writerow([wallet["public_key"], wallet["private_key"], wallet["mnemonic"]])

    print(f"Successfully created {num_wallets} wallets. Details saved to {output_file}")

if __name__ == "__main__":
    num_wallets = int(input("Enter the number of wallets to create: "))
    output_file = "output/solana_wallets.csv"  
    create_solana_wallets(num_wallets, output_file)