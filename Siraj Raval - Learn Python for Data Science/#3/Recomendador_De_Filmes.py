import numpy as np
from lightfm import LightFM
from fetch_lastfm import fetch_lastfm


data = fetch_lastfm()

model = LightFM(loss='warp')
model.fit(data['matrix'], epochs=30, num_threads=2)

def recomendacoes(model, coo_mtrx, users_ids):

    n_items = coo_mtrx.shape[1]

    for user in users_ids:
        scores = model.predict(user, np.arange(n_items))
        top_scores = np.argsort(-scores)[:3]

        print 'Recomendações para:' % user

        for x in top_scores.tolist():
            for artista, valores in data['artists'].iteritems():
                if int(x) == valores['id']:
                    print '   - %s' % valores['name']

        print '\n' 

user_1 = input('Usuário 1 (0 - %s): ' % data['users'])
user_2 = input('Usuário 2 (0 - %s): ' % data['users'])
user_3 = input('Usuário 3 (0 - %s): ' % data['users'])
print '\n' 

recomendacoes(model, data['matrix'], [user_1, user_2, user_3])