import joblib as jb
print("---------------------------------------------------------------------")
print("           Model:Salary Prediction from year of experience           ")
print("---------------------------------------------------------------------")
exp=5.5
mind=jb.load('model_salary_predict.pk1')
salary = mind.predict([[exp]])
print("Salary will be:",salary)
