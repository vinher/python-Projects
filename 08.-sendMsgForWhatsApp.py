import pyautogui as pg, webbrowser as web, time as tm

#Consumimos la API de whatsapp
web.open("https://web.whatsapp.com/send?phone=+52 Numero de telefono")
tm.sleep(8)#Tiempo de espera para que cargue la pagina.
for i in range(10):#Numero de mensajes que se enviaran
    pg.write("Mensaje Prueba")#mensaje a enviar con el metodo write el cual escribira lo que le indiquemos
    pg.press('enter')# Al terminar de escribir el mensaje indicamos que presione enter
