from banks_data import extra_bank_data
from typing import List, Dict, Optional, TypedDict, Literal
import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()

ANCHOR_API_KEY = os.getenv('ANCHOR_API_KEY')
ANCHOR_BASE_URL = "https://api.sandbox.getanchor.co"


class BankAttributes(TypedDict):
   """
   Represents the attributes of a bank entity.
   """
   nipCode: str
   name: str
   cbnCode: Optional[str]

class AnchorBankInfo(TypedDict):
   """
   Represents information about a bank entity on Anchor.
   """
   id: str
   type: str
   attributes: BankAttributes

class AnchorBankData(TypedDict):
   """
   Represents a collection of bank data on Anchor.
   """
   data: List[AnchorBankInfo]

class BankInfo(TypedDict, total=False):
   """
   Represents a collection of bank data.
   """
   id: int
   type: str
   name: str
   nipCode: str
   cbnCode: str
   slug: str
   code: str
   ussd: str
   logo: str

class MergedData(TypedDict):
   data: List[BankInfo]


# Get the current working directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Set the base directory by getting the parent directory of the current directory
BASE_DIR = os.path.dirname(current_dir)
JSON_FILE_NAME = 'banks data.json'
PACKAGE_NAME = 'banklist-ng'


def fetch_banks() -> List[BankInfo]:
   """
   Fetches a list of banks and their data.

   Returns: Data on banks of type BankData
   """
   banks_url = f"{ANCHOR_BASE_URL}/api/v1/banks"
   response = requests.get(banks_url, headers={ "accept": "application/json", "x-anchor-key": ANCHOR_API_KEY })
   
   bank_data: AnchorBankData = response.json()

   transformed_data: Dict[Literal["data"], List[BankInfo]] = {
      "data": [
         {
               "id": index + 1,
               "type": bank["type"],
               "name": bank["attributes"]["name"],
               "nipCode": bank["attributes"]["nipCode"],
               # "cbnCode": bank["attributes"].get("cbnCode", ""),
               
         }
         for index, bank in enumerate(bank_data["data"])
      ]
   }
   
   # Merge the fetched bank data with extra bank data
   merged_data: MergedData = {"data": []}
   for bank_info in transformed_data["data"]:
      # Convert both names to lowercase for case-insensitive comparison
      bank_name_lower = bank_info["name"].lower()
      for extra_info in extra_bank_data:
         if extra_info["name"].lower() == bank_name_lower:
               merged_info = bank_info.copy()
               merged_info.update(extra_info)
               merged_data["data"].append(merged_info)
               break
      else:
         merged_data["data"].append(bank_info)
   
   return merged_data["data"]


banks_data = fetch_banks()

def save_banks_to_json():
   """
   Saves the bank data to a JSON file.
   """
   
   json_output_path = os.path.join(BASE_DIR, 'resources', JSON_FILE_NAME)
   npm_output_path = os.path.join(BASE_DIR, 'npm', 'src', PACKAGE_NAME, JSON_FILE_NAME)
   pypi_output_path = os.path.join(BASE_DIR, 'pypi', 'src', PACKAGE_NAME.replace('-', '_'), JSON_FILE_NAME) # Convert dashes to underscores in the package name

   # Convert STATES data into JSON format
   banks_json = json.dumps(banks_data, indent=4)

   # Save JSON data to the specified file paths
   with open(json_output_path, 'w') as json_file:
      json_file.write(banks_json)
      print(f"\nConversion completed. JSON file saved at: {json_output_path}\n")
   with open(npm_output_path, 'w') as npm_json_file:
      npm_json_file.write(banks_json)
      print(f"Conversion completed. NPM JSON file saved at: {npm_output_path}\n")
   with open(pypi_output_path, 'w') as pypi_json_file:
      pypi_json_file.write(banks_json)
      print(f"Conversion completed. PyPi JSON file saved at: {pypi_output_path}\n")

if __name__ == '__main__':
   save_banks_to_json()