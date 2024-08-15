import matplotlib.pyplot as plt
import pandas as pd

# Dados de exemplo
data = {
    "Data": ["12/08/2024", "13/08/2024", "14/08/2024", "15/08/2024"],
    "Éberton": [93.4, 91.9, 90.7, 90.4],
    "Arlete": [99.6, 97.9, 97.6, 97.7]
}

# Criar um DataFrame
df = pd.DataFrame(data)

# Converter a coluna de datas para datetime
df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')

# Calcular a diferença de peso para Éberton e Arlete
df['Diferença Éberton'] = df['Éberton'].diff().fillna(0)
df['Diferença Arlete'] = df['Arlete'].diff().fillna(0)

# Calcular a soma total da diferença de peso para Éberton e Arlete
total_diff_eberton = df['Diferença Éberton'].sum()
total_diff_arlete = df['Diferença Arlete'].sum()

# Criar um gráfico ajustado
plt.figure(figsize=(14, 7))
plt.plot(df['Data'], df['Éberton'], linestyle='-', color='#00CBBF', label=f"Éberton {total_diff_eberton:.1f}kg", marker='o', markersize=8)  # Cor do Éberton
plt.plot(df['Data'], df['Arlete'], linestyle='-', color='#F857C1', label=f"Arlete {total_diff_arlete:.1f}kg", marker='o', markersize=8)  # Cor da Arlete

# Adicionar os valores dos pesos e diferença nos pontos
for i in range(len(df)):
    plt.text(df['Data'][i], df['Éberton'][i] + 0.2, f"{df['Éberton'][i]}kg", ha='center', fontsize=10, color='black', fontweight='bold')
    plt.text(df['Data'][i], df['Arlete'][i] + 0.2, f"{df['Arlete'][i]}kg", ha='center', fontsize=10, color='black', fontweight='bold')
    plt.text(df['Data'][i], df['Éberton'][i] - 1, f"Dif: {df['Diferença Éberton'][i]:.1f}kg", ha='center', fontsize=10, color='green' if df['Diferença Éberton'][i] < 0 else 'red')
    plt.text(df['Data'][i], df['Arlete'][i] - 1, f"Dif: {df['Diferença Arlete'][i]:.1f}kg", ha='center', fontsize=10, color='green' if df['Diferença Arlete'][i] < 0 else 'red')

# Configurações do gráfico
plt.title('Gráfico Diário de Peso com Diferença e Soma Total na Legenda', fontsize=16, fontweight='bold')
plt.xlabel('Data', fontsize=12)
plt.ylabel('Peso (kg)', fontsize=12)
plt.xticks(df['Data'], df['Data'].dt.strftime('%d/%m/%Y'), fontsize=10)
plt.yticks(fontsize=10)

# Posicionar a legenda
plt.legend(title='', fontsize=10, title_fontsize=12, loc='center', bbox_to_anchor=(0.9, 0.9), shadow=True)

plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()

# Extrair a última data e formatá-la para usar no nome do arquivo
ultima_data = df['Data'].iloc[-1].strftime('%d-%m-%Y')

# Salvar o gráfico em um arquivo com a última data no nome
filename = f'grafico_peso_{ultima_data}.png'
plt.savefig(filename)

# Alternativa: Se estiver em um ambiente que suporta janelas gráficas
# plt.show()

print(f"Gráfico salvo como {filename}")
