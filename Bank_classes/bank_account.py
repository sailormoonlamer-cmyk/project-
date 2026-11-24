import random
import datetime
from Bank_exceptions.exceptions import InvalidAmountError, InvalidOwnerError, InsufficientFundsError

class BankAccount:
  
    def __init__(self, owner, balance = 0):
        self.__owner = None
        self.owner = owner # Через сеттер
        self.__balance = 0
        self.balance = balance
        
        self.account_number = self.get_account_number()
        self.created_at = datetime.datetime.now()
        self.transaction_history = []
    
    # Геттер на имя владельца    
    @property
    def owner(self) -> str:
        return self.__owner
    
    @owner.setter
    def owner(self, value: str):
        if not value or not value.strip():
            raise InvalidOwnerError("Имя владельца не может быть пустым!! ")
        self.__owner = value.strip()
        
    
    
    @property
    def balance(self) -> float:
        return self.__balance
    
    @balance.setter
    def balance(self, value: float):
        if value < 0:
            raise InvalidAmountError("Баланс не может быть отрицательным!! ")
        self.__balance = value
        
      
        
        
        
        
    
    def get_account_number(self) -> int:
        return f'{random.randint(1000,9999)}-{random.randint(1000,9999)}'



    def deposit(self, amount: float):
        if amount <= 0:
            raise InvalidAmountError("ОШИБКА!!! Сумма должна быть больше нуля!! ")
            return False
        
        self.balance += amount
        transaction = f'Пополнение: +{amount}руб. | Баланс:{self.balance}руб.'
        self.transaction_history.append(transaction)
        print(f'Счет пополнен на {amount}руб. | текущий баланс {self.balance}руб.')
        return True
 
 
 
    def withdraw(self, amount: float):
        if amount <= 0:
            raise InvalidAmountError("ОШИБКА!!! Сумма должна быть больше нуля!! ")
            return False
        
        if amount > self.balance:
            raise InsufficientFundsError(self.balance)
            return False
        
        self.balance -= amount
        transaction = f'Cнятие: -{amount}руб. | Баланс:{self.balance}руб.'
        self.transaction_history.append(transaction)
        print(f'Снято {amount}руб. | текущий баланс {self.balance}руб.')
        return True



    def transfer(self, amount: float, target_account):
        if amount <= 0:
            raise InvalidAmountError(self.balance)
            return False
            
        if amount > self.balance:
            raise InsufficientFundsError(f'НЕ ДОСТАТОЧНО СТРЕДСТВ| на балансе: {self.balance}')
            return False
        
        self.balance -= amount
        transaction = f'Перевод: -{amount}руб. на счет {target_account.account_number}| Баланс:{self.balance}руб.'
        self.transaction_history.append(transaction)
        
        target_account.balance += amount
        transaction = f'Перевод: +{amount}руб. c счета {self.balance}| Баланс:{target_account.balance}руб.'
        self.transaction_history.append(transaction)
        
        print(f'Переведено {amount}руб. на счет {target_account.account_number}| ваш баланс {self.balance}руб.')
        return True
 
 
 
    def get_balance(self) -> float:
        return self.balance
   
   
   
    def show_transaction(self) -> None:
        if not self.transaction_history:
            print("История операций пуста!! ")
            return
        print(F'История операций для счета {self.account_number}')
        for i, transaction in enumerate(self.transaction_history):
            print(f'{i+1}, {transaction}')
        print("-" * 50)    



    def __str__(self) -> str:
        return f'Счет: {self.account_number}|Владелец:{self.owner}|Баланс:{self.balance} рублей' 