from tqdm import tqdm
from time import sleep
pbar = tqdm(total=100)
for i in range(10):
    pbar.update(10)
    sleep(2)
pbar.close()