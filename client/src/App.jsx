import React from 'react';
import VehicleList from './components/VehicleList';
import PredictForm from './components/PredictForm';
import Navbar from './components/Navbar';

function App() {
  return (
    <div className="bg-gray-100 min-h-screen">
      <Navbar />
      <main className="container mx-auto py-8">
        <PredictForm />
      </main>
    </div>
  );
}

export default App;