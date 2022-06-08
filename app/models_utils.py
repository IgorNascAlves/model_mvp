import pickle
import sklearn
import pandas as pd

def load_model():
    loaded_model = pickle.load(open('../models/finalized_model.sav', 'rb'))
    return loaded_model

def make_prediction(model, Q, fieldGoalsMade, fieldGoalsAttempted, threePointersMade,
    threePointersAttempted, freeThrowsMade, freeThrowsAttempted, reboundsOffensive,
    reboundsDefensive, assists, steals, blocks, turnovers, foulsPersonal, points):

    dict_dados = {}

    lista_valor = [Q, fieldGoalsMade, fieldGoalsAttempted, threePointersMade,
    threePointersAttempted, freeThrowsMade, freeThrowsAttempted, reboundsOffensive,
    reboundsDefensive, assists, steals, blocks, turnovers, foulsPersonal, points]

    for i in range(len(lista_nomes)):
        dict_dados[lista_nomes[i]] = lista_valor[i]

    df_entrada = pd.DataFrame(data=dict_dados, index=[0])

    if model.predict(df_entrada)[0] == 'L':
        return "Seu time vai perder"
    else:
        return "Seu time vai vencer"

lista_nomes = ['Q', 'fieldGoalsMade', 'fieldGoalsAttempted', 'threePointersMade',
    'threePointersAttempted', 'freeThrowsMade', 'freeThrowsAttempted', 'reboundsOffensive',
    'reboundsDefensive', 'assists', 'steals', 'blocks', 'turnovers', 'foulsPersonal', 'points']