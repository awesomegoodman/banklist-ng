# Nigerian Bank List (banklist-ng)

The `banklist-ng` library provides information about Nigerian banks including the bank's type, NIP code, name, slug, code, USSD, and logo.

## Installation

You can install the package via npm:

```bash
npm install banklist-ng
```

## Usage

### Importing

```javascript
import { fetchBanks, filterBanksByKeyword } from 'banklist-ng';

// Fetch all banks data
const allBanksData = fetchBanks();
console.log(allBanksData);

// Filter banks by keyword
const keyword = 'Zenith';
const zenithBanks = filterBanksByKeyword(keyword);
console.log(`Banks matching '${keyword}':`, zenithBanks);
```

### Functions

- `fetchBanks(): BankData`: Fetches a list of all Nigerian banks with their data.

- `filterBanksByKeyword(keyword: string): BankData`: Filters banks based on a given keyword in their name property.

### Type Definitions

- `BankInfo`: Represents the data structure for information about a bank, including its ID, type, NIP code, name, slug, code, USSD, and logo.

- `BankData`: Represents a collection of bank information.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.

## GitHub Repository

You can find the source code and contribute to this project on GitHub: [Bank List NG on GitHub](https://github.com/awesomegoodman/banklist-ng)
