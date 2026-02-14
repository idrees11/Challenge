import pandas as pd
from sklearn . metrics import f1_score
import sys
#update to include the automated leaderboard.
# Usage : python scoring_script .py submissions / file .csv

submission_file = sys . argv [1]
truth_file = sys.argv[2]

#Load submission
submission = pd.read_csv( submission_file )

12 # Load ground truth ( hidden )
truth = pd.read_csv(truth_file)
# Compute F1 score
score = f1_score(truth["cell_type"], submission["cell_type"], average="macro")
print(f"SCORE={score:.4f}")