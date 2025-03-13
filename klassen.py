

class konto:
    
    def __init__(self, name, start_betrag):
        #super(konto, self).__init__()
        self.konto_inhaber = name
        self.__kontostand = start_betrag

    def einzahlen(self, betrag, inhaber):
        self.__kontostand += betrag
        print(f"Herr {inhaber} Sie haben {betrag} Euro bezahlt. Der neue Kontostand ist {self.__kontostand} Euro ")
        
        

    def get_kontostand(self):
        return self.__kontostand

    def abheben(self, betrag, inhaber):
        if betrag > self.__kontostand:
            raise NotEnoufBalance
        else: 
            self.__kontostand -= betrag
            print(f"Herr {inhaber} Sie haben {betrag} Euro abgehoben."
                f"Der neue Kontostand ist {self.__kontostand} Euro \n")
            

            
        
        
class NegativeNumberError(Exception):
    def __init__(self, message = "Negative Zahlen sind nicht erlaubt! "):
        self.message = message
        super().__init__(self.message)
def check_positive(n):
    if n < 0:
        raise NegativeNumberError
    return n 
class NotEnoufBalance(Exception):
    def __init__(self, message = "Sie haben nicht genug Guthaben! "):
        self.message = message
        super().__init__(self.message)

    


            
print("\n\n Sie möchten für sich eine Bankkonto eröffne? Dann Bitte Folgen Sie die folgenden Anweisungen\n")


while True:
    konto_inhaber = input("Geben Sie Ihren Namen für Ihr Konto ein \n")
    if not konto_inhaber.isnumeric():
         print(f"Herzlich Willkommen Herr {konto_inhaber} zur Testbank! \n\n")
         break
    else: print("Bitte Ihren Namen Richtig eingeben!  ")
    


while True:
    
    try:
    
        start_betrag = int(input("Geben Sie den Betrag, die Sie als Startguthaben einzahlen möchten \n"))
        
        check_positive(start_betrag)
        break
        
    except ValueError:
            print("Bitte eine Zal einegeben!\n ")
                
    except NegativeNumberError as e:
            print("Fehler: ", e)


test_konto = konto(konto_inhaber, start_betrag)
    

print("jetzt wird der Kontostand geprüft\n")
print("Ihre Start Guthaben beträgt: " ,test_konto.get_kontostand())
print("\n")
print("jetzt wird Einzahlung tätigt:\n")

while True:
    
    try:
    
        einzahlung = int(input("Geben Sie den Betrag, die Sie jetzt einzahlen möcheten\n"))
        
        check_positive(einzahlung)
        break
        
    except ValueError:
            print("Bitte eine Zal einegeben!\n ")
                
    except NegativeNumberError as e:
            print("Fehler: ", e)

test_konto.einzahlen(einzahlung, konto_inhaber)
print("\n")
print("jetzt wird eine Abhebung stattfinden\n")

while True:
    
    try:
        abheben = int(input("Wie viel möchten Sie denn jetzt abheben?\n"))
        
        check_positive(abheben)
        test_konto.abheben(abheben, konto_inhaber)
        break

        
    except ValueError:
            print("Bitte eine Zal einegeben!\n ")
                
    except NegativeNumberError as e:
            print("Fehler: ", e)
    except NotEnoufBalance as e:
        print("Feler: ", e)


