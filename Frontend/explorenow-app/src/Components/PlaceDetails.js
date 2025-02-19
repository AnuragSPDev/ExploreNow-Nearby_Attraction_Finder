import PropTypes from 'prop-types';
import React from 'react';


export default function PlaceDetails({ place }) {

    if (!place) {
        return <p className="text-center text-muted">Please enter a place to search.</p>;
    }

    return (
        <div className="card mt-4">
            <div className="card-body">
                <h2 className="card-title text-primary">{place.name}</h2>
                <div className="row">
                    <div className="col-md-6">
                        <p className="card-text"><strong>Latitude:</strong> {place.latitude}</p>
                    </div>
                    <div className="col-md-6">
                        <p className="card-text"><strong>Longitude:</strong> {place.longitude}</p>
                    </div>
                </div>
                <h3 className="mt-4">Attractions:</h3>
                <table className="table table-striped mt-3">
                    <thead>
                        <tr>
                            <th scope="col">Name</th>
                            <th scope="col">Category</th>
                            <th scope="col">Latitude</th>
                            <th scope="col">Longitude</th>
                        </tr>
                    </thead>
                    <tbody>
                        {place.attractions && place.attractions.length > 0 ? (
                            place.attractions.map((attraction) => (
                                <tr key={attraction.id}>
                                    <td>{attraction.name}</td>
                                    <td>{attraction.category_name}</td>
                                    <td>{attraction.latitude}</td>
                                    <td>{attraction.longitude}</td>
                                </tr>
                            ))
                        ) : (
                            <tr>
                                <td colSpan="4" className="text-muted text-center">No attractions found.</td>
                            </tr>
                        )}
                    </tbody>
                </table>
            </div>
        </div>
    )
}

PlaceDetails.propTypes = {
    place: PropTypes.shape({
        name: PropTypes.string.isRequired,
        latitude: PropTypes.number.isRequired,
        longitude: PropTypes.number.isRequired,
        attractions: PropTypes.arrayOf(
            PropTypes.shape({
                id: PropTypes.number.isRequired,
                name: PropTypes.string.isRequired,
                category_id: PropTypes.number,
                latitude: PropTypes.number.isRequired,
                longitude: PropTypes.number.isRequired,
            })
        ).isRequired,
    }),
};
