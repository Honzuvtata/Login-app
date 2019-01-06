class Data_storage:

    def __init__(self): #initialization of data storage and array users
        self.users = []
        self.data_storage_user_id = 0

    def add_user(self, name, password, age, email): #initialize User and save user to array data_storage, users
        new_user = User(self.data_storage_user_id, name, password, age, email)
        self.users.append(new_user)
        self.show_user_info_by_id(self.data_storage_user_id)
        self.data_storage_user_id += 1

    def show_user_info_by_id(self, id): # input - users ID, prints users info
        print("ID:       ", self.users[id].id)
        print("NAME:     ", self.users[id].name)
        print("PASSWORD: ", self.users[id].password)
        print("AGE:      ", self.users[id].age)
        print("EMAIL:    ", self.users[id].email)

    def all_users_info(self): # show info abouth all users
        i = 0
        for item in self.users:
            self.show_user_info_by_id(i)
            print("------------------------------")
            i += 1
        controller.uvodni_okno()

# po zavolani zalozi uzivatele
class User:

    def __init__(self, id, name, password, age, email):
        self.id = id
        self.name = name
        self.password = password
        self.age = age
        self.email = email

    def user_info(self): #vyprintuje info o uzivateli
        print("ID {0}, name: {1}, password: {2}, age: {3}, mail {4}".format(self.id, self.name, self.password, self.age, self.email))

class Controller: #aplikace pro prihlasovani a zakladani uzivatelu

    def welcome(self):
        print("Welcome")

    def uvodni_okno(self): #vyber funkce kterou chces provest
        user_input = input("--------------- What do you want to do? ------------ \n"
                  "a) login \n"
                  "b) create new accoutn (sign up) \n"
                  "c) user info \n"
                  ": ")
        user_input = user_input.lower()
        print(user_input)
        if user_input == "a":
            print("prihlasovaci okno")
            self.login()
        elif user_input == "b":
            print("zalozit ucet")
            self.new_account()
        elif user_input == "c":
            print("Podivej se na info o uzivateli")
            self.users_info_menu()
        else:
            print("Nevalidni command.")
            self.uvodni_okno()

    def login(self): #napis jmeno a heslo a prihlasis se
        login_correct = False
        password_correct = False
        login_name = input("Enter login name: ")
        login_password = input("Enter login passwort: ")
        id = 0
        for item in data_storage.users:
            if login_name == data_storage.users[id].name:
                login_correct = True
                print("login name OK")
            else:
                print("Login name incorrect.")
            if login_password == data_storage.users[id].password:
                password_correct = True
                print("Password is OK")
            else:
                print("Login password incorrect")

        print(login_correct, password_correct)
        if login_correct == True and password_correct == True:
            print("Login and password correct. You are loged in!")
        self.uvodni_okno()

    def users_info_menu(self): #shows menu. Input - choose where to go from menu
        users_input = input("a show all users info \n"
                      "b show users info by ID \n"
                      ": ")
        users_input = users_input.lower()
        if users_input == "a":
            data_storage.all_users_info()
        elif users_input == "b":
            users_input_ID = input("Choose users IN in range from {} to {}: ".format(0, (len(data_storage.users) - 1)))
            data_storage.show_user_info_by_id(int(users_input_ID))



    def new_account(self): #vytvorit novy account (jmeno, heslo, age)
        username = self.create_username()
        password = self.create_password()
        age = self.create_age()
        email = self.create_mail()
        print("Gratuluji! Zalozil jsi uzivatele se jmenem: '{}' a s heslem: '{}'".format(username, password))
        username = data_storage.add_user(username, password, age, email)
        controller.uvodni_okno()

    def create_username(selfself): #zadej jmeno. Zkontroluje se jeho validita. Vrati validni username
        username_valid = False
        while username_valid == False:
            username = input("Enter username: ")
            if len(username) < 4:
                print("Username must be longer than 4 charts")
            else:
                print("you created new username {}".format(username))
                username_valid == True
                return username

    def create_password(self): #zadej heslo, zkontroluje se jeho validita. Vrati validni heslo
        password_valid = False
        while password_valid == False:
            password = input("Zadejte nove heslo")
            password_contains_number = self.contain_number(password)
            if password_contains_number == False:
                print("Heslo musi obsahovat cislo!!")
            elif len(password) < 5:
                print("Heslo je prilis kratke")
            elif password == "12345":
                print("helos nesmí být 12345")
            else:
                print("vytvorili jste nove heslo {}".format(password))
                password_valid = True
        return password

    def create_age(self):
        name = 0
        name = input("Enter your age: ")
        return name

    def create_mail(self):
        email = 0
        email = input("Enter your email: ")
        return email

    def contain_number(self, word): #zkontroluje jestli ve stringu je cislo. Pokud ano vrati True, pokud ne vrati False
        number_in_word = False
        numbers = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        for char in word:
            for num in numbers:
                if char == num:
                    number_in_word = True
        print("Obsahuje slovo cislo??: {}".format(number_in_word))
        return number_in_word

#####testovani zalozeni usera
#user1 = User("Honza", 1234)
#user1.user_info()


data_storage = Data_storage()
data_storage.add_user("Honza", "123456", 20, "svehl.jan@gmail.com")
data_storage.add_user("Honza", "123456", 25, "svehl.jan@gmail.com")
data_storage.add_user("Honza", "123456", 22, "svehl.jan@gmail.com")
data_storage.add_user("Honza", "123456", 23, "svehl.jan@gmail.com")



controller = Controller()
controller.welcome()
controller.uvodni_okno()