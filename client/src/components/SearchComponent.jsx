import React, { useState, useEffect } from 'react';
import axios from 'axios';
import VehicleCard from './VehicleCard';
import PriceTrendGraph from './PriceTrendGraph';

const SearchComponent = () => {
    const [make, setMake] = useState('');
    const [model, setModel] = useState('');
    const [filterType, setFilterType] = useState('');
    const [vehicles, setVehicles] = useState([]);
    const [trendData, setTrendData] = useState([]);
    const [page, setPage] = useState(1);
    const [pages, setPages] = useState(0);
    const [paginationRange, setPaginationRange] = useState([]);
    const [error, setError] = useState('');

    const searchVehicles = async (newPage = 1) => {
        try {
            setError('');
            const response = await axios.get('/api/vehicles', {
                params: { make, model, page: newPage, filter: filterType }
            });

            setVehicles(response.data.vehicles);
            setTrendData(response.data.trend_data);
            setPages(response.data.pages);
            setPage(newPage);

            // Generate pagination range
            const start = Math.max(newPage - 4, 1);
            const end = Math.min(newPage + 4, response.data.pages);
            setPaginationRange([...Array(end - start + 1).keys()].map(i => i + start));
        } catch (error) {
            if (error.response && error.response.data.error) {
                setError(error.response.data.error);
            } else {
                console.error('Error fetching vehicles:', error);
            }
        }
    };

    // Automatically fetch the results when the page number, filter, make, or model changes
    useEffect(() => {
        searchVehicles(page);
    }, [page, filterType, make, model]);

    return (
        <div className="bg-white p-6 rounded-lg shadow-md">
            <div className="flex items-center space-x-4 mb-6">
                <input
                    type="text"
                    value={make}
                    placeholder="Enter Make"
                    onChange={(e) => setMake(e.target.value)}
                    className="p-2 border border-gray-300 rounded-md w-1/3"
                />
                <input
                    type="text"
                    value={model}
                    placeholder="Enter Model"
                    onChange={(e) => setModel(e.target.value)}
                    className="p-2 border border-gray-300 rounded-md w-1/3"
                />
                <select
                    value={filterType}
                    onChange={(e) => setFilterType(e.target.value)}
                    className="p-2 border border-gray-300 rounded-md w-1/3"
                >
                    <option value="">No Filter</option>
                    <option value="price_asc">Price: Low to High</option>
                    <option value="price_desc">Price: High to Low</option>
                    <option value="year_asc">Year: Old to New</option>
                    <option value="year_desc">Year: New to Old</option>
                </select>
                <button
                    onClick={() => searchVehicles(1)}  // Reset to page 1 on new search
                    className="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600"
                >
                    Search
                </button>
            </div>

            {error && (
                <div className="text-red-500 mb-4">
                    {error}
                </div>
            )}

            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
                {vehicles.map(vehicle => (
                    <VehicleCard key={vehicle.id} vehicle={vehicle} />
                ))}
            </div>

            {trendData.length > 0 && (
                <div className="mt-10">
                    <PriceTrendGraph trendData={trendData} make={make} model={model} />
                </div>
            )}

            <div className="flex justify-center mt-8">
                {page > 1 && (
                    <button
                        onClick={() => setPage(page - 1)}
                        className="mx-1 px-4 py-2 rounded-md bg-gray-200 text-gray-700 hover:bg-gray-300"
                    >
                        Previous
                    </button>
                )}
                {paginationRange.map(p => (
                    <button
                        key={p}
                        onClick={() => setPage(p)}
                        className={`mx-1 px-4 py-2 rounded-md ${page === p ? 'bg-blue-500 text-white' : 'bg-gray-200 text-gray-700 hover:bg-gray-300'}`}
                    >
                        {p}
                    </button>
                ))}
                {page < pages && (
                    <button
                        onClick={() => setPage(page + 1)}
                        className="mx-1 px-4 py-2 rounded-md bg-gray-200 text-gray-700 hover:bg-gray-300"
                    >
                        Next
                    </button>
                )}
            </div>
        </div>
    );
};

export default SearchComponent;
