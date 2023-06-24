import os

# Custom Grid Search

n_estimators = [110, 100, 150, 200, 210]
max_depth = [20,25,15,10,5]

for n in n_estimators:
    for m in max_depth:
        print(f"Training with {m} depth and {n} estimators")
        os.system(f"python basic_ml_model.py -n {n} -m {m}")