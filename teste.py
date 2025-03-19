import pandas as pd
from ydata_profiling import ProfileReport

# Criando um DataFrame pequeno para teste
data = {
    "Nome": ["Ana", "Bruno", "Carlos"],
    "Idade": [25, 30, 35],
    "Salário": [5000, 6000, 7000]
}

df = pd.DataFrame(data)

# Gerando o relatório
profile = ProfileReport(df, title="Test Report")
profile.to_file("test_output.html")
