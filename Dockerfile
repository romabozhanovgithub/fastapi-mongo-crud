FROM python:3.10.4

# Set the working directory to /app
WORKDIR /app

# Install dependencies
RUN pip install --upgrade pip

# Copy the current directory contents into the container at /app
COPY . /app
COPY ./requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
