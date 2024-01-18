import datetime as dt

class ValidateName():

    def ValidateNameDef():


        last2_negetive_check = ["KA","MA","NA","RA","YA","LA","SA","VA","DA"]
        #Valast2_negetive_check = ["K","M","N","Y","R","L","S","V","D"]


        Alphabet_Dict = {"a":"1","b":"2","c":"2","d":"4","e":"5","f":"6",
        "g":"3","h":"5","i":"1","j":"1","k":"2","l":"3",
        "m":"4","n":"5","o":"7","p":"8","q":"9","r":"2",
        "s":"3","t":"4","u":"6","v":"6","w":"6","x":"5","y":"1","z":"6" }


        YesToContinue = "Y"
        while YesToContinue == "Y":
            suggested_name  = input("Please insert a name : ")
            if suggested_name[-2:].casefold() in map(str.casefold,last2_negetive_check):
                print("Suggest Enter another name...")
            else:
                suggested_name_len = len(suggested_name)
                n = 0
                for i in range(suggested_name_len):
                    char_lower = suggested_name[i].lower()
                    if char_lower in Alphabet_Dict.keys():
                        x = Alphabet_Dict.get(char_lower)
                        n = int(x) + n
                print('Count for ' + suggested_name + ' is :' + str(n))
                YesToContinue = input("Do you want to continue (Enter Y or N) : ")


ValidateName.ValidateNameDef() 
