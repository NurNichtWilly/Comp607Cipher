# Project README

## Overview

This project consists of two main scripts: [`cipher.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fwilly%2FDocuments%2FVSCE%2FCipherSec%2Fcipher.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/willy/Documents/VSCE/CipherSec/cipher.py") and [`deltxts.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fwilly%2FDocuments%2FVSCE%2FCipherSec%2Fdeltxts.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/willy/Documents/VSCE/CipherSec/deltxts.py"). The [`cipher.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fwilly%2FDocuments%2FVSCE%2FCipherSec%2Fcipher.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/willy/Documents/VSCE/CipherSec/cipher.py") script is used for encrypting and decrypting text using various cipher techniques, while the [`deltxts.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fwilly%2FDocuments%2FVSCE%2FCipherSec%2Fdeltxts.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/willy/Documents/VSCE/CipherSec/deltxts.py") script is used for deleting all `.txt` files in a directory.

## Files

- [`cipher.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fwilly%2FDocuments%2FVSCE%2FCipherSec%2Fcipher.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/willy/Documents/VSCE/CipherSec/cipher.py"): Contains functions for text encryption and decryption.
- [`deltxts.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fwilly%2FDocuments%2FVSCE%2FCipherSec%2Fdeltxts.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/willy/Documents/VSCE/CipherSec/deltxts.py"): Deletes all `.txt` files in the current directory.

## Usage

### Cipher Script

The [`cipher.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fwilly%2FDocuments%2FVSCE%2FCipherSec%2Fcipher.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/willy/Documents/VSCE/CipherSec/cipher.py") script provides several encryption techniques including substitution cipher, Caesar shift, XOR encryption, and string reversal. It also includes functions to decrypt the text.

#### Functions

- [`substitutionCipher(str, sourceAlphabet, targetAlphabet)`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2FUsers%2Fwilly%2FDocuments%2FVSCE%2FCipherSec%2Fcipher.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A27%2C%22character%22%3A4%7D%5D "cipher.py"): Substitutes characters in [`str`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2FUsers%2Fwilly%2FDocuments%2FVSCE%2FCipherSec%2Fcipher.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A6%2C%22character%22%3A16%7D%5D "cipher.py") based on the provided alphabets.
- [`caesarShift(str, shift)`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2FUsers%2Fwilly%2FDocuments%2FVSCE%2FCipherSec%2Fcipher.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A6%2C%22character%22%3A4%7D%5D "cipher.py"): Shifts characters in [`str`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2FUsers%2Fwilly%2FDocuments%2FVSCE%2FCipherSec%2Fcipher.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A6%2C%22character%22%3A16%7D%5D "cipher.py") by the specified [`shift`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2FUsers%2Fwilly%2FDocuments%2FVSCE%2FCipherSec%2Fcipher.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A6%2C%22character%22%3A21%7D%5D "cipher.py").
- [`xorEncrypt(str, key)`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2FUsers%2Fwilly%2FDocuments%2FVSCE%2FCipherSec%2Fcipher.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A13%2C%22character%22%3A4%7D%5D "cipher.py"): Encrypts [`str`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2FUsers%2Fwilly%2FDocuments%2FVSCE%2FCipherSec%2Fcipher.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A6%2C%22character%22%3A16%7D%5D "cipher.py") using XOR with the provided [`key`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2FUsers%2Fwilly%2FDocuments%2FVSCE%2FCipherSec%2Fcipher.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A2%2C%22character%22%3A0%7D%5D "cipher.py").
- [`reverseString(str)`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2FUsers%2Fwilly%2FDocuments%2FVSCE%2FCipherSec%2Fcipher.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A22%2C%22character%22%3A4%7D%5D "cipher.py"): Reverses the input string [`str`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2FUsers%2Fwilly%2FDocuments%2FVSCE%2FCipherSec%2Fcipher.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A6%2C%22character%22%3A16%7D%5D "cipher.py").
- [`cipher(text)`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2FUsers%2Fwilly%2FDocuments%2FVSCE%2FCipherSec%2Fcipher.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A34%2C%22character%22%3A4%7D%5D "cipher.py"): Applies a series of encryption techniques to [`text`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2FUsers%2Fwilly%2FDocuments%2FVSCE%2FCipherSec%2Fcipher.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A34%2C%22character%22%3A11%7D%5D "cipher.py").
- [`decipher(text)`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2FUsers%2Fwilly%2FDocuments%2FVSCE%2FCipherSec%2Fcipher.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A55%2C%22character%22%3A4%7D%5D "cipher.py"): Reverses the encryption applied by [`cipher`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2FUsers%2Fwilly%2FDocuments%2FVSCE%2FCipherSec%2Fcipher.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A34%2C%22character%22%3A4%7D%5D "cipher.py").

#### Example

To run the cipher script:

```sh
python cipher.py
```

This will encrypt the text `"The highest bidding price is 406714 NZ$"` and print the ciphered and deciphered text. The results will also be saved to `ciphered.txt` and `deciphered.txt`.

### Delete Text Files Script

The `deltxts.py` script deletes all `.txt` files in the current directory after user confirmation.

#### Example

To run the delete text files script:

```sh
python deltxts.py
```

This will list all `.txt` files in the directory and ask for user confirmation before deleting them.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.


This README provides an overview of the project, instructions on how to use the scripts, and information on contributing and licensing.