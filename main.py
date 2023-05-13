import tzevaadom
import sys
import datetime
from windows_toasts import WindowsToaster, ToastImageAndText1, ToastDisplayImage

toaster = WindowsToaster('RED ALERT!')

#Take current time

currentime= datetime.datetime.now()

###this command will run when the the library tzevaadom respond with information

#Hebrew
def handlerhe(List_Alerts):
  for alert in List_Alerts:
    Cityhe = alert['name']
    City=alert['name_en']
    Region = alert['zone_en']
    print("New Alert "+ City +" Region: " + Region + "at " + currentime.strftime("%Y-%m-%d %H:%M:%S"))
    newToast = ToastImageAndText1()
    newToast.AddImage(ToastDisplayImage.fromPath('siren.png'))
    newToast.SetBody("צבע אדום!","ב" + Cityhe + " " + currentime.strftime("%Y-%m-%d %H:%M:%S"))
    toaster.show_toast(newToast)

#English
def handler(List_Alerts):
  for alert in List_Alerts:
    City=alert['name_en']
    Region = alert['zone_en']
    print("New Alert "+ City +" Region: " + Region + "at " + currentime.strftime("%Y-%m-%d %H:%M:%S"))
    newToast = ToastImageAndText1()
    newToast.AddImage(ToastDisplayImage.fromPath('siren.png'))
    newToast.SetBody("RED ALERT!","At " + City + " " + currentime.strftime("%Y-%m-%d %H:%M:%S"))
    toaster.show_toast(newToast)

#Get user input if they want Hebrew or English notification
heoren = input("Please choose HE(עברית) or EN(אנגלית):")

#if you want to use specific cities please change tzevaadom.alerts_listener(handlerhe) to tzevaadom.alerts_listener(handlerhe,alerts_only_for_cities=["עיר א","עיר ב"]) same goes for the english version NOTE THE CITY MUST BE WRITTEN IN HEBREW!
if(heoren == "HE"):
  print("You chose Hebrew notifications!")
  tzevaadom.alerts_listener(handlerhe)
elif(heoren == "EN"):
  print("You chose English notifications!")
  tzevaadom.alerts_listener(handler)
else:
  print("Wrong input! please try again.")
  exit()
