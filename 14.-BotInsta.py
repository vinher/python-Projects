from instabot import Bot

devbot = Bot()
devbot.login(username="",password="")

#devbot.follow('Cuenta a seguir') 

devbot.send_message('Mensaje a enviar ',['Usuario 1','Usuario 2'])
devbot.follow_followers('Cuenta de la cual queremos seguir todos los seguidores de el')
