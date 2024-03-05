import banksData from './banks data.json' assert { type: 'json' };

interface BankInfo {
  id: number;
  type: string;
  nipCode: string;
  name: string;
  slug?: string | null;
  code?: string | null;
  ussd?: string | null;
  logo?: string | null;
}

type BankData = BankInfo[];

export function fetchBanks(): BankData {
  /**
   * Fetches a list of banks and their data.
   * @returns Data on banks.
   */
  return banksData;
}

export function filterBanksByKeyword(keyword: string): BankData {
  /**
   * Filters banks based on a given keyword in their name property.
   * @param keyword The keyword to search for in bank names.
   * @returns A list of bank data that matches the keyword.
   */
  const filteredBanks: BankData = banksData.filter((bank) => bank?.name.toLowerCase().includes(keyword.toLowerCase()));
  return filteredBanks;
}
