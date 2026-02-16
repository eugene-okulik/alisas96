FROM python
COPY program.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "program.py"]