let posts = [];

function criarPost() {

    let destino = document.getElementById("destino").value;
    let planejado = document.getElementById("planejado").value;
    let real = document.getElementById("real").value;
    let comentario = document.getElementById("comentario").value;

    if(destino === "" || planejado === "" || real === "" || comentario === "") {
        alert("Por favor, preencha todos os campos.");
        return;
    }

    let post = {
        destino: destino,
        planejado: planejado,
        real: real,
        comentario: comentario
    };

    posts.push(post);

    mostrarPosts();

    Document.getElementById("destino").value = "";
    Document.getElementById("planejado").value = "";
    Documento.getElementById("real").value = "";
    Document.getElementById("comentario").value = "";
}