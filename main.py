# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import pandas as pd
import pickle

#!pip install --upgrade speakleash
from speakleash import Speakleash



PROJECTS = ["web_artykuły_blogi_1", "web_artykuły_edukacja_1", "usenet"]

def get_data(ds):
    lst1 = []
    for doc in ds:  
        txt, meta = doc
        meta['text'] = txt
        lst1.append(meta)
    frame = pd.DataFrame(lst1)
    frame['name'] = frame['name'].apply(lambda x: x.split('\\')[-1])
    return frame


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for p in PROJECTS:
        base_dir = os.path.join(os.path.dirname(p))
        replicate_to = os.path.join(base_dir, p)
        sl = Speakleash(replicate_to)
        ds = sl.get(p).ext_data
        df = pd.DataFrame(get_data(ds))
        with open(f"{p}.pkl","wb") as f:
            pickle.dump(df, f)
    

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
