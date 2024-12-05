# SVM Wallet Maker

## Features

- Generate any number of Solana wallets
- BIP-44 standard compliance
- Secure mnemonic generation (12 words)
- Export wallet details to CSV
- Optional password protection for mnemonics

## Prerequisites

- Python 3.x
- Required packages:
  ```txt
  bip_utils
  csv
  os
  ```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dannweeeee/svm-wallet-maker.git
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script using Python:

```bash
python solana_wallet_maker.py
```

The script will:

1. Prompt you to enter the number of wallets you want to generate
2. Create the specified number of wallets
3. Save the wallet details to `output/solana_wallets.csv`

### Output Format

The generated CSV file contains the following columns:

- Public Key
- Private Key (Base58)
- Mnemonic

## Security Considerations

- Keep your private keys and mnemonics secure
- Never share your private keys or mnemonics with anyone
- The generated CSV file contains sensitive information - store it safely
- Consider encrypting the output file for additional security