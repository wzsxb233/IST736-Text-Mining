import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import re
# sklearn package.
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
# nltk package.
import nltk
from nltk.classify import SklearnClassifier
