import React from 'react';


// categories	Массив категорий из Django
// selectedCategory	Текущая выбранная категория (или пустая строка)
// onSelectCategory	Функция, которая вызывается при клике на кнопку
const CategoryFilter = ({ categories, selectedCategory, onSelectCategory }) => {
    return (
        <div className="category-filter">
            <button
                className={!selectedCategory ? 'active' : ''}
                onClick={() => onSelectCategory('')}
            >
                Все фото
            </button>
            
            {categories.map((category) => (
                <button
                    key={category.id}
                    className={selectedCategory === category.slug ? 'active' : ''}
                    onClick={() => onSelectCategory(category.slug)}
                >
                    {category.name}
                </button>
            ))}
        </div>
    );
};

export default CategoryFilter;