import React from 'react';
import VehicleList from './components/VehicleList';
import PredictForm from './components/PredictForm';
import Navbar from './components/Navbar';
import SearchComponent from './components/SearchComponent';
import VehicleCard from './components/VehicleCard';

function App() {
  return (
    <div className="bg-gray-100 min-h-screen">
      <Navbar />
      <main className="container mx-auto py-8">
        <PredictForm />
        
        <section className="mt-10">
          <SearchComponent />
        </section>
        



      </main>
    </div>
  );
}

export default App;
