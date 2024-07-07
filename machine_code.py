import serial                    
import pyautogui 
#Serial imported for Serial communication 
Arduino_Serial = serial.Serial('com4',9600) #Create Serial port object called 
arduinoSerialData 
while 1: 
incoming = str (Arduino_Serial.readline()) #read the serial data and print it 
as line 
print (incoming) 
if 'Play/Pause' in incoming: 
pyautogui.typewrite(['space'], 0.2) 
if 'Rewind' in incoming: 
pyautogui.hotkey('ctrl', 'left')   
if 'Forward' in incoming: 
pyautogui.hotkey('ctrl', 'right')  
if 'Vup' in incoming: 
12 
pyautogui.hotkey('ctrl', 'down') 
if 'Vdown' in incoming: 
pyautogui.hotkey('ctrl', 'up') 
if 'next' in incoming: 
pyautogui.hotkey('ctrl', 'x') 
incoming = ""; 
