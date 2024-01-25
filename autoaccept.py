from lcu_driver import Connector
import os
import time

connector = Connector()

@connector.ready
async def connect(connection):
    print('API está pronta para ser utilizada')
    player = await connection.request('get', '/lol-summoner/v1/current-summoner')
    time.sleep(2)
    os.system('cls')
    print('Bem vindo ' + (await player.json())['displayName']+'!')
    gamephase = await connection.request('get', '/lol-gameflow/v1/gameflow-phase')
    currentphase = await gamephase.json()
    print('Irei aceitar a partida automáticamente para você.')

    while True:
        gamephase = await connection.request('get', '/lol-gameflow/v1/gameflow-phase')
        currentphase = await gamephase.json()
        if currentphase == 'Lobby' or currentphase == 'Matchmaking':
            while True:
                gamephase = await connection.request('get', '/lol-gameflow/v1/gameflow-phase')
                currentphase = await gamephase.json()     
#aceitar automaticamente
                if currentphase == 'ReadyCheck':
                    await connection.request('post', '/lol-matchmaking/v1/ready-check/accept')
                    time.sleep(5)
                    print('Bora!')

async def disconnect():
    print('O client foi fechado')
    await connector.stop()

connector.start()
