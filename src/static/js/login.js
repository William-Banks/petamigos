document.getElementById("login-form").addEventListener("submit", async (e) => {
  e.preventDefault();

  const email = document.getElementById("email").value;
  const senha = document.getElementById("senha").value;
  const erroMsg = document.getElementById("erro-msg");

  try {
    const resposta = await fetch("http://localhost:5000/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, senha }),
    });

    if (resposta.ok) {
      const dados = await resposta.json();
      localStorage.setItem("usuario", JSON.stringify(dados));
      window.location.href = "index.html";
    } else {
      erroMsg.textContent = "E-mail ou senha inválidos.";
    }
  } catch (erro) {
    erroMsg.textContent = "Erro ao conectar com o servidor.";
  }
});
