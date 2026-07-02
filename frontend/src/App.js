import React from 'react';
import PhotoList from './components/PhotoList';
import './App.css';

function App() {
    return (
        <div className="app">
            <header className="app-header">
                <h1>📸 Фотоальбом</h1>
                <p className="subtitle">Мои любимые фотографии</p>
            </header>
            
            <main className="app-main">
                <PhotoList />
            </main>
            
            <footer className="app-footer">
                <p>© 2025 Фотоальбом. Все права защищены.</p>
            </footer>
        </div>
    );
}

export default App;


// 1. React (App.js) → рендерит PhotoList
// 2. PhotoList → вызывает useEffect
// 3. useEffect → вызывает getPhotos() и getCategories() из api.js
// 4. api.js → отправляет запросы на Django
// 5. Django → возвращает JSON с фото и категориями
// 6. React → сохраняет данные в state
// 7. React → рендерит карточки (PhotoCard) и фильтры (CategoryFilter)
// 8. Пользователь кликает на категорию → вызывается setSelectedCategory
// 9. selectedCategory меняется → useEffect срабатывает снова
// 10. Загружаются фото только для выбранной категории