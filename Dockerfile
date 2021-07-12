FROM centos
RUN yum install python3 -y
RUN pip3 install numpy
RUN pip3 install joblib
RUN pip3 install scipy
RUN pip3 install sklearn 
COPY model_salary_predict.pk1 /
COPY predict_salary.py  /  
CMD python3 predict_salary.py
