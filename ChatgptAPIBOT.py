import openai

# Adicione sua chave de API aqui
openai.api_key = "INSERT API HERE"

def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

# Exemplo de uso
prompt = input('Faça sua pergunta para o ChatGPT: \n')
print(generate_text(prompt))
