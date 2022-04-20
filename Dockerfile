FROM continuumio/miniconda3

WORKDIR /app

COPY environment.yml .

RUN conda env create -f environment.yml

SHELL ["/bin/bash", "--login", "-c"]

COPY environment.yml main.py saved_steps.pkl .

ENTRYPOINT ["/opt/conda/envs/salary_pred/bin/streamlit", "run", "main.py"]
