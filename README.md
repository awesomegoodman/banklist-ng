# Nigerian Bank List

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![npm version](https://badge.fury.io/js/banklist-ng.svg)](https://www.npmjs.com/package/banklist-ng)

## Overview

The "banklist-ng" package allows you to retrieve a list of Nigerian banks and their details. It is designed for use in client-side JavaScript code, making it easy to incorporate bank data into your web applications or projects. This package simplifies the process of fetching bank information from the Nigerian Banks API and provides an easy-to-use interface to interact with the VendBox API.

## Installation

To use the "banklist-ng" package in your client-side JavaScript project, you can install it via npm. Ensure you have npm installed on your system before proceeding.

N.B.: If you don't have an existing npm project, the installation will automatically create a new project for you.

```bash
npm install banklist-ng --save
```

## Prerequisites

Before using this package, make sure your device is connected to the internet. The package relies on fetching data from the Nigerian Banks API, and an active internet connection is required for it to work properly.

## Getting Started

Install the package:

```bash
npm install banklist-ng --save
```

### Setting up ECMAScript Modules (ESM) Support

This package utilizes ECMAScript modules (`type: "module"`) to take advantage of modern JavaScript features. To use it in your project, you need to set the "type" field to "module" in your `package.json` file.

```json
{
  "type": "module"
}
```

### For Older JavaScript Versions

If you are using an older version of JavaScript that doesn't support ECMAScript modules, you can use Babel or any other transpiler to build your code. This will allow you to import the package using the CommonJS syntax.

In your code:

```javascript
const BankAPI = require("banklist-ng");
```

### Creating a User Instance

To start using the package, you need to create a user instance. There are two methods for creating a user instance, depending on your preferred authentication method:

#### Method 1: Email & Password (for VendBox Account)

```javascript
import BankAPI from 'banklist-ng'; // or const BankAPI = require("banklist-ng");

const verifiedEmail = 'your.verified.vendbox.email@domain.com';
const password = 'your.vendbox.password';
const user = new BankAPI(verifiedEmail, password);
```

#### Method 2: Public API Key (Get from VendBox after Sign-up)

```javascript
import BankAPI from 'banklist-ng';

const publicKey = 'vendbox-pk-your_vendbox_public_key';
const user = new BankAPI(publicKey);
```

### Fetching Bank List

Once you have created the user instance, you can retrieve the list of Nigerian banks. You can pass the desired bank name as an argument to filter the list or leave it empty to fetch all banks.

```javascript
const bankName = 'Zenith'; // Replace with the desired bank name or first few letters of the bank name, or leave empty to fetch ALL BANKS
user.fetchBankList(bankName)
  .then((data) => {
    // Handle the retrieved data as required
    console.log(data);
    // console.log(JSON.stringify(data, null, 2)); //<-- Uncomment this for an expanded view of the banks and their details.
  })
  .catch((error) => {
    // Handle any errors that occur during the API call
    console.error(error);
  });
```

### Sample Response Object

The retrieved bank data object will have the following structure:

```json
{
  "data": [
    {
      "type": "Bank",
      "attributes": {
        "name": "ZENITH BANK",
        "extras": {
          "name": "Zenith Bank",
          "slug": "zenith-bank",
          "code": "057",
          "ussd": "*966#",
          "logo": "https://nigerianbanks.xyz/logo/zenith-bank.png"
        }
      }
    },
    {
      "type": "Bank",
      "attributes": {
        "name": "ZENITH EASY WALLET"
      }
    },
    {
      "type": "Bank",
      "attributes": {
        "name": "ZENITH MOBILE"
      }
    }
  ]
}
```

Here's an explanation of each property:

**Explanation of Properties:**

- **type:** Indicates the type of data (in this case, "Bank").
- **attributes:** Contains the bank details, including "name" (bank name).
- **extras:** (Optional) Additional details about the bank, such as "ussd" (Unstructured Supplementary Service Data) code and "logo" (bank logo URL).

## Important Notes

1. This package is designed for client-side JavaScript code and utilizes ECMAScript modules (`type: "module"`). Ensure your project supports modern JavaScript features.

2. For user authentication, you can use my public key: `vendbox-pk-09ecf162-b3b6-436e-8310-a04644f7eb54`, or my email: `test.user@thevendingdepot.co`, and password `password`.

3. Please make sure you have an active internet connection when using this package to fetch bank data.

## License

This package is open-source and distributed under the [MIT License](https://opensource.org/licenses/MIT).

## Version

Current version: 0.0.2

## Author

Awesome Goodman

## Acknowledgments

Special thanks to the VendBox team for their support and providing the Nigerian Banks API.