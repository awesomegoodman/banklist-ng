# Nigerian Bank Data Conversion

This Python script fetches data about Nigerian banks from an external API and merges it with additional bank data to create a comprehensive JSON file. The JSON file includes details such as bank name, NIP code, CBN code, slug, USSD code, and logo.

## Usage

1. Ensure you have the necessary dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```

2. Set the base directory (`BASE_DIR`) in the script to the desired location where you want the JSON files to be saved.

3. Run the script:

   ```bash
   python banks.py
   ```

4. The converted JSON files will be saved in the specified location.

## Additional Features

- **Data Fetching:**

  - The script fetches bank data from an external API using an API key for authentication.

- **Data Merging:**

  - It merges the fetched bank data with additional bank data provided in a predefined list.

- **Error Handling:**

  - The script includes error handling for API requests and data processing to ensure smooth execution.

- **JSON Output:**

  - The output JSON file contains comprehensive information about each bank, including additional data merged from the predefined list.
