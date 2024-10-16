# Use a base image with Conda installed
FROM continuumio/miniconda3

# Set the working directory
WORKDIR /usr/src/app

# Update the package list and install build-essential
RUN apt-get update && \
    apt-get install -y build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Optionally, copy your other application files
COPY . .

# Create the conda environment with the necessary dependencies
RUN conda create --name pygeoflood-env python=3.11

# Activate the environment and install pygeoflood
RUN /bin/bash -c "source activate pygeoflood-env && pip install -e ./pygeoflood && pip list"

# Ensure the `run.sh` script is executable (if it exists)
RUN chmod +x ./run.sh

# Set the entry point for the container with Conda environment activation
ENTRYPOINT ["/bin/bash", "-c", "source activate pygeoflood-env && ./run.sh"]