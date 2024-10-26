# importation des library
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
from sklearn.metrics import classification_report
from sklearn.preprocessing import MinMaxScaler

# Lecture la table des données
X = pd.read_csv('full_data.csv')

# Pour l'affichage total du dataframe
pd.set_option('display.max_columns', None)

# Extraire la colonne cible
y = X['player_status']
X = X.drop('player_status',axis=1)

# remplacer les valeurs pour la prediction des joueurs convoqués seulement
y.replace({'line-up': 'called-up'}, inplace=True)

# Mélangez les deux DataFrames en utilisant la même graine aléatoires
random_seed = 47
y = y.sample(frac=1, random_state=random_seed)
X = X.sample(frac=1, random_state=random_seed)

# calculer la moyenne de saves par matche
X['goals_conceded'] = X['goals_conceded'] + X['saves']
X['saves'] = np.where(X['goals_conceded'] != 0, X['saves'] / X['goals_conceded'] , 0)

# éliminer les valeurs non nessaicaire et les valeurs qu'on a choisis d'éliminer aprés future engineering
X= X.drop('minute_per_game',axis=1)
X = X.drop('tackles_per_game',axis=1)
X = X.drop(X.columns[0],axis=1)
X = X.drop('player_name_sofascore',axis=1)
X = X.drop('player_name_transfer_market',axis=1)
X = X.drop('player_team',axis=1)
X = X.drop('player_league',axis=1)
X = X.drop('goals_conceded',axis=1)
X = X.drop('pourcentage passes', axis=1)
X = X.drop('dribbled_per_game', axis=1)
X = X.drop('national_team', axis=1)

# remplacer les valeurs nulls de la colonne 'player_market_value' par 0
X['player_market_value'] = X['player_market_value'].fillna(0)

# remplacer les valeurs nulls de la colonne 'league_ranking' par le median
X['league_ranking'] = X['league_ranking'].fillna(X['league_ranking'].mean())

# éliminer une colonne nul du data set
X = X.dropna()
y = y.drop(915)

# encoder la colunm 'player_position' et le cible en utilisant labelEncoder() et getdummies()
label_encoder = LabelEncoder()
X = pd.get_dummies(X, columns=['player_position'], prefix='player_position')
y = label_encoder.fit_transform(y)

# utiliser minmaxscaler pour transformer les valeurs de les données
scaler = MinMaxScaler()
X = scaler.fit_transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Logistic Regression classifier
logreg_classifier = LogisticRegression(max_iter=8000,C=10.0)

# Train the classifier on the training set
logreg_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = logreg_classifier.predict(X_test)

# Create a confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Display the confusion matrix
print("Confusion Matrix:")
print(cm)

# Create a heatmap for visualization
plt.figure(figsize=(4, 3))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Evaluate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Calculate precision, recall, and F1-score
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)

# Print the results
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)
print("Accuracy:", accuracy)









