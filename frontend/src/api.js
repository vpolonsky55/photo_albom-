import axios from 'axios'; // позволяет React отправлять GET, POST, PUT, DELETE запросы на сервер (Django).

const API_URL = 'http://127.0.0.1:8000/api';


// Создаёт копию axios с настройками	Чтобы не прописывать настройки каждый раз
const api = axios.create({
    baseURL: API_URL, // Базовый URL для всех запросов	Автоматически добавляет http://127.0.0.1:8000/api к каждому запросу 
    headers: { //Указывает, что отправляем JSON. Django REST Framework ожидает JSON
        'Content-Type': 'application/json',
    },
});

// Функция для получения списка фотографий с возможностью фильтрации по категории.
// getPhotos()  // ➡️ GET /api/photos/ (без фильтра)
// getPhotos('nature')  // ➡️ GET /api/photos/?categories__slug=nature (с фильтром)
export const getPhotos = (categorySlug = '') => { 
    let url = '/photos/'; // Базовый URL для запроса
    if (categorySlug) {
        url += `?categories__slug=${categorySlug}`; //Добавляем параметр фильтрации к URL
    }
    return api.get(url); //Отправляем GET-запрос на полученный URL
};


// Функция для получения списка всех категорий.
export const getCategories = () => {
    return api.get('/categories/'); //Отправляет GET-запрос на /api/categories/
};

export default api;