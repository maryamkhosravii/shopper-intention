FROM tensorflow/tensorflow:2.20.0

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    gfortran \
    g++ \
    python3-dev \
    libatlas-base-dev \
    libblas-dev \
    liblapack-dev \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip setuptools wheel \
    && pip install --ignore-installed blinker \
    && pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt


COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]