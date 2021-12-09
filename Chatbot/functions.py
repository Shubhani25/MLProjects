def create_bot(name):
    from chatterbot import ChatBot
    Bot=ChatBot(name=name,
                read_only=False,
                logic_adapters=['chatterbot.logic.BestMatch'],
                storage_adapter='chatterbot.storage.SQLStorageAdapter')
    return Bot

def train_all_data(Bot):
    from chatterbot.trainers import ChatterBotCorpusTrainer
    corpus_trainer=ChatterBotCorpusTrainer(Bot)
    corpus_trainer.train("chatterbot.corpus.english")

def custom_train(Bot, conversation):
    from chatterbot.trainer import ListTrainer
    trainer = ListTrainer(Bot)
    trainer.train(conversation)

def start_chatbot(Bot):
    print('\033c')
    print("Hello, I am Mike. How can i help you?")
    bye_list = ["bye Mike","bye","good bye"]

    while (True):
        user_input=input("me: ")
        if user_input.lower() in bye_list:
            print("Mike: Good bye and have a blessed day!")
            break

        response = Bot.get_response(user_input)
        print("Mike:", respond)
