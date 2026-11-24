


class BankError(Exception):
    """Базовое исключения для всех банковских ошибок"""
    pass


# Ошибки валидация
class InvalidOwnerError(BankError):
    """Имя владельца пустое или некорректное"""
    pass
class InvalidAmountError(BankError):
    """Сумма операции некорректна(<=0, не число, NaN)"""
    pass


class InvalidBalanceError(BankError):
    """Недостаточно средств для снятия или перевода"""
    def __init__(self, balance):
        self.balance = balance
        super().__init__(f"❌ Нельзя закрыть счет с остатком {balance} руб.\n")
        
        
# Ошибки операций
class InsufficientFundsError(BankError):
    """Недостаточно средств для снятия или перевода"""
    def __init__(self, available):
        self.available = available
        super().__init__(f"❌Недостаточно средств! Доступно: {available} руб.")
        
        
class CreateAcountError(BankError):
    """Недостаточно средств для снятия или перевода"""
    def __init__(self, owner, account_num):
        self.owner = owner
        self.account_num = account_num
        super().__init__(f"❌ У пользователя {owner} уже есть счет: {account_num}")
        
class AcountFoundError(BankError):
    """Недостаточно средств для снятия или перевода"""
    def __init__(self, account_num):
        self.account_num = account_num
        super().__init__(f"❌ Счет {account_num} не найден")     
        