from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Y0Y0.9696')

conversa = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo', 'Você gosta de programar?', 'Sim, eu programo em Python']

bot.set_trainer(ListTrainer)
bot.train(conversa)

while True:
    pergunta = input("Usuário: ")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('y0y0.9696: ', resposta)
    else:
        print('y0y0.9696: Ainda não sei responder esta pergunta')