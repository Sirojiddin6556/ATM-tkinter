import re
class BankSystem:
    
    def __init__(self):
        self.user = 'user'
        self.card_number = []
        self.user_id = []
        self.balance = []
        self.pin_code = []
        self.phone_number = []
        self.transactions = []
        self.nalik = []
        
        return self.Res()
    def Res(self):
        with open('Bank.txt', 'r' , encoding="UTF8") as read1:
            b1 = re.findall(r'\d+', read1.read())
            self.card_number = b1[0]
            self.user_id = b1[1]
            self.balance = b1[2]
            self.pin_code = b1[3]
            self.nalik = b1[4]

    def oplata_TV(self):
        with open('transactions.txt', 'r' , encoding="UTF8") as read2:
            b2 = re.findall(r'\d+', read2.read())
            self.transactions = b2[0]
            self.user_id = b2[1] 
            self.balance = int(self.balance) - int(self.transactions)

        return self.Return_Bank()

    def oplata_telefon(self):
        with open('transactions.txt', 'r' , encoding="UTF8") as read2:
            b2 = re.findall(r'\d+', read2.read())
            self.transactions = b2[0]
            self.phone_number = b2[1] 
            self.balance = int(self.balance) - int(self.transactions)

        return self.Return_Bank()

    
    def Nalik(self):
        with open('transactions.txt', 'r' , encoding="UTF8") as read2:
            b2 = re.findall(r'\d+', read2.read())
            self.nalik = b2[0]
            self.balance = int(self.balance) - int(self.nalik)

        return self.Return_Bank()

    def Return_Bank(self):
        with open('Bank.txt', 'w', encoding="UTF8") as write:
            write.write(f'User: {self.user}\n')
            write.write(str(f'card_number: {self.card_number}\n'))
            write.write(str(f'user_id: {self.user_id}\n'))
            write.write(str(f'Balance: {self.balance}\n'))
            write.write(str(f'pin code: {self.pin_code}\n'))
            write.write(str(f'phone number: {self.phone_number}\n'))
            write.write(str(f'transactions: {self.transactions}\n'))
            write.write(str(f'Наличных снято, в последний раз: {self.nalik}\n'))
            write.write(str(f'\n'))
