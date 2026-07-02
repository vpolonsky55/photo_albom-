import React, { useState, useEffect } from 'react';
import { getPhotos, getCategories } from '../api';
import PhotoCard from './PhotoCard';
import CategoryFilter from './CategoryFilter';

const PhotoList = () => {
    const [photos, setPhotos] = useState([]);
    const [categories, setCategories] = useState([]);
    const [loading, setLoading] = useState(true);
    const [selectedCategory, setSelectedCategory] = useState(''); //Выбранная категория
    const [error, setError] = useState(null);

    // Загружает данные при монтировании и при смене категории
    useEffect(() => {
        const fetchData = async () => {
            try {
                setLoading(true);

                //Загружает одновременно фото и категории
                const [photosRes, categoriesRes] = await Promise.all([ 
                    getPhotos(selectedCategory), //Если категория выбрана — фильтрует
                    getCategories() 
                ]);

                setPhotos(photosRes.data.results || photosRes.data);
                setCategories(categoriesRes.data.results || categoriesRes.data);
                setError(null);
            } catch (err) {
                console.error('Ошибка загрузки:', err);
                setError('Не удалось загрузить данные');
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, [selectedCategory]);

    if (loading) {
        return <div className="loading">📸 Загрузка...</div>;
    }

    if (error) {
        return <div className="error">{error}</div>;
    }

    return (
        <div className="photo-list">
            <CategoryFilter 
                categories={categories}
                selectedCategory={selectedCategory}
                onSelectCategory={setSelectedCategory}
            />
            
            <div className="photos-grid">
                {photos.length === 0 ? (
                    <div className="no-photos">Фотографий пока нет</div>
                ) : (
                    photos.map((photo) => (
                        <PhotoCard key={photo.id} photo={photo} />
                    ))
                )}
            </div>
        </div>
    );
};

export default PhotoList;