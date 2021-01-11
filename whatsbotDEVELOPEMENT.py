## sample code for basic chatbot
# run this on your python compiler
# change the whatsapp number wherever mentioned
# send message to twilio number I sent you today morning 
import random

'''join sandbox by sending "join beneath-highway" '''

from twilio.rest import Client 
account_sid = 'AC265a666606eae125b3fd6dd8b6582d02' 
auth_token  =  'b8d9487229d55173d88ce982213b8a50'
client = Client(account_sid, auth_token) 

def sendtxt(message , person="+917666779269"):      #paste your whatsapp number here
    message = client.messages.create( 
                                  from_='whatsapp:+14155238886',  
                                  body= message,      
                                  to='whatsapp:{}'.format(person) 
                              )
def sendimg(url="https://i0.wp.com/indiacanteen.tastyfix.com/wp-content/uploads/2018/11/1-2.png?fit=600%2C400&ssl=1" , person = "7666779269"):
    message = client.messages.create(
             media_url=[url],
             from_='whatsapp:+14155238886',
             body="It's snacks time!,yummy maggie for you😋😋..!!",
             to='whatsapp:+91{}'.format(person)
         )

def hello():
    return "Hello, World!"

def switch0(arg0="Hi"):
    return switch1("Hi")

def switch1(argument): 
    mydict = {"Hi": 'जी वस्तू मागवायची आहे जस कि जर दूध हवे असेल तर 1 ,बिस्किट्स साठी 3 ,इ. याप्रमाणे आकडे निवडा ..🙂\n1: milk \n2:dal\n3:oilProducts\n4: Soap ',
              "1":"code       company       rate(inRs)\n 1            amul milk            56 \n 2            warna milk          56 \n  3            gokul milk           56 \n  4            nandini milk        54",
               "2":"Code.        Company.          Rate \n 1.             Mug.                  80/kg\n 2.             Masoor.            60/kg\n 3.            Harbhara.          70/kg \n 4.             Toordal.            70/kg \n 5.             Masoordal.       75/kg",
               "3":"Code.         Company.       Price \n  1.               Fortune          130/kg \n 2.               Gemini.          128/kg \n 3.                Safola.          120/kg \n 4.               Star.                120/kg \n 5.                Kirtigold.       115/kg",
               "4":"code       company       rate(inRs) \n 1.         surfexcel soap         10 \n 2         vim soap                  10 \n 3         wheel soap               8 \n 4         tiptop soap               7 \n 5         hamam soap            6",
             "Hi2.0": " to add next item in your cart,make your next choices \n1: milk \n2:dal\n3:oilProducts\n4: Soap ",
             }    
    
    a = "plz give correct input option number.I am still in learning phase."
    return  (mydict.get(argument, a))
    
def switch2(arg3): 
    switcher = {
            "1": "how many litres of milk do you want?", 
            "2": "how many grams or KGs of Dal you want to buy?", 
            "3": "how many Kgs of oil do you need?",
            "4": "how many soaps do you want?",
            }
    return switcher.get(arg3 , "nothing")

def switch3(arg3):
    switchof="select the correct option-- \n 1. add next  \n 2. no more ,place order"
    return switchof
  
def switch4(arg4):
    dictl = {"1":switch1("Hi"),
             "2":"your order is taken by our side",
            }
    return dictl.get(arg4," I don't understand your response plz make it correct")
  
def random_response(arg):
    randomdict = {
        1:"sorry I didn't hear that ",
        2:"please specify your input in correct manner which I can understand",
        3:"plz give the correct input so I can understand.\nTo order new item just send *Hi* here" ,
        4:"Ohh I didn't see that coming make it more specific in a way I can understand",
        5:"you can simply state *Hi* for making new order"
    }
    return randomdict[arg]
    
class sub1():
    
    pot1 = {"+917666779269":[]}          #add your phone number
    pot  = {"+917666779269":[]}          #add your phone number
    
    def __init__(self,cust):
        self.cust=cust
        
    def add_and_show(self,arg):        
        if arg in ["Hi","hi"]:
            self.pot[self.cust] = ["hi"]
            return  switch1("Hi")
        else:
            if arg in ["1","2","3","4","5"]:
                self.pot[self.cust].append(arg)
                pot = self.pot[self.cust]
                if len(pot) == 2:
                    if pot[-1] in "1234":
                        return switch1(pot[-1])
                    else:
                        return  "plz give the correct input sdo I can understand." 
                elif len(pot) == 3:
                    if pot[-1] in "12345":
                        return switch2(pot[-2])
                    else:
                        return  "plz give the correct input sdo I can understand." 
                elif len(pot) == 4:
                    if len(pot)==4:
                        return switch3(pot[-1])
                elif len(pot)==5:
                    if pot[-1]=="1":
                        self.pot1[self.cust].append(self.pot[self.cust])
                        self.pot[self.cust] = ["hi"]
                        return switch1("Hi2.0")
                    elif pot[-1] == "2":
                        self.pot1[self.cust].append(self.pot[self.cust])
                        self.pot[self.cust] = []
                        return "your order is taken by our side thank you.."
                    else:
                        return  "plz give the correct input sdo I can understand." 
                else:
                    self.pot[self.cust].pop(-1)
                    return  "plz give the correct input so I can understand.\nTo order new item just send *Hi* here" 

            else:# type(arg) == str:
                self.pot[self.cust].append(arg)
                pot = self.pot[self.cust]
                if len(pot)==4:
                    return switch3(pot[-1])
                else:
                    self.pot[self.cust].pop(-1)
                    return  random_response(random.randint(1,5))
            
def sms_reply():
    msg = input()
    rem = "+917666779269"                   #paste your whatsapp number here
    am = msg
    api = sub1(rem).add_and_show(am)
    print("sublist",sub1(rem).pot)
    print("mainlist",sub1(rem).pot1)
    return sendtxt( api,rem)
 
    
for i in range(1,10):                       #run this and give input here but you will see reply on your whatsapp 
    sms_reply()