
from sklearn.preprocessing import scale, normalize
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.cross_validation import StratifiedKFold
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC, SVC
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
import pandas as pd
from sklearn.externals import joblib
from sklearn.ensemble import GradientBoostingClassifier
from xgboost import XGBClassifier
import numpy as np


from sklearn.metrics import classification_report, accuracy_score, make_scorer
# Variables for average classification report
originalclass = []
predictedclass = []

class ModelEvaluation:


    def __init__(self, X, y, feature_name):
        '''
        :param X: training features
        :param y: categories
        '''

        # Scale and normalize training features

        #self.X = scale(X)
        #self.X = normalize(X, norm='l2')
        self.X = X
        self.y = y
        self.feature_name = feature_name

    def classification_report_with_accuracy_score(self, y_true, y_pred):

        originalclass.extend(y_true)
        predictedclass.extend(y_pred)
        return accuracy_score(y_true, y_pred)  # return accuracy score


    def run_evaluation(self, name='default'):

        with open('evaluation/performance_report_final'+ name +'.md', 'a') as f:

            f.write('------' + self.feature_name + '--------')
            f.write('\n')

            names = ["Nearest Neighbors", "Linear SVM", "RBF SVM", "Linear SVM (squared loss)",  "Logistic Regression",
                     "Decision Tree", "Random Forest", "Neural Net", "Naive Bayes", "Gradient Boost"]


            models = [
                KNeighborsClassifier(n_neighbors=5, weights='distance'),
                SVC(kernel="linear", C=0.025),
                SVC(gamma=2, C=1),
                LinearSVC(random_state=42, C= 0.1, dual= True, loss='squared_hinge', penalty='l2', tol=0.0001),
                LogisticRegression(random_state=42, solver='newton-cg'),
                #GaussianProcessClassifier(1.0 * RBF(1.0), n_jobs= -1, random_state=42, warm_start=True, multi_class="one_vs_rest"),
                #GaussianProcessClassifier(1.0 * RBF(1.0), n_jobs=-1),
                DecisionTreeClassifier(max_depth=7, random_state=42, criterion='gini', min_samples_leaf=2, min_samples_split=12),
                RandomForestClassifier(max_depth=5, n_estimators=10),
                MLPClassifier(alpha=1),
                #AdaBoostClassifier(),
                GaussianNB(),
                #XGBClassifier(random_state=42, learning_rate= 0.01, n_estimators= 100, subsample=0.7500000000000001),
                GradientBoostingClassifier(learning_rate=0.01, max_depth=10, max_features=0.35000000000000003,
                                           min_samples_leaf=10, min_samples_split=6, n_estimators=100,
                                           subsample=0.7500000000000001)

                # QuadraticDiscriminantAnalysis()
                 ]


            #kf = 10
            kf = StratifiedKFold(self.y, n_folds=10, shuffle=True, random_state=42)

            entries = []
            for name, model in zip(names, models):
                scores = cross_val_score(model, self.X, self.y, scoring=make_scorer(self.classification_report_with_accuracy_score), cv=kf, verbose=1, n_jobs=-1)
                # Average values in classification report for all folds in a K-fold Cross-validation
                print(name)
                # f.write(name)
                # f.write(classification_report(originalclass, predictedclass))
                joblib.dump(model, 'models/final_eval/' + self.feature_name + '-' + model.__class__.__name__+ '-'+ name +'.pkl')
                for fold_idx, accuracy in enumerate(scores):
                    entries.append((name, fold_idx, accuracy))

            cv_df = pd.DataFrame(entries, columns=['model_name', 'fold_idx', 'accuracy'])
            mean_acc = cv_df.groupby(['model_name'], as_index=False, sort=False).accuracy.mean()
            f.write(str(mean_acc))
            f.write('\n\n')
            print(mean_acc)
            #-----------visualization of models and accuracies---------
            # sns.barplot(x='model_name', y = 'accuracy', data=cv_df)
            # plt.show()

