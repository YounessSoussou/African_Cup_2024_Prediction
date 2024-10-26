import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import accuracy_score, classification_report

pd.set_option('display.max_columns', None)


# lecture du table du données
X = pd.read_csv('full_data_africa.csv')

# éxtraire la cible
y = X['result']
X = X.drop('result',axis=1)

# calcule de la colonne differance entre somme buts marquées lors des 5 dernier match
X['rolling_sum_away_goals'] = X.groupby('AwayTeam')['AwayTeamGoals'].rolling(5, min_periods=1).sum().reset_index(level=0, drop=True)
X['rolling_sum_home_goals'] = X.groupby('HomeTeam')['HomeTeamGoals'].rolling(5, min_periods=1).sum().reset_index(level=0, drop=True)
X['diffrance_goals'] = X['rolling_sum_home_goals'] - X['rolling_sum_away_goals']
X = X.drop('rolling_sum_away_goals',axis=1)
X = X.drop('rolling_sum_home_goals',axis=1)

# calcule de la colonne differance entre somme buts subis lors des 5 dernier matches
X['rolling_sum_away_goals_subis'] = X.groupby('AwayTeam')['HomeTeamGoals'].rolling(5, min_periods=1).sum().reset_index(level=0, drop=True)
X['rolling_sum_home_goals_subis'] = X.groupby('HomeTeam')['AwayTeamGoals'].rolling(5, min_periods=1).sum().reset_index(level=0, drop=True)
X['diffrance_goals_subis'] = X['rolling_sum_away_goals_subis'] - X['rolling_sum_home_goals_subis']
X = X.drop('rolling_sum_home_goals_subis',axis=1)
X = X.drop('rolling_sum_away_goals_subis',axis=1)

#calcule de la colonne differance entre les gains dans les dernier 5 matches
X['diffrance_win'] = X['team_win_home'] - X['team_win_away']
X = X.drop('team_win_home',axis=1)
X = X.drop('team_win_away',axis=1)

# éliminer les valeurs non nessaicaire et les valeurs qu'on a choisis d'éliminer aprés future engineering
X = X.drop('rank_home',axis=1)
X = X.drop('rank_away',axis=1)
X = X.drop('Year',axis=1)
X = X.drop('HomeTeam',axis=1)
X = X.drop('AwayTeam',axis=1)
X = X.drop('HomeTeamGoals',axis=1)
X = X.drop('AwayTeamGoals',axis=1)
X = X.drop('Stage',axis=1)
X = X.drop(X.columns[0],axis=1)
X = X.drop(X.columns[0],axis=1)

# Mélangez les deux DataFrames en utilisant la même graine aléatoires
random_seed = 49
y = y.sample(frac=1, random_state=random_seed)
X = X.sample(frac=1, random_state=random_seed)

# remplacer les valeurs nulles par 0
X = X.fillna(0)
# encoder les valeurs dans la dataframe
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Fit and transform the DataFrame
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Gradient Boosting classifier
gb_classifier = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42)

# Train the classifier on the training set
gb_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = gb_classifier.predict(X_test)

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
print(f'Gradient Boosting Accuracy: {accuracy}')
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Calculate precision, recall, and F1-score
precision = precision_score(y_test, y_pred,average='macro')
recall = recall_score(y_test, y_pred,average='macro')
f1 = f1_score(y_test, y_pred,average='macro')

# Print the results
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)
print("Accuracy:", accuracy)








