const form = document.getElementById('formFilme');

form.addEventListener('submit', function(event) {
    event.preventDefault(); // Evita o envio padrão do formulário

    const nome = document.getElementById('nomeFilme').value;
    const dataLancamento = document.getElementById('dataLancamento').value;
    const genero = document.getElementById('generoFilme').value;
    const duracao = document.getElementById('duracaoFilme').value;
    const sinopse = document.getElementById('sinopseFilme').value;

    // Validação básica dos dados (opcional)

    if (nome === '' || dataLancamento === '' || genero === '' || duracao === '' || sinopse === '') {
        alert('Preencha todos os campos!');
        return;
    }

    // Enviar dados para o servidor (via AJAX, por exemplo)
    // ...

    alert('Filme adicionado com sucesso!');

    // Limpar o formulário
    form.reset();
});
