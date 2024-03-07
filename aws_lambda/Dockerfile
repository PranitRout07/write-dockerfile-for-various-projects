FROM public.ecr.aws/lambda/python:3.8

#this part basically copies app.py to a location set by the environment variable . It is given by lambda .  
COPY app.py ${LAMBDA_TASK_ROOT}    
COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip install -r requirements.txt 
CMD ["app.handler"]
