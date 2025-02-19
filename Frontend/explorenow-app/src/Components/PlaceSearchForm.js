import PropTypes from 'prop-types';
import React, { useState } from 'react';


export default function PlaceSearchForm({ onSearch, setLoading }) {
    const [place, setPlace] = useState('');
    const [error, setError] = useState('');

    const handleInputChange = (event) => {
        setPlace(event.target.value);
    };

    const validateInput = () => {
        if (place.trim() === '') {
            setError('Place name is required');
            return false;
        }
        setError('');
        return true;
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        if (!validateInput()) {
            return;
        }

        try {
            const url = 'http://localhost:8000/places/search/';
            setLoading(true);
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ name: place }),
            });

            console.log('Response status:', response.status);  // Log the response status

            if (!response.ok) {
                const errorData = await response.json();  // Parse the error response body
                console.log('Error response:', errorData);  // Log the error response body
                throw new Error('Failed to fetch data');
            }

            const data = await response.json();
            console.log('Fetched data:', data);  // Log the fetched data for debugging
            onSearch(data);
        } catch (error) {
            setError('Failed to fetch data');
            console.error(error);  // Log the error for debugging
        } finally {
            setLoading(false);
        }
    };


    return (
        <form onSubmit={handleSubmit} className="mb-4 my-4">
            <div className="form-group">
                <label className="form-label">
                    <strong>Place Name: &nbsp;</strong>
                    <input
                        type="text"
                        value={place}
                        onChange={handleInputChange}
                    />
                </label>
            </div>
            {error && <p className="text-danger">{error}</p>}
            <button type="submit" className="btn btn-primary mt-3">Search</button>
        </form>
    )
}

PlaceSearchForm.propTypes = {
    onSearch: PropTypes.func.isRequired,
    setLoading: PropTypes.func.isRequired,
};
