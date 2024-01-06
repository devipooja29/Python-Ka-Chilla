# Model Training Report

## Introduction

A model was trained on dataset after EDA, data wrangling and hypothesis testing.

## Model Objective

The aim of model is to predict total recoveries when total cases and total tests are given.

## Model Selection

Multiple linear regression model was chosen for its simplicity and interpretability, supported by a strong linear relationship observed in the heatmap between 'Total Cases,' 'Total Tests,' and 'Total Recovered.' The model's coefficients provide clear insights into how changes in predictor variables impact the target, making it suitable for understanding recovery patterns. While acknowledging assumptions, the straightforward nature of relationships and the desire for an interpretable baseline model guided this choice.

## Model Training


The model training process involved splitting the dataset into training and testing sets using the train_test_split function from the sklearn.model_selection module. The data was divided into training and testing subsets with a test size of 20%, ensuring that the model's performance could be adequately evaluated. Subsequently, a grid search was performed to optimize the hyperparameters of the model using GridSearchCV from the same module. The parameter grid encompassed various options for fitting intercepts, copying input data, enforcing positivity, and configuring the number of parallel jobs. The grid search employed a 5-fold cross-validation approach, and the model's performance was evaluated using the R-squared (r2) scoring metric. After the grid search, the best parameters and corresponding best score were printed, providing insights into the optimal configuration for the model based on the training data.

The results of the grid search revealed the following optimal hyperparameters: 'copy_X': True, 'fit_intercept': True, 'n_jobs': None, and 'positive': True. The associated R-squared score, indicating the proportion of variance explained by the model on the training data, was 0.7463819984036325. These findings guide the selection of hyperparameters for the model, emphasizing the importance of features such as intercepts and positivity enforcement in achieving optimal performance.

## Model Evaluation
 
The model's performance was rigorously assessed through evaluation on the testing set using the R-squared metric. After training the model with optimized hyperparameters, predictions were generated on the testing data using the predict method. Subsequently, the R-squared score was calculated by comparing the predicted values (y_pred) to the actual target values (y_test). The R-squared score, accessed through the r2_score function from sklearn.metrics, quantifies the proportion of variance in the target variable explained by the model. A higher R-squared score, indicative of a better fit, suggests that the model generalizes well to unseen data. The obtained R-squared value on the testing set was then printed, revealing a high value of 0.916764935280859. This signifies that the model explains approximately 91.68% of the variance in the testing data, underscoring its robustness and effectiveness in making accurate predictions on previously unseen observations. This evaluation step is crucial for assessing how well the trained model extrapolates to new observations, ensuring its reliability in real-world scenarios.

## Conclusion


In conclusion, the developed multiple linear regression model, trained and evaluated on a dataset encompassing total cases, total tests, and total recoveries, demonstrates promising predictive capabilities. The model selection process favored simplicity and interpretability, aligning with the observed strong linear relationships in the heatmap between predictor and target variables. Following meticulous model training with hyperparameter optimization using grid search, the chosen configuration, including fitting intercepts, copying input data, and enforcing positivity, resulted in an R-squared score of 0.7463819984036325 on the training set.

Upon evaluation on the testing set, the model exhibited a notably high R-squared score of 0.916764935280859, indicating its ability to explain approximately 91.68% of the variance in unseen data. This performance underscores the model's robustness and effectiveness in making accurate predictions, validating its potential utility in forecasting total recoveries based on total cases and total tests. The systematic approach employed in model development, encompassing exploratory data analysis, hypothesis testing, and hyperparameter tuning, enhances confidence in the model's generalization to real-world scenarios. Further refinement and validation with additional datasets could contribute to the model's applicability and reliability in diverse contexts.
