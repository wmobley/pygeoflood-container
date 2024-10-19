# Use a base image with Conda installed
FROM continuumio/miniconda3

# Update the package list and install build-essential
RUN apt-get update && \
    apt-get install -y build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy your application files
COPY --chmod=755 run.sh /tapis/run.sh
COPY main.py /code/main.py

# Create the conda environment with the necessary dependencies and install pygeoflood
RUN conda create --name pygeoflood-env python=3.11 --yes && \
    conda run -n pygeoflood-env pip install git+https://github.com/tobiashi26/pygeoflood.git && \
    conda clean --all --yes  # Clean up unnecessary files to reduce image size

# Ensure the `run.sh` script is executable
RUN chmod +x /tapis/run.sh

# Set the entry point for the container with Conda environment activation
ENTRYPOINT ["/bin/bash", "-c", "source activate pygeoflood-env && /tapis/run.sh"]