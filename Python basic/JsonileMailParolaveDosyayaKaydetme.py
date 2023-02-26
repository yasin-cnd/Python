import json
import os
class User:
    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email


class UserRepository:
    def __init__(self):
        self.users=[]
        self.isLoggedIn=False
        self.currentUser={}
        
        ##load users from .json file
        
        self.loadUsers()
    
    def loadUsers(self):
        if os.path.exists("users.json"):
            with open("users.json","r",encoding="utf-8") as file:
                users=json.load(file)
                for user in users:
                    user=json.loads(user)   ##liste içindeki username leri aldık
                    newUser=User(username=user["username"],password=user["password"],email=user["email"])
                    self.users.append(newUser)
            print(self.users) ##obje şeklinde geldi
                                     
    def register(self,user=User):
        self.users.append(user)
        self.savetoFile() ##bütün listei dosyaya kaydetti
        print("kullanıcı oluşturuldu")
        
        
    def login(self,username,password):
        for user in self.users:
            if user.username==username and user.password==password :
                self.isLoggedIn=True
                self.currentUser=user
                print("login yapıldı.") ##kullanıcı <varsa> login yapıldı 
                break
    def logout(self):
        self.isLoggedIn=False
        self.currentUser={}
        print("Çıkış yapıldı.")
    def identily(self):
        if self.isLoggedIn:
            print(f"username: {self.currentUser.username}")
        else:
            print("Giriş yapılmadı")
        
    def savetoFile(self):
        list=[]
        
        for user in self.users:
            list.append(json.dumps(user.__dict__)) ##jsonda class yok bu yüzden lilstey cevirdik
        
        
        with open("users.json","w") as file:
            json.dump(list,file)         ## users.json içine kaydettik
    
    
repository=UserRepository()    
    
while True:
    print("menü".center(50,"*"))
    secim=input("1-  Register\n2- Login\n3- Logout\n4- idenity\n5 -Exit\n seçiminiz :")
    if secim=="5":
        break
    else: 
        if secim=="1":
            username=input("username:")   ##register
            password=input("password:") 
            email=input("email:") 
            
            user=User(username=username,password=password,email=email)
            repository.register(user)
            
            
            
        elif secim=="2" :  ##login
            if repository.isLoggedIn:
                print("zaten login oldunuz")
            else:   
                username=input("username :")
                password=input("password :")
            
                repository.login(username,password)
        elif secim=="3":
            repository.logout() ##logout

        elif secim=="4":
            repository.identily() ##display username
        else:
            print("yanlış secim")

    

