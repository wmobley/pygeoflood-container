# Use a base image with Conda installed
FROM continuumio/miniconda3

# Update the package list and install build-essential
RUN apt-get update && \
    apt-get install -y build-essential wget unzip && \
    apt-get clean &&\
    apt-get install -y proj-data &&\
    rm -rf /var/lib/apt/lists/*

# Create a directory for WhiteboxTools
RUN mkdir -p /opt/whitebox_tools

# Download and install WhiteboxTools in /opt/whitebox_tools
WORKDIR /opt/whitebox_tools

RUN wget https://www.whiteboxgeo.com/WBT_Linux/WhiteboxTools_linux_amd64.zip -O whitebox_tools.zip && \
    unzip whitebox_tools.zip && rm whitebox_tools.zip

WORKDIR /

# Set environment variables to include WhiteboxTools in PATH
ENV PATH="/opt/whitebox_tools/WhiteboxTools_linux_amd64/WBT:$PATH"
    
# Set environment variable for WhiteboxTools directory
ENV WBT_PATH="/opt/whitebox_tools/WhiteboxTools_linux_amd64/WBT"
    
# Copy your application files
COPY --chmod=755 run.sh /tapis/run.sh
COPY main.py /code/main.py
COPY environment.yml /code/environment.yml

# Create the conda environment with the necessary dependencies and install pygeoflood
# Create the conda environment with the necessary dependencies and install pygeoflood
RUN conda env create --name pygeoflood-env --file /code/environment.yml
RUN conda run -n pygeoflood-env pip install git+https://github.com/tobiashi26/pygeoflood.git && \
    conda run -n pygeoflood-env pip install whitebox && \
    conda clean --all --yes  # Clean up unnecessary files to reduce image size
    
# Set environment variables for Conda to avoid using 'source activate'
ENV PATH="/opt/conda/envs/pygeoflood-env/bin:$PATH"

ENV PYTHONPATH=/code

# Set the entry point for the container
ENTRYPOINT ["/tapis/run.sh"]