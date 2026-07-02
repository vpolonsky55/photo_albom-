import React from 'react';
import { format } from 'date-fns';
import { ru } from 'date-fns/locale';

const PhotoCard = ({ photo }) => {
    const imageUrl = photo.image_url || 'https://via.placeholder.com/400x300/2d2d44/ffffff?text=No+Image';
    
    //Форматирует дату в человеческий вид (25.06.2025 14:30)
    const formatDate = (date) => {
        if (!date) return '—';
        try {
            return format(new Date(date), 'dd.MM.yyyy HH:mm', { locale: ru });
        } catch {
            return date;
        }
    };

    return (
        <div className="photo-card">
            <div className="photo-image">
                <img src={imageUrl} alt={photo.title || 'Фото'} />
            </div>
            
            <div className="photo-info">
                {photo.title && <h3 className="photo-title">{photo.title}</h3>}
                {photo.description && <p className="photo-description">{photo.description}</p>}
                
                <div className="photo-meta">
                    <span className="photo-date">
                        📅 Добавлено: {formatDate(photo.created_at)}
                    </span>
                    {photo.photo_date && (
                        <span className="photo-date">
                            📷 Снято: {formatDate(photo.photo_date)}
                        </span>
                    )}
                </div>
                
                <div className="photo-categories">
                    {photo.categories && photo.categories.map((cat) => (
                        <span key={cat.id} className="category-badge">
                            {cat.name}
                        </span>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default PhotoCard;