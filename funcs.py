from keras.applications.mobilenet import MobileNet
from keras.preprocessing import image
from keras.applications.mobilenet import preprocess_input, decode_predictions
import numpy as np
import matplotlib.pyplot as plt
import os
import id_to_name
import pickle



def mnetv2_input_from_image(img):
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    return preprocess_input(x)

def create_in(path_folders):
    model = MobileNet(weights='imagenet')

    img_list = []

    folders = os.listdir(path_folders)
    # print(folders)
    for f in folders:
        dire = os.listdir(path_folders + f)
        for a in dire:
            caminho = '{}{}/{}'.format(path_folders, f,a)
            img_list.append(caminho)

    list_predicted = []
    for index, im in enumerate(img_list):

        img = image.load_img(im, target_size=(224, 224))
        x = mnetv2_input_from_image(img)
        
        preds = model.predict(x)
        ids = (np.fliplr(np.argsort(preds))[0][:5]).tolist()
        probs = [preds[0][i] for i in ids]
        list_predicted.append((im, ids, probs))

    inv = dict()
    for x in id_to_name.dic.values():
        inv[x] =  []

    for i, img in enumerate(list_predicted):
        for j, id_ in enumerate(list_predicted[i][1]):
            chave = id_to_name.dic[id_]
            inv[chave].append((img[0], list_predicted[i][2][j]))

    invs = dict()
    for v in inv:
        invs[v] = sorted(inv[v], key=lambda t:t[1], reverse=True)

    pickle.dump(invs, open("dictimgs.p", "wb"))

def part(diciinv):
    invsp = dict()
    for v in diciinv:
        vp = v.split(', ')
        for t in vp:
            invsp[t] = sorted(diciinv[v], key=lambda t:t[1], reverse=True)

    pickle.dump(invsp, open("dictimgspartial.p", "wb"))

def show_5(dici, termo):
    sorted_most5 = dici[termo][:5]

    if len(sorted_most5) > 0:
        plt.figure(figsize=(20,5))
        i = 1
        for img in sorted_most5:
            plt.subplot(2,3,i)
            plt.axis('off')
            plt.title('{}, conf: {}'.format(img[0], '%.3f'%(img[1])))
            img_path = img[0]
            im = image.load_img(img_path)
            plt.imshow(im)
            i += 1
        plt.show()   
    else:
        print('Não exitem imagens com esse termo :(')