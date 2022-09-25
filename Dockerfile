# start by pulling the python image
FROM python:3.10-buster

# copy the requirements file into the image
COPY . /app
WORKDIR /app

#COPY ./requirements.txt /app/requirements.txt

# # switch working directory

# # install the dependencies and packages in the requirements file
# RUN pip install -r requirements.txt

# # copy every content from the local file to the image

# # configure the container to run in an executed manner

# CMD ["python","app.py" ]