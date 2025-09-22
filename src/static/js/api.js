const API_BASE_URL = ""; // Se sua API estiver em outro domínio ou porta, configure aqui, ex: "http://localhost:5000"

// Função genérica para tratar respostas
async function handleResponse(response) {
    if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        const error = new Error(errorData.erro || 'Erro desconhecido na API');
        error.status = response.status;
        throw error;
    }
    return response.json();
}

// GET
export async function apiGet(endpoint) {
    const response = await fetch(API_BASE_URL + endpoint, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            // 'Authorization': `Bearer ${getAuthToken()}`, // caso use token
        },
    });
    return handleResponse(response);
}

// POST
export async function apiPost(endpoint, data) {
    const response = await fetch(API_BASE_URL + endpoint, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            // 'Authorization': `Bearer ${getAuthToken()}`,
        },
        body: JSON.stringify(data),
    });
    return handleResponse(response);
}

// PUT
export async function apiPut(endpoint, data) {
    const response = await fetch(API_BASE_URL + endpoint, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            // 'Authorization': `Bearer ${getAuthToken()}`,
        },
        body: JSON.stringify(data),
    });
    return handleResponse(response);
}

// DELETE
export async function apiDelete(endpoint) {
    const response = await fetch(API_BASE_URL + endpoint, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            // 'Authorization': `Bearer ${getAuthToken()}`,
        },
    });
    if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        const error = new Error(errorData.erro || 'Erro desconhecido na API');
        error.status = response.status;
        throw error;
    }
    // DELETE pode não retornar JSON, então só retornar vazio
    return;
}

// Helper para pegar usuário logado no localStorage
export function getUsuarioLogado() {
    const usuario = localStorage.getItem("usuario");
    return usuario ? JSON.parse(usuario) : null;
}

// Se futuramente usar token Bearer, pode guardar aqui
export function getAuthToken() {
    const usuario = getUsuarioLogado();
    return usuario?.token || null;
}
