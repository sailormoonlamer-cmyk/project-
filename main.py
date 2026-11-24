from Bank_exceptions import *
from Bank_classes import Bank
from utils import print_menu

# Бизнес-логика 

def main():
    bank = Bank("Мой банк")
    
    try:
        
        bank.create_account("Иван Петров", 50000)
        bank.create_account("Мария Иванова", 80000)
        bank.create_account("Алексей Петров", 20000)
    
    except BankError as e:
        print(f'Ошибка создания тестовых счетов: {e}')
        return
    
    print("Добро пожаловать в банк! ")
    while True:
        print_menu()
        choice = input("Выберите действие: ").strip()
        
        
        try:
            if choice == '1':
                print("Создание нового счета: ")
                owner = input("Введите свое имя: ").strip()
                
                balance = input("Введите начальный баланс: ").strip()
                if balance:
                    balance = float(balance)
                
                else:
                    balance = 0
                
                bank.create_account(owner, balance)  
            
                    
                print(" ")     
            
            
            
            elif choice == '2':
                bank.show_all_accounts()
        
        
        
            elif choice == "3":
                account_number = input("Введите номер счета: ").strip()
                account = bank.find_account(account_number)
                if not account:
                    print(f"Счет {account_number} не найден! ")
                    continue
                amount = float(input("Введите сумму пополнения ").strip())
                account.deposit(amount)
                print(" ")
            
            
                
            elif choice == '4':
                account_number = input("Введите номер счета: ").strip()
                account = bank.find_account(account_number)
                if not account:
                    print(f"Счет {account_number} не найден! ")
                    continue
                amount = float(input("Введите сумму снятия ").strip())
                account.withdraw(amount)
                print(" ")
            
            
                
            elif choice == '5':
                user1 = input("Введите номер счета отправителя: ").strip()
                from_user1 = bank.find_account(user1)
                if not from_user1:
                    print(f"Счет {user1} не найден! ")
                    continue
                user2 = input("Введите номер счета получателя: ")
                to_user2 = bank.find_account(user2)
                if not to_user2:
                    print(f"Счет {user2} не найден! ")
                    continue
                amount = float(input("Введите сумму перевода: ").strip())
                from_user1.transfer(amount, to_user2)
                print(" ")
            
            
            
            elif choice == '6':                                                                                 
                account_number = input("Введите номер счета: ").strip()
                account = bank.find_account(account_number)                                                             
                if not account:
                    print("Счет не найден! ")
                    continue
                print(f'Баланс счета:{account} руб')
            
            
                
            elif choice == '7':
                account_number = input("Введите номер счета: ").strip()
                account = bank.find_account(account_number)
                if not account:
                    print(f'Счет {account_number} не найден!')
                    continue
            
            
                
            elif choice == '8':
                account_number = input("Введите номер счета: ").strip()
                account = bank.find_account(account_number)
                if account:
                    print(account)
                else:
                    print(f'Счет {account_number} не найден!')
            
            
                    
            elif choice == '9':
                owner = input("Введите имя владельца: ").strip()
                account = bank.find_account(account_number)
                if account:
                    print(account)
                else:
                    print("Счета владельца не найдены!")
            
            
            
            elif choice == '10':
                account_number = input("Введите номер счета: ").strip()
                if bank.delete_account(account_number):
                    print("Счет успешно закрыт!")
                else:
                    print("Счеь не удалось закрыть!")
            
            
                
            elif choice == '11':
                print(f'Навазние банка:{bank.name}')
                print(f'Количетсво счетов:{len(bank.accounts)}')
                print(f'Общий баланс::{bank.get_total_balance()}')
            
            
                
            elif choice == '0':
                print("Спасибо за использование банком!")
                break
            
            else:
                print("НЕ ВЕРНАЯ КОМАНДА! введите номер от 0 до 11/n")
                
                
        # except BankError as e:
        #     print(f'Ошибка: {e}')           
        
        
        except InvalidOwnerError as e:
            print(f'Ошибка владельца: {e}')    
        
        except  InvalidAmountError as e:
            print(f'Ошибка суммы: {e}')
        
        except InvalidBalanceError as e:
            print(f'Ошибка баланса: {e}') 
        
        except InsufficientFundsError as e:
            print(f'Ошибка: {e}') 
        
        except CreateAcountError as e:
            print(f'Ошибка создания: {e}')
        
        except AcountFoundError as e:
            print(f'Ошибка поиска : {e}')
        
        except BankError as e:
            print(f'Банковская оишбка: {e} ')
        

        
        
        
if __name__ == "__main__":
    main()        