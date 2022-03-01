import numpy as np
import tensorflow as tf
import json
import random

from tensorflow import keras
from typing import List, Tuple
import os.path


def save_image(table:List[int], val: int) -> None:
    with open("back/data/" + str(val) + ".data",'a+') as f:
        f.write(str(table))
        f.write('\n')
    return

def train_from_files() -> None :
    all_nums = []
    indexs = []

    shuffled_nums = []
    shuffled_index = []

    #Lecture des fichiers
    for i in range (10):
            with open("back/data/" + str(i) + ".data",'r') as f:
                lines = f.readlines()
                for l in lines:
                    temp = list(map(int, l[1:-2].split(',')))
                    all_nums.append( temp )
                    indexs.append(i)

    #On "mélange" les images            
    random.seed()
    while len(all_nums) > 0:
        index = random.randint(0, len(all_nums) - 1)
        print(index)
        shuffled_nums.append(all_nums[index])
        tmp = np.array([0,0,0,0,0,0,0,0,0,0])
        tmp[indexs[index]] = 1
        shuffled_index.append( tmp )
        del all_nums[index]
        del indexs[index]

    #On entraine avec toute la "batch"
    model = get_model()
    model.fit(np.array(shuffled_nums), np.array(shuffled_index), batch_size=len(shuffled_nums), epochs=2)
    print("Finished training!")
    save("model.h5", model)
    return


def create_model() -> keras.Sequential:
    model = keras.Sequential()
    #inputs
    model.add(keras.layers.Input(shape=(20*20)))
    #"inside" layer
    model.add(tf.keras.layers.Dense(100, activation='relu'))

    #outputs
    #10 possible numbers with a total probability of 1
    model.add(tf.keras.layers.Dense(10, activation='softmax'))

    model.compile(optimizer='Adam', loss="mse")

    model.summary()

    return model

def load(fp: str) -> keras.Model:
    return keras.models.load_model(fp)

def save(fp: str, model: keras.Model) -> None:
    model.save(fp)
    return

def get_model():
    if not os.path.exists("model.h5"):
        model = create_model()
    else:
        model = load("model.h5")
    return model

def train_model(val: int, tab: List[int]) -> None:
    model = get_model()

    expected_output = np.array([0,0,0,0,0,0,0,0,0,0])
    expected_output[val] = 1

    model.fit(np.array([tab]), np.array([expected_output]), epochs=1, batch_size=1)
    save("model.h5", model)
    save_image(tab, val)
    return 

#Guessing table
def guess(tab:List[int]) -> np.ndarray:
    model = get_model()
    
    val = model.predict(np.array([tab]))
    print(type(val))
    return val
