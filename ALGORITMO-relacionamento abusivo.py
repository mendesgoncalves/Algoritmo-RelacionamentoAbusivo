from time import sleep
def opcoes():
    print('=' * 50)
    print('\033[1:36m  --> frequentemente \n \033[1:34m  --> as vezes \n \033[1:35m  --> raramente \n \033[1:33m  --> nunca\033[m')
    print('=' * 50)
def  informacoes():
    print('='*100)
    print('\t\t\033[1:36m Olá! Este algoritmo te ajuda a saber se você se encontra em um relacionamento abusivo \033[m')
    print('='*100)
    print('\033[31mSerão 10 perguntas no total. Para responder as questões, utilize as opcoes.\033[m \n \033[1:36m  --> frequentemente \n \033[1:34m  --> as vezes \n \033[1:35m  --> raramente \n \033[1:33m  --> nunca\033[m')
    sleep(2)
    print('Após identificar & digitar a opcao que corresponde à sua resposta, precione ENTER. Vamos começar!')
def perguntas():
    lista=['Pergunta 1: O ciúme do seu parceiro alguma vez virou argumento para controlar\nsuas decisões, adentrar sua privacidade e/ou já levou a ofensas? '
           ,'Pergunta 2: "Por que eu te amo demais" ou "é para o seu bem" e\ou similares já foram utilizados\npelo seu parceiro para indicar roupas que você devia vestir, atividades que devia fazer, etc? '
           ,'Pergunta 3: Seu parceiro já teve acesso a senhas pessoais, mexeu no seu celular ou leu mensagens suas \nsem o seu conhecimento?(Ou sob a justificativa de que "quem ama não tem nada a esconder"?'
           ,'Pergunta 4: Você já se afastou de algumas amizades para evitar conflito com seu parceiro? Ou "fulano é má influência" ou \n"ciclano dé encima de você" são frases que você costuma ouvir?'
           ,'Pergunta 5: Você já percebeu seu parceiro utilizando frases de chantagem para conseguir o que quer? \n"Vou ficar doente assim" ou "vou me matar" ou algo específico que ele saiba que mexe com você?'
           ,'Pergunta 6: "Críticas construtivas" são cada vez mais comuns e um pesadas?'
           ,'Pergunta 7: Se você diz que ficou chateada com alguma coisa que ele falou ou fez, costuma ouvir que é\n"besteira sua" ou "drama" e derivados?'
           ,'Pergunta 8: Seu parceiro já insistiu em uma relação sexual mesmo após você ter dito não? Ou já tentou \niniciar uma relação sexual com você dormindo\desacordada\etc?'
           ,'Pergunta 9: Seu parceiro tem acesso ao seu dinheiro? Se sim, com que frequência ele tenta controlar\nos seus gastos ou fazê-la se sentir mal com suas decisões financeiras?'
           ,'Pergunta 10: Tirar dinheiro, sumir com os filhos, agressões verbais ou outros tipos de ameaça já foram feitas a você?']
    return lista
def programa():
    lista=perguntas()
    aux=0
    contador=0
    while aux!=9:
        for i in range(0,len(lista)):
            opcoes()
            resposta=str(input(lista[i])).replace(' ','')
            if resposta == 'frequente':
                contador += 2
            elif resposta == 'asvezes':
                contador += 1
            elif resposta == 'raramente':
                contador += 0.5
            elif resposta == 'nunca':
                contador += 0
            else:
                print('\33[1:33:41m Ops! O opcao digitada não corresponde à uma resposta. Tente novamente na próxima. \33[m')
                i-=1
        aux=9
    if contador > 11:
        print('Seu relacionamento é abusivo! Peça ajuda!')
    elif contador>7 and contador<=10:
        print('Seu relacionamento tem MUITOS momentos abusivos. Peça ajuda!')
    elif contador>4 and contador<=6:
        print('Seu relacionamento tem alguns momentos abusivos. Fique atenta!')
    else:
        print('Aparentemente não há muitos sinais abusivos. Mantenha-se alerta!')

informacoes()
programa(
