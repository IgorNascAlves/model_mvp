# model MVP
==============================

Objetivo:

- [X] Recebemos um notebook (criacao_modelo.ipynb), um modelo (finalized_model.sav) e dados crus(002_20_all_Q.csv);
- [ ] Refatorar código notebook buscando identificar pipelines, métricas e bibliotecas;
- [ ] Criar dados de treinamento;
- [ ] Criar pipeline para gerar dados de treinamento a partir de novos dados;
- [X] Disponível em produção (FAST API);
- [X] Nuvem (Heroku);
 
Estudo:

- [X] [MLOps: Machine Learning e APIs](https://cursos.alura.com.br/course/mlops-machine-learning-e-apis)
- [X] [Machine Learning e o MLOps](https://cursos.alura.com.br/extra/hipsterstech/machine-learning-e-o-mlops-hipsters-171-a398)
- [X] [MLOps: deploy de modelos](https://cursos.alura.com.br/course/mlops-deploy-modelos)
- [ ] [Engenharia de machine learning](https://cursos.alura.com.br/extra/hipsterstech/engenharia-de-machine-learning-hipsters-ponto-tech-248-a853)
- [ ] [MLflow: gestão do ciclo de vidas de modelos de ML](https://cursos.alura.com.br/course/mlflow-gestao-ciclo-vidas-modelos-ml)


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
