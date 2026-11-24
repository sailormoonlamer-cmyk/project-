from .bank_account import BankAccount
from Bank_exceptions.exceptions import CreateAcountError, AcountFoundError, InvalidBalanceError




class Bank:  

        
    def __init__(self, name: str):
        self.name = name
        self.accounts = []
  
  
  
    def create_account(self, owner: str, initial_balance: float = 0) -> BankAccount:
        for account in self.accounts:
            if account.owner.lower() == owner.lower():
                raise CreateAcountError(owner, account.account_number)
                
                return None
            
        new_account = BankAccount(owner, initial_balance)  
        
        self.accounts.append(new_account)
        
        print("Счет успешно создан")
        print(f'Владелец: {owner}|номер счета:{new_account.account_number}|начальный баланс:{initial_balance}руб')
        return new_account
    
    
    
    def find_account(self, account_number: str) -> BankAccount:
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None
    
    
    
    def find_accounts_by_owner(self, owner: str):
        found = []
        for account in self.accounts:
            if account.owner.lower() == owner.lower():
                found.append(account)
        return found
         
         
                
    def get_total_balance(self) -> float:
        total = 0
        for account in self.accounts:
            total += account.balance
        return total
    
    
    
    def show_all_accounts(self) -> None:
        if not self.accounts:
            print("В банке нет счетов")
            return
        print(f"Все в банке '{self.name}' ")
        for i , account in enumerate(self.accounts):
            print(f'{i+1}. {account}')
            
        print(f'Общая сумма средств в банке: {self.get_total_balance()} рублей ')
        
        
        
    def delete_account(self, account_number: str) -> bool:
        account = self.find_account(account_number)
        
        if not account:
            raise AcountFoundError(account_number)
            return False
        
        if account.balance != 0:
            raise InvalidBalanceError(account.balance)
            return False
        
        self.accounts.remove(account)
        print(f'Счет {account_number} закрыт! ')
        return True